# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/CreateOrderViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import userInfo_pb2 as executor_dot_models_dot_userInfo__pb2
from executor.models import requestMetaInfo_pb2 as executor_dot_models_dot_requestMetaInfo__pb2
from executor.models import paymentType_pb2 as executor_dot_models_dot_paymentType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/CreateOrderViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n-executor/request/CreateOrderViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a\x1e\x65xecutor/models/userInfo.proto\x1a%executor/models/requestMetaInfo.proto\x1a!executor/models/paymentType.proto\"\xf3\x01\n\x16\x43reateOrderViewRequest\x12;\n\x08userInfo\x18\x01 \x01(\x0b\x32).fkhp.data.layer.executor.models.UserInfo\x12I\n\x0frequestMetaInfo\x18\x02 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfo\x12\x12\n\ncampaignId\x18\x03 \x01(\t\x12\x10\n\x08stracker\x18\x04 \x01(\t\x12\x15\n\rstrackerValue\x18\x05 \x01(\t\x12\x14\n\x0cwalletAmount\x18\x06 \x01(\tB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_userInfo__pb2.DESCRIPTOR,executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_paymentType__pb2.DESCRIPTOR,])




_CREATEORDERVIEWREQUEST = _descriptor.Descriptor(
  name='CreateOrderViewRequest',
  full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest.requestMetaInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaignId', full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest.campaignId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stracker', full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest.stracker', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strackerValue', full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest.strackerValue', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='walletAmount', full_name='fkhp.data.layer.executor.request.CreateOrderViewRequest.walletAmount', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=190,
  serialized_end=433,
)

_CREATEORDERVIEWREQUEST.fields_by_name['userInfo'].message_type = executor_dot_models_dot_userInfo__pb2._USERINFO
_CREATEORDERVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
DESCRIPTOR.message_types_by_name['CreateOrderViewRequest'] = _CREATEORDERVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOrderViewRequest = _reflection.GeneratedProtocolMessageType('CreateOrderViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEORDERVIEWREQUEST,
  __module__ = 'executor.request.CreateOrderViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.CreateOrderViewRequest)
  ))
_sym_db.RegisterMessage(CreateOrderViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)