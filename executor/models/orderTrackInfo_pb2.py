# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/orderTrackInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/orderTrackInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n$executor/models/orderTrackInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"r\n\x0eOrderTrackInfo\x12\x13\n\x0borderStatus\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x11\n\tupdatedBy\x18\x03 \x01(\t\x12\x15\n\rorderStatusId\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\tB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)




_ORDERTRACKINFO = _descriptor.Descriptor(
  name='OrderTrackInfo',
  full_name='fkhp.data.layer.executor.models.OrderTrackInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderStatus', full_name='fkhp.data.layer.executor.models.OrderTrackInfo.orderStatus', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='fkhp.data.layer.executor.models.OrderTrackInfo.date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatedBy', full_name='fkhp.data.layer.executor.models.OrderTrackInfo.updatedBy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderStatusId', full_name='fkhp.data.layer.executor.models.OrderTrackInfo.orderStatusId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='fkhp.data.layer.executor.models.OrderTrackInfo.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=73,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['OrderTrackInfo'] = _ORDERTRACKINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderTrackInfo = _reflection.GeneratedProtocolMessageType('OrderTrackInfo', (_message.Message,), dict(
  DESCRIPTOR = _ORDERTRACKINFO,
  __module__ = 'executor.models.orderTrackInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.OrderTrackInfo)
  ))
_sym_db.RegisterMessage(OrderTrackInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)