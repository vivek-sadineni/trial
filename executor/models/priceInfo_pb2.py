# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/priceInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/priceInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\x1f\x65xecutor/models/priceInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"B\n\tPriceInfo\x12\x0b\n\x03mrp\x18\x01 \x01(\x01\x12\x14\n\x0csellingPrice\x18\x02 \x01(\x01\x12\x12\n\nfinalPrice\x18\x03 \x01(\x01\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)




_PRICEINFO = _descriptor.Descriptor(
  name='PriceInfo',
  full_name='fkhp.data.layer.executor.models.PriceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mrp', full_name='fkhp.data.layer.executor.models.PriceInfo.mrp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sellingPrice', full_name='fkhp.data.layer.executor.models.PriceInfo.sellingPrice', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finalPrice', full_name='fkhp.data.layer.executor.models.PriceInfo.finalPrice', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=68,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['PriceInfo'] = _PRICEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PriceInfo = _reflection.GeneratedProtocolMessageType('PriceInfo', (_message.Message,), dict(
  DESCRIPTOR = _PRICEINFO,
  __module__ = 'executor.models.priceInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.PriceInfo)
  ))
_sym_db.RegisterMessage(PriceInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)