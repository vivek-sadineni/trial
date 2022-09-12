# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/userPurchaseInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/userPurchaseInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n&executor/models/userPurchaseInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"u\n\x10UserPurchaseInfo\x12\x14\n\x0ctotalSavings\x18\x02 \x01(\t\x12K\n\x10userPurchaseType\x18\x01 \x01(\x0e\x32\x31.fkhp.data.layer.executor.models.UserPurchaseType*N\n\x10UserPurchaseType\x12\x19\n\x15UserPurchaseType_NONE\x10\x00\x12\x11\n\rREPEATED_USER\x10\x01\x12\x0c\n\x08NEW_USER\x10\x02\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)

_USERPURCHASETYPE = _descriptor.EnumDescriptor(
  name='UserPurchaseType',
  full_name='fkhp.data.layer.executor.models.UserPurchaseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UserPurchaseType_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPEATED_USER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_USER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=194,
  serialized_end=272,
)
_sym_db.RegisterEnumDescriptor(_USERPURCHASETYPE)

UserPurchaseType = enum_type_wrapper.EnumTypeWrapper(_USERPURCHASETYPE)
UserPurchaseType_NONE = 0
REPEATED_USER = 1
NEW_USER = 2



_USERPURCHASEINFO = _descriptor.Descriptor(
  name='UserPurchaseInfo',
  full_name='fkhp.data.layer.executor.models.UserPurchaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalSavings', full_name='fkhp.data.layer.executor.models.UserPurchaseInfo.totalSavings', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userPurchaseType', full_name='fkhp.data.layer.executor.models.UserPurchaseInfo.userPurchaseType', index=1,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=75,
  serialized_end=192,
)

_USERPURCHASEINFO.fields_by_name['userPurchaseType'].enum_type = _USERPURCHASETYPE
DESCRIPTOR.message_types_by_name['UserPurchaseInfo'] = _USERPURCHASEINFO
DESCRIPTOR.enum_types_by_name['UserPurchaseType'] = _USERPURCHASETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserPurchaseInfo = _reflection.GeneratedProtocolMessageType('UserPurchaseInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERPURCHASEINFO,
  __module__ = 'executor.models.userPurchaseInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.UserPurchaseInfo)
  ))
_sym_db.RegisterMessage(UserPurchaseInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
