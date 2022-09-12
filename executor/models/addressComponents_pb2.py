# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/addressComponents.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import regionType_pb2 as executor_dot_models_dot_regionType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/addressComponents.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\'executor/models/addressComponents.proto\x12\x1f\x66khp.data.layer.executor.models\x1a executor/models/regionType.proto\"n\n\x11\x41\x64\x64ressComponents\x12?\n\nregionType\x18\x01 \x01(\x0e\x32+.fkhp.data.layer.executor.models.RegionType\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\tB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_regionType__pb2.DESCRIPTOR,])




_ADDRESSCOMPONENTS = _descriptor.Descriptor(
  name='AddressComponents',
  full_name='fkhp.data.layer.executor.models.AddressComponents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regionType', full_name='fkhp.data.layer.executor.models.AddressComponents.regionType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='fkhp.data.layer.executor.models.AddressComponents.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='fkhp.data.layer.executor.models.AddressComponents.name', index=2,
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
  serialized_start=110,
  serialized_end=220,
)

_ADDRESSCOMPONENTS.fields_by_name['regionType'].enum_type = executor_dot_models_dot_regionType__pb2._REGIONTYPE
DESCRIPTOR.message_types_by_name['AddressComponents'] = _ADDRESSCOMPONENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddressComponents = _reflection.GeneratedProtocolMessageType('AddressComponents', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSCOMPONENTS,
  __module__ = 'executor.models.addressComponents_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.AddressComponents)
  ))
_sym_db.RegisterMessage(AddressComponents)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)