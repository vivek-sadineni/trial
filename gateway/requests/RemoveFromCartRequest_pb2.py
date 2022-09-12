# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/requests/RemoveFromCartRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.models.user import UserAddress_pb2 as gateway_dot_models_dot_user_dot_UserAddress__pb2
from gateway.models.app import AppInfo_pb2 as gateway_dot_models_dot_app_dot_AppInfo__pb2
from gateway.models.device import DeviceInfo_pb2 as gateway_dot_models_dot_device_dot_DeviceInfo__pb2
from gateway.models import CartProductInfo_pb2 as gateway_dot_models_dot_CartProductInfo__pb2
from gateway.models.user import UserInfo_pb2 as gateway_dot_models_dot_user_dot_UserInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/requests/RemoveFromCartRequest.proto',
  package='fkhp.gateway.layer.client.requests',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.requestsP\001'),
  serialized_pb=_b('\n,gateway/requests/RemoveFromCartRequest.proto\x12\"fkhp.gateway.layer.client.requests\x1a%gateway/models/user/UserAddress.proto\x1a gateway/models/app/AppInfo.proto\x1a&gateway/models/device/DeviceInfo.proto\x1a$gateway/models/CartProductInfo.proto\x1a\"gateway/models/user/UserInfo.proto\"\xf6\x01\n\x15RemoveFromCartRequest\x12>\n\x07\x61ppInfo\x18\x01 \x01(\x0b\x32-.fkhp.gateway.layer.client.models.app.AppInfo\x12G\n\ndeviceInfo\x18\x02 \x01(\x0b\x32\x33.fkhp.gateway.layer.client.models.device.DeviceInfo\x12\x11\n\tproductId\x18\x03 \x01(\t\x12\x41\n\x08userInfo\x18\x04 \x01(\x0b\x32/.fkhp.gateway.layer.client.models.user.UserInfoB&\n\"fkhp.gateway.layer.client.requestsP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_models_dot_user_dot_UserAddress__pb2.DESCRIPTOR,gateway_dot_models_dot_app_dot_AppInfo__pb2.DESCRIPTOR,gateway_dot_models_dot_device_dot_DeviceInfo__pb2.DESCRIPTOR,gateway_dot_models_dot_CartProductInfo__pb2.DESCRIPTOR,gateway_dot_models_dot_user_dot_UserInfo__pb2.DESCRIPTOR,])




_REMOVEFROMCARTREQUEST = _descriptor.Descriptor(
  name='RemoveFromCartRequest',
  full_name='fkhp.gateway.layer.client.requests.RemoveFromCartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appInfo', full_name='fkhp.gateway.layer.client.requests.RemoveFromCartRequest.appInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceInfo', full_name='fkhp.gateway.layer.client.requests.RemoveFromCartRequest.deviceInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productId', full_name='fkhp.gateway.layer.client.requests.RemoveFromCartRequest.productId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.gateway.layer.client.requests.RemoveFromCartRequest.userInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=272,
  serialized_end=518,
)

_REMOVEFROMCARTREQUEST.fields_by_name['appInfo'].message_type = gateway_dot_models_dot_app_dot_AppInfo__pb2._APPINFO
_REMOVEFROMCARTREQUEST.fields_by_name['deviceInfo'].message_type = gateway_dot_models_dot_device_dot_DeviceInfo__pb2._DEVICEINFO
_REMOVEFROMCARTREQUEST.fields_by_name['userInfo'].message_type = gateway_dot_models_dot_user_dot_UserInfo__pb2._USERINFO
DESCRIPTOR.message_types_by_name['RemoveFromCartRequest'] = _REMOVEFROMCARTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveFromCartRequest = _reflection.GeneratedProtocolMessageType('RemoveFromCartRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEFROMCARTREQUEST,
  __module__ = 'gateway.requests.RemoveFromCartRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.requests.RemoveFromCartRequest)
  ))
_sym_db.RegisterMessage(RemoveFromCartRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)