# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: router.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import pam_pb2 as pam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0crouter.proto\x12\x06Router\x1a\tpam.proto\"r\n\x0eRouterResponse\x12\x30\n\x0cresponseCode\x18\x01 \x01(\x0e\x32\x1a.Router.RouterResponseCode\x12\x14\n\x0c\x65rrorMessage\x18\x02 \x01(\t\x12\x18\n\x10\x65ncryptedPayload\x18\x03 \x01(\x0c\"\xb2\x01\n\x17RouterControllerMessage\x12\x32\n\x0bmessageType\x18\x01 \x01(\x0e\x32\x1d.Router.ControllerMessageType\x12\x12\n\nmessageUid\x18\x02 \x01(\x0c\x12\x15\n\rcontrollerUid\x18\x03 \x01(\x0c\x12\x16\n\x0estreamResponse\x18\x04 \x01(\x08\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\x12\x0f\n\x07timeout\x18\x06 \x01(\x05\"\x92\x01\n\x0eRouterUserAuth\x12\x17\n\x0ftransmissionKey\x18\x01 \x01(\x0c\x12\x14\n\x0csessionToken\x18\x02 \x01(\x0c\x12\x0e\n\x06userId\x18\x03 \x01(\x05\x12\x18\n\x10\x65nterpriseUserId\x18\x04 \x01(\x03\x12\x12\n\ndeviceName\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65viceToken\x18\x06 \x01(\x0c\"\xb9\x01\n\x10RouterDeviceAuth\x12\x10\n\x08\x63lientId\x18\x01 \x01(\t\x12\x15\n\rclientVersion\x18\x02 \x01(\t\x12\x14\n\x0c\x65nterpriseId\x18\x03 \x01(\x05\x12\x0e\n\x06nodeId\x18\x04 \x01(\x03\x12\x12\n\ndeviceName\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65viceToken\x18\x06 \x01(\x0c\x12\x16\n\x0e\x63ontrollerName\x18\x07 \x01(\t\x12\x15\n\rcontrollerUid\x18\x08 \x01(\x0c\"n\n\x14RouterRecordRotation\x12\x11\n\trecordUid\x18\x01 \x01(\x0c\x12\x18\n\x10\x63onfigurationUid\x18\x02 \x01(\x0c\x12\x15\n\rcontrollerUid\x18\x03 \x01(\x0c\x12\x12\n\nnoSchedule\x18\x04 \x01(\x08\"E\n\x1cRouterRecordRotationsRequest\x12\x14\n\x0c\x65nterpriseId\x18\x01 \x01(\x05\x12\x0f\n\x07records\x18\x02 \x03(\x0c\"a\n\x1dRouterRecordRotationsResponse\x12/\n\trotations\x18\x01 \x03(\x0b\x32\x1c.Router.RouterRecordRotation\x12\x0f\n\x07hasMore\x18\x02 \x01(\x08\"\xd8\x01\n\x12RouterRotationInfo\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.Router.RouterRotationStatus\x12\x18\n\x10\x63onfigurationUid\x18\x02 \x01(\x0c\x12\x0e\n\x06nodeId\x18\x03 \x01(\x03\x12\x15\n\rcontrollerUid\x18\x04 \x01(\x0c\x12\x16\n\x0e\x63ontrollerName\x18\x05 \x01(\t\x12\x12\n\nscriptName\x18\x07 \x01(\t\x12\x15\n\rpwdComplexity\x18\x08 \x01(\t\x12\x10\n\x08\x64isabled\x18\t \x01(\x08\"\xb1\x01\n\x1bRouterRecordRotationRequest\x12\x11\n\trecordUid\x18\x01 \x01(\x0c\x12\x10\n\x08revision\x18\x02 \x01(\x03\x12\x18\n\x10\x63onfigurationUid\x18\x03 \x01(\x0c\x12\x10\n\x08schedule\x18\x04 \x01(\t\x12\x18\n\x10\x65nterpriseUserId\x18\x05 \x01(\x03\x12\x15\n\rpwdComplexity\x18\x06 \x01(\x0c\x12\x10\n\x08\x64isabled\x18\x07 \x01(\x08*\xb6\x01\n\x12RouterResponseCode\x12\n\n\x06RRC_OK\x10\x00\x12\x15\n\x11RRC_GENERAL_ERROR\x10\x01\x12\x13\n\x0fRRC_NOT_ALLOWED\x10\x02\x12\x13\n\x0fRRC_BAD_REQUEST\x10\x03\x12\x0f\n\x0bRRC_TIMEOUT\x10\x04\x12\x11\n\rRRC_BAD_STATE\x10\x05\x12\x17\n\x13RRC_CONTROLLER_DOWN\x10\x06\x12\x16\n\x12RRC_WRONG_INSTANCE\x10\x07*k\n\x14RouterRotationStatus\x12\x0e\n\nRRS_ONLINE\x10\x00\x12\x13\n\x0fRRS_NO_ROTATION\x10\x01\x12\x15\n\x11RRS_NO_CONTROLLER\x10\x02\x12\x17\n\x13RRS_CONTROLLER_DOWN\x10\x03\x42\"\n\x18\x63om.keepersecurity.protoB\x06Routerb\x06proto3')

_ROUTERRESPONSECODE = DESCRIPTOR.enum_types_by_name['RouterResponseCode']
RouterResponseCode = enum_type_wrapper.EnumTypeWrapper(_ROUTERRESPONSECODE)
_ROUTERROTATIONSTATUS = DESCRIPTOR.enum_types_by_name['RouterRotationStatus']
RouterRotationStatus = enum_type_wrapper.EnumTypeWrapper(_ROUTERROTATIONSTATUS)
RRC_OK = 0
RRC_GENERAL_ERROR = 1
RRC_NOT_ALLOWED = 2
RRC_BAD_REQUEST = 3
RRC_TIMEOUT = 4
RRC_BAD_STATE = 5
RRC_CONTROLLER_DOWN = 6
RRC_WRONG_INSTANCE = 7
RRS_ONLINE = 0
RRS_NO_ROTATION = 1
RRS_NO_CONTROLLER = 2
RRS_CONTROLLER_DOWN = 3


_ROUTERRESPONSE = DESCRIPTOR.message_types_by_name['RouterResponse']
_ROUTERCONTROLLERMESSAGE = DESCRIPTOR.message_types_by_name['RouterControllerMessage']
_ROUTERUSERAUTH = DESCRIPTOR.message_types_by_name['RouterUserAuth']
_ROUTERDEVICEAUTH = DESCRIPTOR.message_types_by_name['RouterDeviceAuth']
_ROUTERRECORDROTATION = DESCRIPTOR.message_types_by_name['RouterRecordRotation']
_ROUTERRECORDROTATIONSREQUEST = DESCRIPTOR.message_types_by_name['RouterRecordRotationsRequest']
_ROUTERRECORDROTATIONSRESPONSE = DESCRIPTOR.message_types_by_name['RouterRecordRotationsResponse']
_ROUTERROTATIONINFO = DESCRIPTOR.message_types_by_name['RouterRotationInfo']
_ROUTERRECORDROTATIONREQUEST = DESCRIPTOR.message_types_by_name['RouterRecordRotationRequest']
RouterResponse = _reflection.GeneratedProtocolMessageType('RouterResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERRESPONSE,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterResponse)
  })
_sym_db.RegisterMessage(RouterResponse)

RouterControllerMessage = _reflection.GeneratedProtocolMessageType('RouterControllerMessage', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERCONTROLLERMESSAGE,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterControllerMessage)
  })
_sym_db.RegisterMessage(RouterControllerMessage)

RouterUserAuth = _reflection.GeneratedProtocolMessageType('RouterUserAuth', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERUSERAUTH,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterUserAuth)
  })
_sym_db.RegisterMessage(RouterUserAuth)

RouterDeviceAuth = _reflection.GeneratedProtocolMessageType('RouterDeviceAuth', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERDEVICEAUTH,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterDeviceAuth)
  })
_sym_db.RegisterMessage(RouterDeviceAuth)

RouterRecordRotation = _reflection.GeneratedProtocolMessageType('RouterRecordRotation', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERRECORDROTATION,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterRecordRotation)
  })
_sym_db.RegisterMessage(RouterRecordRotation)

RouterRecordRotationsRequest = _reflection.GeneratedProtocolMessageType('RouterRecordRotationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERRECORDROTATIONSREQUEST,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterRecordRotationsRequest)
  })
_sym_db.RegisterMessage(RouterRecordRotationsRequest)

RouterRecordRotationsResponse = _reflection.GeneratedProtocolMessageType('RouterRecordRotationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERRECORDROTATIONSRESPONSE,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterRecordRotationsResponse)
  })
_sym_db.RegisterMessage(RouterRecordRotationsResponse)

RouterRotationInfo = _reflection.GeneratedProtocolMessageType('RouterRotationInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERROTATIONINFO,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterRotationInfo)
  })
_sym_db.RegisterMessage(RouterRotationInfo)

RouterRecordRotationRequest = _reflection.GeneratedProtocolMessageType('RouterRecordRotationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROUTERRECORDROTATIONREQUEST,
  '__module__' : 'router_pb2'
  # @@protoc_insertion_point(class_scope:Router.RouterRecordRotationRequest)
  })
_sym_db.RegisterMessage(RouterRecordRotationRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.keepersecurity.protoB\006Router'
  _ROUTERRESPONSECODE._serialized_start=1351
  _ROUTERRESPONSECODE._serialized_end=1533
  _ROUTERROTATIONSTATUS._serialized_start=1535
  _ROUTERROTATIONSTATUS._serialized_end=1642
  _ROUTERRESPONSE._serialized_start=35
  _ROUTERRESPONSE._serialized_end=149
  _ROUTERCONTROLLERMESSAGE._serialized_start=152
  _ROUTERCONTROLLERMESSAGE._serialized_end=330
  _ROUTERUSERAUTH._serialized_start=333
  _ROUTERUSERAUTH._serialized_end=479
  _ROUTERDEVICEAUTH._serialized_start=482
  _ROUTERDEVICEAUTH._serialized_end=667
  _ROUTERRECORDROTATION._serialized_start=669
  _ROUTERRECORDROTATION._serialized_end=779
  _ROUTERRECORDROTATIONSREQUEST._serialized_start=781
  _ROUTERRECORDROTATIONSREQUEST._serialized_end=850
  _ROUTERRECORDROTATIONSRESPONSE._serialized_start=852
  _ROUTERRECORDROTATIONSRESPONSE._serialized_end=949
  _ROUTERROTATIONINFO._serialized_start=952
  _ROUTERROTATIONINFO._serialized_end=1168
  _ROUTERRECORDROTATIONREQUEST._serialized_start=1171
  _ROUTERRECORDROTATIONREQUEST._serialized_end=1348
# @@protoc_insertion_point(module_scope)
