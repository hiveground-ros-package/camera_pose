#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import roslib; roslib.load_manifest('camera_pose_calibration')
import rospy
import yaml
import sys
import actionlib
import time
import threading
import message_filters

import pr2_calibration_executive
from pr2_calibration_executive.config_manager import ConfigManager
from pr2_calibration_executive.robot_measurement_cache import RobotMeasurementCache

from calibration_msgs.msg import RobotMeasurement, Interval, CalibrationPattern, CameraMeasurement
from sensor_msgs.msg import CameraInfo, Image


class CameraCaptureExecutive:
    def __init__(self, cam_ids):
        self.cam_ids = cam_ids
        self.cache = RobotMeasurementCache()
        self.lock = threading.Lock()

        # Specifies if we're currently waiting for a sample
        self.active = False

        # Construct a manager for each sensor stream (Don't enable any of them)
        image_topic = rospy.get_param('~image_topic', 'image')
        image_rect_topic = rospy.get_param('~image_rect_topic', 'image_rect')
        cam_info_topic = rospy.get_param('~cam_info_topic', 'cam_info')

        self.cam_managers   = [ (cam_id,   CamManager(  cam_id,  image_topic,
                                                        image_rect_topic, cam_info_topic, 
                                                        self.add_cam_measurement) )   for cam_id   in cam_ids ]

        # Turn on all of the camera modes into verbose model, since we want the CalibrationPattern data
        for cam_manager in zip(*self.cam_managers)[1]:
            cam_manager.enable(verbose=True)

        # Subscribe to topic containing stable intervals
        self.measurement_pub = rospy.Publisher("robot_measurement", RobotMeasurement)
        self.request_interval_sub = rospy.Subscriber("request_interval", Interval, self.request_callback)

        # Set up the cache with only the sensors we care about
        chain_ids = []
        laser_ids = []
        self.cache.reconfigure(cam_ids, chain_ids, laser_ids)

    def request_callback(self, msg):

        print "Got a request callback"

        # See if the interval is big enough to care
        #if (msg.end - msg.start) < rospy.Duration(1,0):
        #    return

        self.lock.acquire()
        # Do some query into the cache
        m_robot = self.cache.request_robot_measurement(msg.start, msg.end, min_duration=rospy.Duration(0.01))

        # We found a sample, so we can deactive (kind of a race condition, since 'active' triggers capture() to exit... I don't care)
        if m_robot:
            # Change camera ids to be the tf frame IDs
            for cam in m_robot.M_cam:
                cam.camera_id = cam.image.header.frame_id
            self.measurement_pub.publish(m_robot)
        else:
            print "Couldn't get measurement in interval"
        self.lock.release()

    def add_cam_measurement(self, cam_id, msg):
        #print "Adding [%s]" % cam_id
        if len(msg.image_points) > 0:
            self.lock.acquire()
            self.cache.add_cam_measurement(cam_id, msg)
            self.lock.release()



class CamManager:
    def __init__(self, cam_id, image_topic, image_rect_topic, cam_info_topic, callback):
        self._cam_id = cam_id
        self._callback = callback
        self._mode = "off"

        self._lock = threading.Lock()

        # How do I specify a queue size of 1?                                                                                                                                
        self._features_sub = message_filters.Subscriber(cam_id + "/features", CalibrationPattern)
        self._cam_info_sub = message_filters.Subscriber(cam_id + "/" + cam_info_topic, CameraInfo)
        self._image_sub    = message_filters.Subscriber(cam_id + "/" + image_topic,    Image)
        self._image_rect_sub=message_filters.Subscriber(cam_id + "/" + image_rect_topic, Image)

        self._verbose_sync = message_filters.TimeSynchronizer([self._cam_info_sub, self._features_sub, self._image_sub, self._image_rect_sub], 10)
        self._minimal_sync = message_filters.TimeSynchronizer([self._cam_info_sub, self._features_sub], 10)

        self._verbose_sync.registerCallback(self.verbose_callback)
        self._minimal_sync.registerCallback(self.minimal_callback)

    def verbose_callback(self, cam_info, features, image, image_rect):
        self._lock.acquire()
        if self._mode is "verbose":
            # Populate measurement message                                                                                                                                   
            msg = CameraMeasurement()
            msg.header.stamp = cam_info.header.stamp
            msg.camera_id = self._cam_id
            msg.image_points = features.image_points
            msg.cam_info = cam_info
            msg.verbose = True
            msg.image = image
            msg.image_rect = image_rect
            msg.features = features
            self._callback(self._cam_id, msg)
        self._lock.release()

    def minimal_callback(self, cam_info, features):
        self._lock.acquire()
        if self._mode is "minimal":
            # Populate measurement message                                                                                                                                   
            msg = CameraMeasurement()
            msg.header.stamp = cam_info.header.stamp
            msg.camera_id = self._cam_id
            msg.image_points = features.image_points
            msg.cam_info = cam_info
            msg.verbose = False
            self._callback(self._cam_id, msg)
        self._lock.release()

    def enable(self, verbose=False):
        self._lock.acquire()
        if verbose:
            self._mode = "verbose"
        else:
            self._mode = "minimal"
        self._lock.release()

    def disable(self):
        self._lock.acquire()
        self._mode = "off"
        self._lock.release()



if __name__ == '__main__':
    rospy.init_node('capture_exec')
    args = rospy.myargv(sys.argv)

    # get list of camera's from arguments
    if len(args) < 2:
        rospy.logfatal("multicam_capture_exec.py needs camera's as arguments")
        raise
    camera_list = args[1:]
    executive = CameraCaptureExecutive(camera_list)
    rospy.spin()