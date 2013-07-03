"""autogenerated by genpy from kinect_depth_calibration/GetCheckerboardCenterRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetCheckerboardCenterRequest(genpy.Message):
  _md5sum = "cb32cbfa86e51d8153cc69cc05343fdf"
  _type = "kinect_depth_calibration/GetCheckerboardCenterRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 min_x
float32 max_x
float32 min_y
float32 max_y
float32 depth_prior

"""
  __slots__ = ['min_x','max_x','min_y','max_y','depth_prior']
  _slot_types = ['float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       min_x,max_x,min_y,max_y,depth_prior

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetCheckerboardCenterRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.min_x is None:
        self.min_x = 0.
      if self.max_x is None:
        self.max_x = 0.
      if self.min_y is None:
        self.min_y = 0.
      if self.max_y is None:
        self.max_y = 0.
      if self.depth_prior is None:
        self.depth_prior = 0.
    else:
      self.min_x = 0.
      self.max_x = 0.
      self.min_y = 0.
      self.max_y = 0.
      self.depth_prior = 0.

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
      _x = self
      buff.write(_struct_5f.pack(_x.min_x, _x.max_x, _x.min_y, _x.max_y, _x.depth_prior))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.min_x, _x.max_x, _x.min_y, _x.max_y, _x.depth_prior,) = _struct_5f.unpack(str[start:end])
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
      _x = self
      buff.write(_struct_5f.pack(_x.min_x, _x.max_x, _x.min_y, _x.max_y, _x.depth_prior))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.min_x, _x.max_x, _x.min_y, _x.max_y, _x.depth_prior,) = _struct_5f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_5f = struct.Struct("<5f")
"""autogenerated by genpy from kinect_depth_calibration/GetCheckerboardCenterResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GetCheckerboardCenterResponse(genpy.Message):
  _md5sum = "6deb06b7b7183f5581b3362a0cb413b7"
  _type = "kinect_depth_calibration/GetCheckerboardCenterResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 depth



"""
  __slots__ = ['depth']
  _slot_types = ['float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       depth

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetCheckerboardCenterResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.depth is None:
        self.depth = 0.
    else:
      self.depth = 0.

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
      buff.write(_struct_f.pack(self.depth))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.depth,) = _struct_f.unpack(str[start:end])
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
      buff.write(_struct_f.pack(self.depth))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.depth,) = _struct_f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f = struct.Struct("<f")
class GetCheckerboardCenter(object):
  _type          = 'kinect_depth_calibration/GetCheckerboardCenter'
  _md5sum = '1f713d495aa6446fb95738e3ba579737'
  _request_class  = GetCheckerboardCenterRequest
  _response_class = GetCheckerboardCenterResponse