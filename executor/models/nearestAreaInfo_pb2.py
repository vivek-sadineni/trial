# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/nearestAreaInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import addressInfo_pb2 as executor_dot_models_dot_addressInfo__pb2
from executor.models import idInfo_pb2 as executor_dot_models_dot_idInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/nearestAreaInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n%executor/models/nearestAreaInfo.proto\x12\x1f\x66khp.data.layer.executor.models\x1a!executor/models/addressInfo.proto\x1a\x1c\x65xecutor/models/idInfo.proto\"\x8f\x01\n\x0fNearestAreaInfo\x12\x39\n\x08\x61reaInfo\x18\x01 \x01(\x0b\x32\'.fkhp.data.layer.executor.models.IdInfo\x12\x41\n\x0b\x61\x64\x64ressInfo\x18\x02 \x01(\x0b\x32,.fkhp.data.layer.executor.models.AddressInfoB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_addressInfo__pb2.DESCRIPTOR,executor_dot_models_dot_idInfo__pb2.DESCRIPTOR,])




_NEARESTAREAINFO = _descriptor.Descriptor(
  name='NearestAreaInfo',
  full_name='fkhp.data.layer.executor.models.NearestAreaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='areaInfo', full_name='fkhp.data.layer.executor.models.NearestAreaInfo.areaInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addressInfo', full_name='fkhp.data.layer.executor.models.NearestAreaInfo.addressInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=140,
  serialized_end=283,
)

_NEARESTAREAINFO.fields_by_name['areaInfo'].message_type = executor_dot_models_dot_idInfo__pb2._IDINFO
_NEARESTAREAINFO.fields_by_name['addressInfo'].message_type = executor_dot_models_dot_addressInfo__pb2._ADDRESSINFO
DESCRIPTOR.message_types_by_name['NearestAreaInfo'] = _NEARESTAREAINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NearestAreaInfo = _reflection.GeneratedProtocolMessageType('NearestAreaInfo', (_message.Message,), dict(
  DESCRIPTOR = _NEARESTAREAINFO,
  __module__ = 'executor.models.nearestAreaInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.NearestAreaInfo)
  ))
_sym_db.RegisterMessage(NearestAreaInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
