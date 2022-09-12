# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/enums/ReactionType.proto

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
  name='page/models/enums/ReactionType.proto',
  package='fkhp.page.layer.models.enums',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.models.enumsP\001'),
  serialized_pb=_b('\n$page/models/enums/ReactionType.proto\x12\x1c\x66khp.page.layer.models.enums*\xdf\x04\n\x0cReactionType\x12\x19\n\x15\x44\x45\x46\x41ULT_REACTION_TYPE\x10\x00\x12\r\n\tPOST_DATA\x10\x01\x12\x17\n\x13NAVIGATE_TO_SECTION\x10\x02\x12\t\n\x05POPUP\x10\x03\x12\x19\n\x15NAVIGATE_TO_COMPONENT\x10\x04\x12\x17\n\x13NAVIGATE_TO_GALLERY\x10\x05\x12\x14\n\x10NAVIGATE_TO_FILE\x10\x06\x12\x0f\n\x0b\x43LOSE_POPUP\x10\x07\x12\x14\n\x10NAVIGATE_TO_PAGE\x10\x08\x12\n\n\x06\x45XPAND\x10\t\x12\x15\n\x11\x43OLLAPSE_REACTION\x10\n\x12\x0f\n\x0b\x44\x45LETE_FILE\x10\x0b\x12\x10\n\x0cPREVIEW_FILE\x10\x0c\x12\x0b\n\x07GO_BACK\x10\r\x12\x16\n\x12NAVIGATE_HOME_PAGE\x10\x0e\x12\x15\n\x11\x45LEMENT_LOAD_MORE\x10\x0f\x12\x12\n\x0eSELECT_TO_FORM\x10\x10\x12\x14\n\x10SUBMIT_FORM_DATA\x10\x11\x12\x14\n\x10\x44ISPLAY_TEXT_BOX\x10\x12\x12\x12\n\x0eSUBMIT_TO_FORM\x10\x13\x12\x0e\n\nSHARE_INFO\x10\x14\x12\x10\n\x0cVOICE_SEARCH\x10\x15\x12\x14\n\x10RELOAD_COMPONENT\x10\x16\x12\x11\n\rDOWNLOAD_FILE\x10\x17\x12\x16\n\x12NO_FILTER_REACTION\x10\x18\x12\x1a\n\x16\x46ILTER_BUY_AGAIN_CARDS\x10\x19\x12\x1a\n\x16\x43LIENT_DRIVEN_WORKFLOW\x10\x1a\x12\r\n\tTELEPHONE\x10\x1b\x12\x10\n\x0cREPLACE_PAGE\x10\x1c\x42 \n\x1c\x66khp.page.layer.models.enumsP\x01\x62\x06proto3')
)

_REACTIONTYPE = _descriptor.EnumDescriptor(
  name='ReactionType',
  full_name='fkhp.page.layer.models.enums.ReactionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_REACTION_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST_DATA', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATE_TO_SECTION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POPUP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATE_TO_COMPONENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATE_TO_GALLERY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATE_TO_FILE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE_POPUP', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATE_TO_PAGE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPAND', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLAPSE_REACTION', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_FILE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREVIEW_FILE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GO_BACK', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAVIGATE_HOME_PAGE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_LOAD_MORE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELECT_TO_FORM', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_FORM_DATA', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_TEXT_BOX', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_TO_FORM', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_INFO', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOICE_SEARCH', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELOAD_COMPONENT', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_FILE', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_FILTER_REACTION', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILTER_BUY_AGAIN_CARDS', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_DRIVEN_WORKFLOW', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEPHONE', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLACE_PAGE', index=28, number=28,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=71,
  serialized_end=678,
)
_sym_db.RegisterEnumDescriptor(_REACTIONTYPE)

ReactionType = enum_type_wrapper.EnumTypeWrapper(_REACTIONTYPE)
DEFAULT_REACTION_TYPE = 0
POST_DATA = 1
NAVIGATE_TO_SECTION = 2
POPUP = 3
NAVIGATE_TO_COMPONENT = 4
NAVIGATE_TO_GALLERY = 5
NAVIGATE_TO_FILE = 6
CLOSE_POPUP = 7
NAVIGATE_TO_PAGE = 8
EXPAND = 9
COLLAPSE_REACTION = 10
DELETE_FILE = 11
PREVIEW_FILE = 12
GO_BACK = 13
NAVIGATE_HOME_PAGE = 14
ELEMENT_LOAD_MORE = 15
SELECT_TO_FORM = 16
SUBMIT_FORM_DATA = 17
DISPLAY_TEXT_BOX = 18
SUBMIT_TO_FORM = 19
SHARE_INFO = 20
VOICE_SEARCH = 21
RELOAD_COMPONENT = 22
DOWNLOAD_FILE = 23
NO_FILTER_REACTION = 24
FILTER_BUY_AGAIN_CARDS = 25
CLIENT_DRIVEN_WORKFLOW = 26
TELEPHONE = 27
REPLACE_PAGE = 28


DESCRIPTOR.enum_types_by_name['ReactionType'] = _REACTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)