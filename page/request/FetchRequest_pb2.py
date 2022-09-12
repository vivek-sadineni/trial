# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/FetchRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.requests import AppInfo_pb2 as page_dot_models_dot_requests_dot_AppInfo__pb2
from page.models.requests import DeviceInfo_pb2 as page_dot_models_dot_requests_dot_DeviceInfo__pb2
from page.models.requests import UserInfo_pb2 as page_dot_models_dot_requests_dot_UserInfo__pb2
from page.models.requests import PageRequestInfo_pb2 as page_dot_models_dot_requests_dot_PageRequestInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/request/FetchRequest.proto',
  package='fkhp.page.layer.request',
  syntax='proto3',
  serialized_options=_b('\n\027fkhp.page.layer.requestP\001'),
  serialized_pb=_b('\n\x1fpage/request/FetchRequest.proto\x12\x17\x66khp.page.layer.request\x1a\"page/models/requests/AppInfo.proto\x1a%page/models/requests/DeviceInfo.proto\x1a#page/models/requests/UserInfo.proto\x1a*page/models/requests/PageRequestInfo.proto\"\xd5\x02\n\x0c\x46\x65tchRequest\x12\x11\n\tuserAgent\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\t\x12\x0e\n\x06\x63ookie\x18\x03 \x01(\t\x12\x0c\n\x04\x63srf\x18\x04 \x01(\t\x12\x39\n\x07\x61ppInfo\x18\x05 \x01(\x0b\x32(.fkhp.page.layer.models.requests.AppInfo\x12?\n\ndeviceInfo\x18\x06 \x01(\x0b\x32+.fkhp.page.layer.models.requests.DeviceInfo\x12;\n\x08userInfo\x18\x07 \x01(\x0b\x32).fkhp.page.layer.models.requests.UserInfo\x12I\n\x0fpageRequestInfo\x18\x08 \x01(\x0b\x32\x30.fkhp.page.layer.models.requests.PageRequestInfoB\x1b\n\x17\x66khp.page.layer.requestP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_requests_dot_AppInfo__pb2.DESCRIPTOR,page_dot_models_dot_requests_dot_DeviceInfo__pb2.DESCRIPTOR,page_dot_models_dot_requests_dot_UserInfo__pb2.DESCRIPTOR,page_dot_models_dot_requests_dot_PageRequestInfo__pb2.DESCRIPTOR,])




_FETCHREQUEST = _descriptor.Descriptor(
  name='FetchRequest',
  full_name='fkhp.page.layer.request.FetchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userAgent', full_name='fkhp.page.layer.request.FetchRequest.userAgent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='fkhp.page.layer.request.FetchRequest.clientId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cookie', full_name='fkhp.page.layer.request.FetchRequest.cookie', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='csrf', full_name='fkhp.page.layer.request.FetchRequest.csrf', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appInfo', full_name='fkhp.page.layer.request.FetchRequest.appInfo', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceInfo', full_name='fkhp.page.layer.request.FetchRequest.deviceInfo', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.page.layer.request.FetchRequest.userInfo', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageRequestInfo', full_name='fkhp.page.layer.request.FetchRequest.pageRequestInfo', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=217,
  serialized_end=558,
)

_FETCHREQUEST.fields_by_name['appInfo'].message_type = page_dot_models_dot_requests_dot_AppInfo__pb2._APPINFO
_FETCHREQUEST.fields_by_name['deviceInfo'].message_type = page_dot_models_dot_requests_dot_DeviceInfo__pb2._DEVICEINFO
_FETCHREQUEST.fields_by_name['userInfo'].message_type = page_dot_models_dot_requests_dot_UserInfo__pb2._USERINFO
_FETCHREQUEST.fields_by_name['pageRequestInfo'].message_type = page_dot_models_dot_requests_dot_PageRequestInfo__pb2._PAGEREQUESTINFO
DESCRIPTOR.message_types_by_name['FetchRequest'] = _FETCHREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchRequest = _reflection.GeneratedProtocolMessageType('FetchRequest', (_message.Message,), dict(
  DESCRIPTOR = _FETCHREQUEST,
  __module__ = 'page.request.FetchRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.FetchRequest)
  ))
_sym_db.RegisterMessage(FetchRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)