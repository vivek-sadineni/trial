# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/pmp/CreateUIComponentModelDefinitionRequest.proto

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
  name='page/request/pmp/CreateUIComponentModelDefinitionRequest.proto',
  package='fkhp.page.layer.request.pmp',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.request.pmpP\001'),
  serialized_pb=_b('\n>page/request/pmp/CreateUIComponentModelDefinitionRequest.proto\x12\x1b\x66khp.page.layer.request.pmp\x1a:page/models/component/pmp/UIComponentModelDefinition.proto\"\xa7\x01\n\'CreateUIComponentModelDefinitionRequest\x12\x64\n\x1auiComponentModelDefinition\x18\x01 \x01(\x0b\x32@.fkhp.page.layer.models.component.pmp.UIComponentModelDefinition\x12\x16\n\x0eupgradeVersion\x18\x02 \x01(\x08\x42\x1f\n\x1b\x66khp.page.layer.request.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_component_dot_pmp_dot_UIComponentModelDefinition__pb2.DESCRIPTOR,])




_CREATEUICOMPONENTMODELDEFINITIONREQUEST = _descriptor.Descriptor(
  name='CreateUIComponentModelDefinitionRequest',
  full_name='fkhp.page.layer.request.pmp.CreateUIComponentModelDefinitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiComponentModelDefinition', full_name='fkhp.page.layer.request.pmp.CreateUIComponentModelDefinitionRequest.uiComponentModelDefinition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upgradeVersion', full_name='fkhp.page.layer.request.pmp.CreateUIComponentModelDefinitionRequest.upgradeVersion', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=156,
  serialized_end=323,
)

_CREATEUICOMPONENTMODELDEFINITIONREQUEST.fields_by_name['uiComponentModelDefinition'].message_type = page_dot_models_dot_component_dot_pmp_dot_UIComponentModelDefinition__pb2._UICOMPONENTMODELDEFINITION
DESCRIPTOR.message_types_by_name['CreateUIComponentModelDefinitionRequest'] = _CREATEUICOMPONENTMODELDEFINITIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUIComponentModelDefinitionRequest = _reflection.GeneratedProtocolMessageType('CreateUIComponentModelDefinitionRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUICOMPONENTMODELDEFINITIONREQUEST,
  __module__ = 'page.request.pmp.CreateUIComponentModelDefinitionRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.pmp.CreateUIComponentModelDefinitionRequest)
  ))
_sym_db.RegisterMessage(CreateUIComponentModelDefinitionRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
