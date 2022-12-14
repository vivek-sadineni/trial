# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/OrderSuccessViewRequest.proto

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
  name='executor/request/OrderSuccessViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n.executor/request/OrderSuccessViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a\x1e\x65xecutor/models/userInfo.proto\x1a%executor/models/requestMetaInfo.proto\x1a!executor/models/paymentType.proto\"\xf5\x01\n\x17OrderSuccessViewRequest\x12;\n\x08userInfo\x18\x01 \x01(\x0b\x32).fkhp.data.layer.executor.models.UserInfo\x12I\n\x0frequestMetaInfo\x18\x02 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfo\x12\x41\n\x0bpaymentType\x18\x03 \x01(\x0e\x32,.fkhp.data.layer.executor.models.PaymentType\x12\x0f\n\x07orderId\x18\x04 \x01(\tB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_userInfo__pb2.DESCRIPTOR,executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_paymentType__pb2.DESCRIPTOR,])




_ORDERSUCCESSVIEWREQUEST = _descriptor.Descriptor(
  name='OrderSuccessViewRequest',
  full_name='fkhp.data.layer.executor.request.OrderSuccessViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.data.layer.executor.request.OrderSuccessViewRequest.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.OrderSuccessViewRequest.requestMetaInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paymentType', full_name='fkhp.data.layer.executor.request.OrderSuccessViewRequest.paymentType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderId', full_name='fkhp.data.layer.executor.request.OrderSuccessViewRequest.orderId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=191,
  serialized_end=436,
)

_ORDERSUCCESSVIEWREQUEST.fields_by_name['userInfo'].message_type = executor_dot_models_dot_userInfo__pb2._USERINFO
_ORDERSUCCESSVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
_ORDERSUCCESSVIEWREQUEST.fields_by_name['paymentType'].enum_type = executor_dot_models_dot_paymentType__pb2._PAYMENTTYPE
DESCRIPTOR.message_types_by_name['OrderSuccessViewRequest'] = _ORDERSUCCESSVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderSuccessViewRequest = _reflection.GeneratedProtocolMessageType('OrderSuccessViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _ORDERSUCCESSVIEWREQUEST,
  __module__ = 'executor.request.OrderSuccessViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.OrderSuccessViewRequest)
  ))
_sym_db.RegisterMessage(OrderSuccessViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
