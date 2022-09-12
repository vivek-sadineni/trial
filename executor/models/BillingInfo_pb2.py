# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/BillingInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import addressInfo_pb2 as executor_dot_models_dot_addressInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/BillingInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n!executor/models/BillingInfo.proto\x12\x1f\x66khp.data.layer.executor.models\x1a!executor/models/addressInfo.proto\"d\n\x0b\x42illingInfo\x12\x11\n\tbillingId\x18\x01 \x01(\t\x12\x42\n\x0cshippingInfo\x18\x02 \x01(\x0b\x32,.fkhp.data.layer.executor.models.AddressInfoB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_addressInfo__pb2.DESCRIPTOR,])




_BILLINGINFO = _descriptor.Descriptor(
  name='BillingInfo',
  full_name='fkhp.data.layer.executor.models.BillingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='billingId', full_name='fkhp.data.layer.executor.models.BillingInfo.billingId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shippingInfo', full_name='fkhp.data.layer.executor.models.BillingInfo.shippingInfo', index=1,
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
  serialized_start=105,
  serialized_end=205,
)

_BILLINGINFO.fields_by_name['shippingInfo'].message_type = executor_dot_models_dot_addressInfo__pb2._ADDRESSINFO
DESCRIPTOR.message_types_by_name['BillingInfo'] = _BILLINGINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingInfo = _reflection.GeneratedProtocolMessageType('BillingInfo', (_message.Message,), dict(
  DESCRIPTOR = _BILLINGINFO,
  __module__ = 'executor.models.BillingInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.BillingInfo)
  ))
_sym_db.RegisterMessage(BillingInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
