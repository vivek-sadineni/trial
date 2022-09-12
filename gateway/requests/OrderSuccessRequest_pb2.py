# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/requests/OrderSuccessRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.models.app import AppInfo_pb2 as gateway_dot_models_dot_app_dot_AppInfo__pb2
from gateway.models.device import DeviceInfo_pb2 as gateway_dot_models_dot_device_dot_DeviceInfo__pb2
from gateway.models.enums import PaymentType_pb2 as gateway_dot_models_dot_enums_dot_PaymentType__pb2
from gateway.models.user import UserInfo_pb2 as gateway_dot_models_dot_user_dot_UserInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/requests/OrderSuccessRequest.proto',
  package='fkhp.gateway.layer.client.requests',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.requestsP\001'),
  serialized_pb=_b('\n*gateway/requests/OrderSuccessRequest.proto\x12\"fkhp.gateway.layer.client.requests\x1a gateway/models/app/AppInfo.proto\x1a&gateway/models/device/DeviceInfo.proto\x1a&gateway/models/enums/PaymentType.proto\x1a\"gateway/models/user/UserInfo.proto\"\xbc\x02\n\x13OrderSuccessRequest\x12>\n\x07\x61ppInfo\x18\x01 \x01(\x0b\x32-.fkhp.gateway.layer.client.models.app.AppInfo\x12G\n\ndeviceInfo\x18\x02 \x01(\x0b\x32\x33.fkhp.gateway.layer.client.models.device.DeviceInfo\x12H\n\x0bpaymentType\x18\x03 \x01(\x0e\x32\x33.fkhp.gateway.layer.client.models.enums.PaymentType\x12\x41\n\x08userInfo\x18\x04 \x01(\x0b\x32/.fkhp.gateway.layer.client.models.user.UserInfo\x12\x0f\n\x07orderId\x18\x05 \x01(\tB&\n\"fkhp.gateway.layer.client.requestsP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_models_dot_app_dot_AppInfo__pb2.DESCRIPTOR,gateway_dot_models_dot_device_dot_DeviceInfo__pb2.DESCRIPTOR,gateway_dot_models_dot_enums_dot_PaymentType__pb2.DESCRIPTOR,gateway_dot_models_dot_user_dot_UserInfo__pb2.DESCRIPTOR,])




_ORDERSUCCESSREQUEST = _descriptor.Descriptor(
  name='OrderSuccessRequest',
  full_name='fkhp.gateway.layer.client.requests.OrderSuccessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appInfo', full_name='fkhp.gateway.layer.client.requests.OrderSuccessRequest.appInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceInfo', full_name='fkhp.gateway.layer.client.requests.OrderSuccessRequest.deviceInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paymentType', full_name='fkhp.gateway.layer.client.requests.OrderSuccessRequest.paymentType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.gateway.layer.client.requests.OrderSuccessRequest.userInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderId', full_name='fkhp.gateway.layer.client.requests.OrderSuccessRequest.orderId', index=4,
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
  serialized_start=233,
  serialized_end=549,
)

_ORDERSUCCESSREQUEST.fields_by_name['appInfo'].message_type = gateway_dot_models_dot_app_dot_AppInfo__pb2._APPINFO
_ORDERSUCCESSREQUEST.fields_by_name['deviceInfo'].message_type = gateway_dot_models_dot_device_dot_DeviceInfo__pb2._DEVICEINFO
_ORDERSUCCESSREQUEST.fields_by_name['paymentType'].enum_type = gateway_dot_models_dot_enums_dot_PaymentType__pb2._PAYMENTTYPE
_ORDERSUCCESSREQUEST.fields_by_name['userInfo'].message_type = gateway_dot_models_dot_user_dot_UserInfo__pb2._USERINFO
DESCRIPTOR.message_types_by_name['OrderSuccessRequest'] = _ORDERSUCCESSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderSuccessRequest = _reflection.GeneratedProtocolMessageType('OrderSuccessRequest', (_message.Message,), dict(
  DESCRIPTOR = _ORDERSUCCESSREQUEST,
  __module__ = 'gateway.requests.OrderSuccessRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.requests.OrderSuccessRequest)
  ))
_sym_db.RegisterMessage(OrderSuccessRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
