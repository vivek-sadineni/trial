# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/pmp/CreateUIComponentModelDefinitionResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.component.pmp import UIComponentModelDefinition_pb2 as page_dot_models_dot_component_dot_pmp_dot_UIComponentModelDefinition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/pmp/CreateUIComponentModelDefinitionResponse.proto',
  package='fkhp.page.layer.response.pmp',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.response.pmpP\001'),
  serialized_pb=_b('\n@page/response/pmp/CreateUIComponentModelDefinitionResponse.proto\x12\x1c\x66khp.page.layer.response.pmp\x1a:page/models/component/pmp/UIComponentModelDefinition.proto\"\xa0\x01\n(CreateUIComponentModelDefinitionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x64\n\x1auiComponentModelDefinition\x18\x02 \x01(\x0b\x32@.fkhp.page.layer.models.component.pmp.UIComponentModelDefinitionB \n\x1c\x66khp.page.layer.response.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_component_dot_pmp_dot_UIComponentModelDefinition__pb2.DESCRIPTOR,])




_CREATEUICOMPONENTMODELDEFINITIONRESPONSE = _descriptor.Descriptor(
  name='CreateUIComponentModelDefinitionResponse',
  full_name='fkhp.page.layer.response.pmp.CreateUIComponentModelDefinitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkhp.page.layer.response.pmp.CreateUIComponentModelDefinitionResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uiComponentModelDefinition', full_name='fkhp.page.layer.response.pmp.CreateUIComponentModelDefinitionResponse.uiComponentModelDefinition', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=159,
  serialized_end=319,
)

_CREATEUICOMPONENTMODELDEFINITIONRESPONSE.fields_by_name['uiComponentModelDefinition'].message_type = page_dot_models_dot_component_dot_pmp_dot_UIComponentModelDefinition__pb2._UICOMPONENTMODELDEFINITION
DESCRIPTOR.message_types_by_name['CreateUIComponentModelDefinitionResponse'] = _CREATEUICOMPONENTMODELDEFINITIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUIComponentModelDefinitionResponse = _reflection.GeneratedProtocolMessageType('CreateUIComponentModelDefinitionResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUICOMPONENTMODELDEFINITIONRESPONSE,
  __module__ = 'page.response.pmp.CreateUIComponentModelDefinitionResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.pmp.CreateUIComponentModelDefinitionResponse)
  ))
_sym_db.RegisterMessage(CreateUIComponentModelDefinitionResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
