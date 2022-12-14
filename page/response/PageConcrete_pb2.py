# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/PageConcrete.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.design import DesignModel_pb2 as page_dot_models_dot_design_dot_DesignModel__pb2
from page.models.section import PageSectionConcrete_pb2 as page_dot_models_dot_section_dot_PageSectionConcrete__pb2
from page.models.page import PageDataContext_pb2 as page_dot_models_dot_page_dot_PageDataContext__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/PageConcrete.proto',
  package='fkhp.page.layer.response',
  syntax='proto3',
  serialized_options=_b('\n\030fkhp.page.layer.responseP\001'),
  serialized_pb=_b('\n page/response/PageConcrete.proto\x12\x18\x66khp.page.layer.response\x1a$page/models/design/DesignModel.proto\x1a-page/models/section/PageSectionConcrete.proto\x1a&page/models/page/PageDataContext.proto\"\xed\x01\n\x0cPageConcrete\x12?\n\x0b\x64\x65signModel\x18\x01 \x01(\x0b\x32*.fkhp.page.layer.models.design.DesignModel\x12\x45\n\x08sections\x18\x02 \x03(\x0b\x32\x33.fkhp.page.layer.models.section.PageSectionConcrete\x12\x0e\n\x06pageId\x18\x03 \x01(\t\x12\x45\n\x0fpageDataContext\x18\x04 \x01(\x0b\x32,.fkhp.page.layer.models.page.PageDataContextB\x1c\n\x18\x66khp.page.layer.responseP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_design_dot_DesignModel__pb2.DESCRIPTOR,page_dot_models_dot_section_dot_PageSectionConcrete__pb2.DESCRIPTOR,page_dot_models_dot_page_dot_PageDataContext__pb2.DESCRIPTOR,])




_PAGECONCRETE = _descriptor.Descriptor(
  name='PageConcrete',
  full_name='fkhp.page.layer.response.PageConcrete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='designModel', full_name='fkhp.page.layer.response.PageConcrete.designModel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sections', full_name='fkhp.page.layer.response.PageConcrete.sections', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageId', full_name='fkhp.page.layer.response.PageConcrete.pageId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageDataContext', full_name='fkhp.page.layer.response.PageConcrete.pageDataContext', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=188,
  serialized_end=425,
)

_PAGECONCRETE.fields_by_name['designModel'].message_type = page_dot_models_dot_design_dot_DesignModel__pb2._DESIGNMODEL
_PAGECONCRETE.fields_by_name['sections'].message_type = page_dot_models_dot_section_dot_PageSectionConcrete__pb2._PAGESECTIONCONCRETE
_PAGECONCRETE.fields_by_name['pageDataContext'].message_type = page_dot_models_dot_page_dot_PageDataContext__pb2._PAGEDATACONTEXT
DESCRIPTOR.message_types_by_name['PageConcrete'] = _PAGECONCRETE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageConcrete = _reflection.GeneratedProtocolMessageType('PageConcrete', (_message.Message,), dict(
  DESCRIPTOR = _PAGECONCRETE,
  __module__ = 'page.response.PageConcrete_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.PageConcrete)
  ))
_sym_db.RegisterMessage(PageConcrete)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
