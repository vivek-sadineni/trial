# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/pmp/SearchPageMetaDataByFilterResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.page.pmp import PageMetaData_pb2 as page_dot_models_dot_page_dot_pmp_dot_PageMetaData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/pmp/SearchPageMetaDataByFilterResponse.proto',
  package='fkhp.page.layer.response.pmp',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.response.pmpP\001'),
  serialized_pb=_b('\n:page/response/pmp/SearchPageMetaDataByFilterResponse.proto\x12\x1c\x66khp.page.layer.response.pmp\x1a\'page/models/page/pmp/PageMetaData.proto\"\x87\x01\n\"SearchPageMetaDataByFilterResponse\x12\x18\n\x10searchResultSize\x18\x01 \x01(\t\x12G\n\x10pageMetaDataList\x18\x02 \x03(\x0b\x32-.fkhp.page.layer.models.page.pmp.PageMetaDataB \n\x1c\x66khp.page.layer.response.pmpP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_page_dot_pmp_dot_PageMetaData__pb2.DESCRIPTOR,])




_SEARCHPAGEMETADATABYFILTERRESPONSE = _descriptor.Descriptor(
  name='SearchPageMetaDataByFilterResponse',
  full_name='fkhp.page.layer.response.pmp.SearchPageMetaDataByFilterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='searchResultSize', full_name='fkhp.page.layer.response.pmp.SearchPageMetaDataByFilterResponse.searchResultSize', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageMetaDataList', full_name='fkhp.page.layer.response.pmp.SearchPageMetaDataByFilterResponse.pageMetaDataList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=134,
  serialized_end=269,
)

_SEARCHPAGEMETADATABYFILTERRESPONSE.fields_by_name['pageMetaDataList'].message_type = page_dot_models_dot_page_dot_pmp_dot_PageMetaData__pb2._PAGEMETADATA
DESCRIPTOR.message_types_by_name['SearchPageMetaDataByFilterResponse'] = _SEARCHPAGEMETADATABYFILTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchPageMetaDataByFilterResponse = _reflection.GeneratedProtocolMessageType('SearchPageMetaDataByFilterResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPAGEMETADATABYFILTERRESPONSE,
  __module__ = 'page.response.pmp.SearchPageMetaDataByFilterResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.pmp.SearchPageMetaDataByFilterResponse)
  ))
_sym_db.RegisterMessage(SearchPageMetaDataByFilterResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
