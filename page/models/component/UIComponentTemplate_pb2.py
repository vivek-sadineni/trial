# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/component/UIComponentTemplate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.design import DesignModel_pb2 as page_dot_models_dot_design_dot_DesignModel__pb2
from page.models.design import DataSourceTemplate_pb2 as page_dot_models_dot_design_dot_DataSourceTemplate__pb2
from page.models.element import UIElementTemplate_pb2 as page_dot_models_dot_element_dot_UIElementTemplate__pb2
from page.models.enums import UIComponentType_pb2 as page_dot_models_dot_enums_dot_UIComponentType__pb2
from page.models.element import UIElementAction_pb2 as page_dot_models_dot_element_dot_UIElementAction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/component/UIComponentTemplate.proto',
  package='fkhp.page.layer.models.component',
  syntax='proto3',
  serialized_options=_b('\n fkhp.page.layer.models.componentP\001'),
  serialized_pb=_b('\n/page/models/component/UIComponentTemplate.proto\x12 fkhp.page.layer.models.component\x1a$page/models/design/DesignModel.proto\x1a+page/models/design/DataSourceTemplate.proto\x1a+page/models/element/UIElementTemplate.proto\x1a\'page/models/enums/UIComponentType.proto\x1a)page/models/element/UIElementAction.proto\"\xdf\x05\n\x13UIComponentTemplate\x12\x15\n\ruiComponentId\x18\x01 \x01(\t\x12?\n\x0b\x64\x65signModel\x18\x02 \x01(\x0b\x32*.fkhp.page.layer.models.design.DesignModel\x12\x45\n\ndataSource\x18\x03 \x01(\x0b\x32\x31.fkhp.page.layer.models.design.DataSourceTemplate\x12\x1a\n\x12sectionComponentId\x18\x04 \x01(\t\x12\x45\n\nuiElements\x18\x05 \x03(\x0b\x32\x31.fkhp.page.layer.models.element.UIElementTemplate\x12\x46\n\x0fuiComponentType\x18\x06 \x01(\x0e\x32-.fkhp.page.layer.models.enums.UIComponentType\x12\x0f\n\x07version\x18\x07 \x01(\t\x12H\n\x0fuiElementAction\x18\x08 \x03(\x0b\x32/.fkhp.page.layer.models.element.UIElementAction\x12U\n\x08metaData\x18\t \x03(\x0b\x32\x43.fkhp.page.layer.models.component.UIComponentTemplate.MetaDataEntry\x12\x63\n\x0ftrackingContext\x18\n \x03(\x0b\x32J.fkhp.page.layer.models.component.UIComponentTemplate.TrackingContextEntry\x1a/\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14TrackingContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42$\n fkhp.page.layer.models.componentP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_design_dot_DesignModel__pb2.DESCRIPTOR,page_dot_models_dot_design_dot_DataSourceTemplate__pb2.DESCRIPTOR,page_dot_models_dot_element_dot_UIElementTemplate__pb2.DESCRIPTOR,page_dot_models_dot_enums_dot_UIComponentType__pb2.DESCRIPTOR,page_dot_models_dot_element_dot_UIElementAction__pb2.DESCRIPTOR,])




_UICOMPONENTTEMPLATE_METADATAENTRY = _descriptor.Descriptor(
  name='MetaDataEntry',
  full_name='fkhp.page.layer.models.component.UIComponentTemplate.MetaDataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.page.layer.models.component.UIComponentTemplate.MetaDataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.page.layer.models.component.UIComponentTemplate.MetaDataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=930,
  serialized_end=977,
)

_UICOMPONENTTEMPLATE_TRACKINGCONTEXTENTRY = _descriptor.Descriptor(
  name='TrackingContextEntry',
  full_name='fkhp.page.layer.models.component.UIComponentTemplate.TrackingContextEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.page.layer.models.component.UIComponentTemplate.TrackingContextEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.page.layer.models.component.UIComponentTemplate.TrackingContextEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=979,
  serialized_end=1033,
)

_UICOMPONENTTEMPLATE = _descriptor.Descriptor(
  name='UIComponentTemplate',
  full_name='fkhp.page.layer.models.component.UIComponentTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiComponentId', full_name='fkhp.page.layer.models.component.UIComponentTemplate.uiComponentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='designModel', full_name='fkhp.page.layer.models.component.UIComponentTemplate.designModel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataSource', full_name='fkhp.page.layer.models.component.UIComponentTemplate.dataSource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionComponentId', full_name='fkhp.page.layer.models.component.UIComponentTemplate.sectionComponentId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uiElements', full_name='fkhp.page.layer.models.component.UIComponentTemplate.uiElements', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uiComponentType', full_name='fkhp.page.layer.models.component.UIComponentTemplate.uiComponentType', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='fkhp.page.layer.models.component.UIComponentTemplate.version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uiElementAction', full_name='fkhp.page.layer.models.component.UIComponentTemplate.uiElementAction', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metaData', full_name='fkhp.page.layer.models.component.UIComponentTemplate.metaData', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trackingContext', full_name='fkhp.page.layer.models.component.UIComponentTemplate.trackingContext', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UICOMPONENTTEMPLATE_METADATAENTRY, _UICOMPONENTTEMPLATE_TRACKINGCONTEXTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=1033,
)

_UICOMPONENTTEMPLATE_METADATAENTRY.containing_type = _UICOMPONENTTEMPLATE
_UICOMPONENTTEMPLATE_TRACKINGCONTEXTENTRY.containing_type = _UICOMPONENTTEMPLATE
_UICOMPONENTTEMPLATE.fields_by_name['designModel'].message_type = page_dot_models_dot_design_dot_DesignModel__pb2._DESIGNMODEL
_UICOMPONENTTEMPLATE.fields_by_name['dataSource'].message_type = page_dot_models_dot_design_dot_DataSourceTemplate__pb2._DATASOURCETEMPLATE
_UICOMPONENTTEMPLATE.fields_by_name['uiElements'].message_type = page_dot_models_dot_element_dot_UIElementTemplate__pb2._UIELEMENTTEMPLATE
_UICOMPONENTTEMPLATE.fields_by_name['uiComponentType'].enum_type = page_dot_models_dot_enums_dot_UIComponentType__pb2._UICOMPONENTTYPE
_UICOMPONENTTEMPLATE.fields_by_name['uiElementAction'].message_type = page_dot_models_dot_element_dot_UIElementAction__pb2._UIELEMENTACTION
_UICOMPONENTTEMPLATE.fields_by_name['metaData'].message_type = _UICOMPONENTTEMPLATE_METADATAENTRY
_UICOMPONENTTEMPLATE.fields_by_name['trackingContext'].message_type = _UICOMPONENTTEMPLATE_TRACKINGCONTEXTENTRY
DESCRIPTOR.message_types_by_name['UIComponentTemplate'] = _UICOMPONENTTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UIComponentTemplate = _reflection.GeneratedProtocolMessageType('UIComponentTemplate', (_message.Message,), dict(

  MetaDataEntry = _reflection.GeneratedProtocolMessageType('MetaDataEntry', (_message.Message,), dict(
    DESCRIPTOR = _UICOMPONENTTEMPLATE_METADATAENTRY,
    __module__ = 'page.models.component.UIComponentTemplate_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.component.UIComponentTemplate.MetaDataEntry)
    ))
  ,

  TrackingContextEntry = _reflection.GeneratedProtocolMessageType('TrackingContextEntry', (_message.Message,), dict(
    DESCRIPTOR = _UICOMPONENTTEMPLATE_TRACKINGCONTEXTENTRY,
    __module__ = 'page.models.component.UIComponentTemplate_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.component.UIComponentTemplate.TrackingContextEntry)
    ))
  ,
  DESCRIPTOR = _UICOMPONENTTEMPLATE,
  __module__ = 'page.models.component.UIComponentTemplate_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.component.UIComponentTemplate)
  ))
_sym_db.RegisterMessage(UIComponentTemplate)
_sym_db.RegisterMessage(UIComponentTemplate.MetaDataEntry)
_sym_db.RegisterMessage(UIComponentTemplate.TrackingContextEntry)


DESCRIPTOR._options = None
_UICOMPONENTTEMPLATE_METADATAENTRY._options = None
_UICOMPONENTTEMPLATE_TRACKINGCONTEXTENTRY._options = None
# @@protoc_insertion_point(module_scope)
