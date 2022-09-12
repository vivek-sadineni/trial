# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/CreativeViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import query_pb2 as executor_dot_models_dot_query__pb2
from executor.models import filter_pb2 as executor_dot_models_dot_filter__pb2
from executor.models import requestMetaInfo_pb2 as executor_dot_models_dot_requestMetaInfo__pb2
from executor.models import userInfo_pb2 as executor_dot_models_dot_userInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/CreativeViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n*executor/request/CreativeViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a\x1b\x65xecutor/models/query.proto\x1a\x1c\x65xecutor/models/filter.proto\x1a%executor/models/requestMetaInfo.proto\x1a\x1e\x65xecutor/models/userInfo.proto\"\xd8\x02\n\x13\x43reativeViewRequest\x12=\n\tqueryMeta\x18\x01 \x01(\x0b\x32*.fkhp.data.layer.executor.models.QueryMeta\x12\x39\n\x05query\x18\x03 \x01(\x0b\x32*.fkhp.data.layer.executor.models.QueryInfo\x12?\n\nfilterInfo\x18\x04 \x01(\x0b\x32+.fkhp.data.layer.executor.models.FilterInfo\x12I\n\x0frequestMetaInfo\x18\x05 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfo\x12;\n\x08userInfo\x18\x06 \x01(\x0b\x32).fkhp.data.layer.executor.models.UserInfoB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_query__pb2.DESCRIPTOR,executor_dot_models_dot_filter__pb2.DESCRIPTOR,executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_userInfo__pb2.DESCRIPTOR,])




_CREATIVEVIEWREQUEST = _descriptor.Descriptor(
  name='CreativeViewRequest',
  full_name='fkhp.data.layer.executor.request.CreativeViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queryMeta', full_name='fkhp.data.layer.executor.request.CreativeViewRequest.queryMeta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='fkhp.data.layer.executor.request.CreativeViewRequest.query', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterInfo', full_name='fkhp.data.layer.executor.request.CreativeViewRequest.filterInfo', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.CreativeViewRequest.requestMetaInfo', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='fkhp.data.layer.executor.request.CreativeViewRequest.userInfo', index=4,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=211,
  serialized_end=555,
)

_CREATIVEVIEWREQUEST.fields_by_name['queryMeta'].message_type = executor_dot_models_dot_query__pb2._QUERYMETA
_CREATIVEVIEWREQUEST.fields_by_name['query'].message_type = executor_dot_models_dot_query__pb2._QUERYINFO
_CREATIVEVIEWREQUEST.fields_by_name['filterInfo'].message_type = executor_dot_models_dot_filter__pb2._FILTERINFO
_CREATIVEVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
_CREATIVEVIEWREQUEST.fields_by_name['userInfo'].message_type = executor_dot_models_dot_userInfo__pb2._USERINFO
DESCRIPTOR.message_types_by_name['CreativeViewRequest'] = _CREATIVEVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreativeViewRequest = _reflection.GeneratedProtocolMessageType('CreativeViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATIVEVIEWREQUEST,
  __module__ = 'executor.request.CreativeViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.CreativeViewRequest)
  ))
_sym_db.RegisterMessage(CreativeViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
