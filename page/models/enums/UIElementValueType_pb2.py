# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/enums/UIElementValueType.proto

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
  name='page/models/enums/UIElementValueType.proto',
  package='fkhp.page.layer.models.enums',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.models.enumsP\001'),
  serialized_pb=_b('\n*page/models/enums/UIElementValueType.proto\x12\x1c\x66khp.page.layer.models.enums*o\n\x12UIElementValueType\x12\x16\n\x12\x44\x45\x46\x41ULT_VALUE_TYPE\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x08\n\x04TEXT\x10\x02\x12\x07\n\x03URL\x10\x03\x12\x08\n\x04LIST\x10\x04\x12\x0f\n\x0b\x43OMPOSITION\x10\x05\x12\x08\n\x04ICON\x10\x06\x42 \n\x1c\x66khp.page.layer.models.enumsP\x01\x62\x06proto3')
)

_UIELEMENTVALUETYPE = _descriptor.EnumDescriptor(
  name='UIElementValueType',
  full_name='fkhp.page.layer.models.enums.UIElementValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_VALUE_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPOSITION', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICON', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=76,
  serialized_end=187,
)
_sym_db.RegisterEnumDescriptor(_UIELEMENTVALUETYPE)

UIElementValueType = enum_type_wrapper.EnumTypeWrapper(_UIELEMENTVALUETYPE)
DEFAULT_VALUE_TYPE = 0
IMAGE = 1
TEXT = 2
URL = 3
LIST = 4
COMPOSITION = 5
ICON = 6


DESCRIPTOR.enum_types_by_name['UIElementValueType'] = _UIELEMENTVALUETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
