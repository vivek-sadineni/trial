# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/requests/UserInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/requests/UserInfo.proto',
  package='fkhp.page.layer.models.requests',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.page.layer.models.requestsP\001'),
  serialized_pb=_b('\n#page/models/requests/UserInfo.proto\x12\x1f\x66khp.page.layer.models.requests\"N\n\x08UserInfo\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x10\n\x08userType\x18\x02 \x01(\t\x12\x10\n\x08loggedIn\x18\x03 \x01(\t\x12\x0b\n\x03org\x18\x04 \x01(\tB#\n\x1f\x66khp.page.layer.models.requestsP\x01\x62\x06proto3')
)




_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='fkhp.page.layer.models.requests.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountId', full_name='fkhp.page.layer.models.requests.UserInfo.accountId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userType', full_name='fkhp.page.layer.models.requests.UserInfo.userType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loggedIn', full_name='fkhp.page.layer.models.requests.UserInfo.loggedIn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='fkhp.page.layer.models.requests.UserInfo.org', index=3,
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
  serialized_start=72,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERINFO,
  __module__ = 'page.models.requests.UserInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.requests.UserInfo)
  ))
_sym_db.RegisterMessage(UserInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
