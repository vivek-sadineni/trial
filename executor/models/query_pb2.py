# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/query.proto

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
  name='executor/models/query.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\x1b\x65xecutor/models/query.proto\x12\x1f\x66khp.data.layer.executor.models\"1\n\tQueryMeta\x12\x10\n\x08pageSize\x18\x01 \x01(\x05\x12\x12\n\npageNumber\x18\x02 \x01(\x05\"^\n\tQueryInfo\x12=\n\tqueryType\x18\x01 \x01(\x0e\x32*.fkhp.data.layer.executor.models.QueryType\x12\x12\n\nqueryValue\x18\x02 \x01(\t*\xf5\x02\n\tQueryType\x12\x0f\n\x0bSEARCH_TERM\x10\x00\x12\x0e\n\nOFFER_TYPE\x10\x01\x12\x15\n\x11\x43REATIVE_CATEGORY\x10\x02\x12\x14\n\x10\x43REATIVE_BANNERS\x10\x03\x12\x1b\n\x17\x43REATIVE_SHOP_BY_BRANDS\x10\x04\x12\x1d\n\x19\x43REATIVE_SHOP_BY_CATEGORY\x10\x05\x12\x18\n\x14\x43REATIVE_BANNER_MENU\x10\x06\x12\x14\n\x10SIMILAR_PRODUCTS\x10\x07\x12\x15\n\x11\x43\x41TEGORY_PRODCUTS\x10\x08\x12\x19\n\x15RK_PRODUCTS_HOME_PAGE\x10\t\x12\x0f\n\x0bRK_PRODUCTS\x10\n\x12\x0b\n\x07RK_TAGS\x10\x0b\x12\x0f\n\x0bRK_CATEGORY\x10\x0c\x12\x14\n\x10RELATED_PRODUCTS\x10\r\x12\x14\n\x10\x41RTICLE_CATEGORY\x10\x0e\x12\x14\n\x10\x46\x45\x41TURED_ARTICLE\x10\x0f\x12\x0b\n\x07\x41RTICLE\x10\x10\x42#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
)

_QUERYTYPE = _descriptor.EnumDescriptor(
  name='QueryType',
  full_name='fkhp.data.layer.executor.models.QueryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEARCH_TERM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFER_TYPE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_CATEGORY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_BANNERS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_SHOP_BY_BRANDS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_SHOP_BY_CATEGORY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_BANNER_MENU', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR_PRODUCTS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_PRODCUTS', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RK_PRODUCTS_HOME_PAGE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RK_PRODUCTS', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RK_TAGS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RK_CATEGORY', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELATED_PRODUCTS', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTICLE_CATEGORY', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURED_ARTICLE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTICLE', index=16, number=16,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=212,
  serialized_end=585,
)
_sym_db.RegisterEnumDescriptor(_QUERYTYPE)

QueryType = enum_type_wrapper.EnumTypeWrapper(_QUERYTYPE)
SEARCH_TERM = 0
OFFER_TYPE = 1
CREATIVE_CATEGORY = 2
CREATIVE_BANNERS = 3
CREATIVE_SHOP_BY_BRANDS = 4
CREATIVE_SHOP_BY_CATEGORY = 5
CREATIVE_BANNER_MENU = 6
SIMILAR_PRODUCTS = 7
CATEGORY_PRODCUTS = 8
RK_PRODUCTS_HOME_PAGE = 9
RK_PRODUCTS = 10
RK_TAGS = 11
RK_CATEGORY = 12
RELATED_PRODUCTS = 13
ARTICLE_CATEGORY = 14
FEATURED_ARTICLE = 15
ARTICLE = 16



_QUERYMETA = _descriptor.Descriptor(
  name='QueryMeta',
  full_name='fkhp.data.layer.executor.models.QueryMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='fkhp.data.layer.executor.models.QueryMeta.pageSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageNumber', full_name='fkhp.data.layer.executor.models.QueryMeta.pageNumber', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=113,
)


_QUERYINFO = _descriptor.Descriptor(
  name='QueryInfo',
  full_name='fkhp.data.layer.executor.models.QueryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queryType', full_name='fkhp.data.layer.executor.models.QueryInfo.queryType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryValue', full_name='fkhp.data.layer.executor.models.QueryInfo.queryValue', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=209,
)

_QUERYINFO.fields_by_name['queryType'].enum_type = _QUERYTYPE
DESCRIPTOR.message_types_by_name['QueryMeta'] = _QUERYMETA
DESCRIPTOR.message_types_by_name['QueryInfo'] = _QUERYINFO
DESCRIPTOR.enum_types_by_name['QueryType'] = _QUERYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryMeta = _reflection.GeneratedProtocolMessageType('QueryMeta', (_message.Message,), dict(
  DESCRIPTOR = _QUERYMETA,
  __module__ = 'executor.models.query_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.QueryMeta)
  ))
_sym_db.RegisterMessage(QueryMeta)

QueryInfo = _reflection.GeneratedProtocolMessageType('QueryInfo', (_message.Message,), dict(
  DESCRIPTOR = _QUERYINFO,
  __module__ = 'executor.models.query_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.QueryInfo)
  ))
_sym_db.RegisterMessage(QueryInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)