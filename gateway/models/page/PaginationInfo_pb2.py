# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/models/page/PaginationInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/models/page/PaginationInfo.proto',
  package='fkhp.gateway.layer.client.models',
  syntax='proto3',
  serialized_options=_b('\n fkhp.gateway.layer.client.modelsP\001'),
  serialized_pb=_b('\n(gateway/models/page/PaginationInfo.proto\x12 fkhp.gateway.layer.client.models\"G\n\x0ePaginationInfo\x12\x12\n\npageNumber\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x0f\n\x07hasMore\x18\x03 \x01(\x08\x42$\n fkhp.gateway.layer.client.modelsP\x01\x62\x06proto3')
)




_PAGINATIONINFO = _descriptor.Descriptor(
  name='PaginationInfo',
  full_name='fkhp.gateway.layer.client.models.PaginationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageNumber', full_name='fkhp.gateway.layer.client.models.PaginationInfo.pageNumber', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='fkhp.gateway.layer.client.models.PaginationInfo.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasMore', full_name='fkhp.gateway.layer.client.models.PaginationInfo.hasMore', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=78,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['PaginationInfo'] = _PAGINATIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaginationInfo = _reflection.GeneratedProtocolMessageType('PaginationInfo', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATIONINFO,
  __module__ = 'gateway.models.page.PaginationInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.models.PaginationInfo)
  ))
_sym_db.RegisterMessage(PaginationInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)