# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/element/pmp/UIElementModelDefinition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.enums import UIElementValueType_pb2 as page_dot_models_dot_enums_dot_UIElementValueType__pb2
from page.models.enums import UIElementType_pb2 as page_dot_models_dot_enums_dot_UIElementType__pb2
from page.models.design.pmp import DesignParameter_pb2 as page_dot_models_dot_design_dot_pmp_dot_DesignParameter__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/element/pmp/UIElementModelDefinition.proto',
  package='fkhp.page.layer.models.element.pmp',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.page.layer.models.element.pmpP\001'),
  serialized_pb=_b('\n6page/models/element/pmp/UIElementModelDefinition.proto\x12\"fkhp.page.layer.models.element.pmp\x1a*page/models/enums/UIElementValueType.proto\x1a%page/models/enums/UIElementType.proto\x1a,page/models/design/pmp/DesignParameter.proto\"\xa2\x03\n\x18UIElementModelDefinition\x12\x13\n\x0buiElementId\x18\x01 \x01(\t\x12\x43\n\tvalueType\x18\x02 \x01(\x0e\x32\x30.fkhp.page.layer.models.enums.UIElementValueType\x12\x42\n\ruiElementType\x18\x03 \x01(\x0e\x32+.fkhp.page.layer.models.enums.UIElementType\x12L\n\x10\x64\x65signParameters\x18\x04 \x03(\x0b\x32\x32.fkhp.page.layer.models.design.pmp.DesignParameter\x12S\n\rchildElements\x18\x05 \x03(\x0b\x32<.fkhp.page.layer.models.element.pmp.UIElementModelDefinition\x12\x14\n\x0c\x65lementValue\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65\x66\x61ultValue\x18\x07 \x01(\t\x12\x19\n\x11isActionMandatory\x18\x08 \x01(\x08\x42&\n\"fkhp.page.layer.models.element.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_enums_dot_UIElementValueType__pb2.DESCRIPTOR,page_dot_models_dot_enums_dot_UIElementType__pb2.DESCRIPTOR,page_dot_models_dot_design_dot_pmp_dot_DesignParameter__pb2.DESCRIPTOR,])




_UIELEMENTMODELDEFINITION = _descriptor.Descriptor(
  name='UIElementModelDefinition',
  full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiElementId', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.uiElementId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.valueType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uiElementType', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.uiElementType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='designParameters', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.designParameters', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='childElements', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.childElements', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elementValue', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.elementValue', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultValue', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.defaultValue', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isActionMandatory', full_name='fkhp.page.layer.models.element.pmp.UIElementModelDefinition.isActionMandatory', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=224,
  serialized_end=642,
)

_UIELEMENTMODELDEFINITION.fields_by_name['valueType'].enum_type = page_dot_models_dot_enums_dot_UIElementValueType__pb2._UIELEMENTVALUETYPE
_UIELEMENTMODELDEFINITION.fields_by_name['uiElementType'].enum_type = page_dot_models_dot_enums_dot_UIElementType__pb2._UIELEMENTTYPE
_UIELEMENTMODELDEFINITION.fields_by_name['designParameters'].message_type = page_dot_models_dot_design_dot_pmp_dot_DesignParameter__pb2._DESIGNPARAMETER
_UIELEMENTMODELDEFINITION.fields_by_name['childElements'].message_type = _UIELEMENTMODELDEFINITION
DESCRIPTOR.message_types_by_name['UIElementModelDefinition'] = _UIELEMENTMODELDEFINITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UIElementModelDefinition = _reflection.GeneratedProtocolMessageType('UIElementModelDefinition', (_message.Message,), dict(
  DESCRIPTOR = _UIELEMENTMODELDEFINITION,
  __module__ = 'page.models.element.pmp.UIElementModelDefinition_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.element.pmp.UIElementModelDefinition)
  ))
_sym_db.RegisterMessage(UIElementModelDefinition)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
