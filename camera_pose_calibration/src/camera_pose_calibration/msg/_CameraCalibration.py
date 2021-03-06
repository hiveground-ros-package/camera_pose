"""autogenerated by genpy from camera_pose_calibration/CameraCalibration.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import genpy

class CameraCalibration(genpy.Message):
  _md5sum = "3cc5d376bac75efd371d4df5fb750ad6"
  _type = "camera_pose_calibration/CameraCalibration"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Pose[] camera_pose
string[] camera_id
time[] time_stamp
int32 m_count

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['camera_pose','camera_id','time_stamp','m_count']
  _slot_types = ['geometry_msgs/Pose[]','string[]','time[]','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       camera_pose,camera_id,time_stamp,m_count

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CameraCalibration, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.camera_pose is None:
        self.camera_pose = []
      if self.camera_id is None:
        self.camera_id = []
      if self.time_stamp is None:
        self.time_stamp = []
      if self.m_count is None:
        self.m_count = 0
    else:
      self.camera_pose = []
      self.camera_id = []
      self.time_stamp = []
      self.m_count = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.camera_pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_pose:
        _v1 = val1.position
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.camera_id)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_id:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.time_stamp)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_stamp:
        _x = val1
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
      buff.write(_struct_i.pack(self.m_count))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.camera_pose is None:
        self.camera_pose = None
      if self.time_stamp is None:
        self.time_stamp = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v3 = val1.position
        _x = _v3
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v4 = val1.orientation
        _x = _v4
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.camera_pose.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_id = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.camera_id.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.time_stamp = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        self.time_stamp.append(val1)
      start = end
      end += 4
      (self.m_count,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.camera_pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_pose:
        _v5 = val1.position
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = val1.orientation
        _x = _v6
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.camera_id)
      buff.write(_struct_I.pack(length))
      for val1 in self.camera_id:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.time_stamp)
      buff.write(_struct_I.pack(length))
      for val1 in self.time_stamp:
        _x = val1
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
      buff.write(_struct_i.pack(self.m_count))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.camera_pose is None:
        self.camera_pose = None
      if self.time_stamp is None:
        self.time_stamp = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v7 = val1.position
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v8 = val1.orientation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.camera_pose.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.camera_id = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.camera_id.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.time_stamp = []
      for i in range(0, length):
        val1 = genpy.Time()
        _x = val1
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        self.time_stamp.append(val1)
      start = end
      end += 4
      (self.m_count,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
