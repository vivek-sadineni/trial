# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/element/UIElementAction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.enums import UIElementActionType_pb2 as page_dot_models_dot_enums_dot_UIElementActionType__pb2
from page.models.element import Reaction_pb2 as page_dot_models_dot_element_dot_Reaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/element/UIElementAction.proto',
  package='fkhp.page.layer.models.element',
  syntax='proto3',
  serialized_options=_b('\n\036fkhp.page.layer.models.elementP\001'),
  serialized_pb=_b('\n)page/models/element/UIElementAction.proto\x12\x1e\x66khp.page.layer.models.element\x1a+page/models/enums/UIElementActionType.proto\x1a\"page/models/element/Reaction.proto\"\x94\x01\n\x0fUIElementAction\x12\x45\n\nactionType\x18\x01 \x01(\x0e\x32\x31.fkhp.page.layer.models.enums.UIElementActionType\x12:\n\x08reaction\x18\x02 \x01(\x0b\x32(.fkhp.page.layer.models.element.ReactionB\"\n\x1e\x66khp.page.layer.models.elementP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_enums_dot_UIElementActionType__pb2.DESCRIPTOR,page_dot_models_dot_element_dot_Reaction__pb2.DESCRIPTOR,])




_UIELEMENTACTION = _descriptor.Descriptor(
  name='UIElementAction',
  full_name='fkhp.page.layer.models.element.UIElementAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionType', full_name='fkhp.page.layer.models.element.UIElementAction.actionType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reaction', full_name='fkhp.page.layer.models.element.UIElementAction.reaction', index=1,
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
  serialized_end=307,
)

_UIELEMENTACTION.fields_by_name['actionType'].enum_type = page_dot_models_dot_enums_dot_UIElementActionType__pb2._UIELEMENTACTIONTYPE
_UIELEMENTACTION.fields_by_name['reaction'].message_type = page_dot_models_dot_element_dot_Reaction__pb2._REACTION
DESCRIPTOR.message_types_by_name['UIElementAction'] = _UIELEMENTACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UIElementAction = _reflection.GeneratedProtocolMessageType('UIElementAction', (_message.Message,), dict(
  DESCRIPTOR = _UIELEMENTACTION,
  __module__ = 'page.models.element.UIElementAction_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.element.UIElementAction)
  ))
_sym_db.RegisterMessage(UIElementAction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
