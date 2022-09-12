# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/appInfo.proto

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
  name='executor/models/appInfo.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\x1d\x65xecutor/models/appInfo.proto\x12\x1f\x66khp.data.layer.executor.models\"X\n\x07\x41ppInfo\x12\x12\n\nappVersion\x18\x01 \x01(\t\x12\x39\n\x07\x61ppType\x18\x02 \x01(\x0e\x32(.fkhp.data.layer.executor.models.AppType*7\n\x07\x41ppType\x12\x07\n\x03IOS\x10\x00\x12\t\n\x05MSITE\x10\x01\x12\x0b\n\x07\x41NDROID\x10\x02\x12\x0b\n\x07WEBSITE\x10\x03\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)

_APPTYPE = _descriptor.EnumDescriptor(
  name='AppType',
  full_name='fkhp.data.layer.executor.models.AppType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IOS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSITE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEBSITE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=156,
  serialized_end=211,
)
_sym_db.RegisterEnumDescriptor(_APPTYPE)

AppType = enum_type_wrapper.EnumTypeWrapper(_APPTYPE)
IOS = 0
MSITE = 1
ANDROID = 2
WEBSITE = 3



_APPINFO = _descriptor.Descriptor(
  name='AppInfo',
  full_name='fkhp.data.layer.executor.models.AppInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appVersion', full_name='fkhp.data.layer.executor.models.AppInfo.appVersion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appType', full_name='fkhp.data.layer.executor.models.AppInfo.appType', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=66,
  serialized_end=154,
)

_APPINFO.fields_by_name['appType'].enum_type = _APPTYPE
DESCRIPTOR.message_types_by_name['AppInfo'] = _APPINFO
DESCRIPTOR.enum_types_by_name['AppType'] = _APPTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppInfo = _reflection.GeneratedProtocolMessageType('AppInfo', (_message.Message,), dict(
  DESCRIPTOR = _APPINFO,
  __module__ = 'executor.models.appInfo_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.AppInfo)
  ))
_sym_db.RegisterMessage(AppInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
