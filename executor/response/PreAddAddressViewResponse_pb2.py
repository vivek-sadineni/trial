# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/PreAddAddressViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2
from executor.models import nearestAreaInfo_pb2 as executor_dot_models_dot_nearestAreaInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/PreAddAddressViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n1executor/response/PreAddAddressViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a\x19google/protobuf/any.proto\x1a executor/models/statusInfo.proto\x1a%executor/models/nearestAreaInfo.proto\"\xb5\x01\n\x19PreAddAddressViewResponse\x12?\n\nstatusInfo\x18\x01 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12\x42\n\x08\x61reaList\x18\x02 \x03(\x0b\x32\x30.fkhp.data.layer.executor.models.NearestAreaInfo\x12\x13\n\x0bphoneNumber\x18\x03 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_nearestAreaInfo__pb2.DESCRIPTOR,])




_PREADDADDRESSVIEWRESPONSE = _descriptor.Descriptor(
  name='PreAddAddressViewResponse',
  full_name='fkhp.data.layer.executor.response.PreAddAddressViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.PreAddAddressViewResponse.statusInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='areaList', full_name='fkhp.data.layer.executor.response.PreAddAddressViewResponse.areaList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='fkhp.data.layer.executor.response.PreAddAddressViewResponse.phoneNumber', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=370,
)

_PREADDADDRESSVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
_PREADDADDRESSVIEWRESPONSE.fields_by_name['areaList'].message_type = executor_dot_models_dot_nearestAreaInfo__pb2._NEARESTAREAINFO
DESCRIPTOR.message_types_by_name['PreAddAddressViewResponse'] = _PREADDADDRESSVIEWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreAddAddressViewResponse = _reflection.GeneratedProtocolMessageType('PreAddAddressViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _PREADDADDRESSVIEWRESPONSE,
  __module__ = 'executor.response.PreAddAddressViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PreAddAddressViewResponse)
  ))
_sym_db.RegisterMessage(PreAddAddressViewResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
