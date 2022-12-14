# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/BuyAgainViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import query_pb2 as executor_dot_models_dot_query__pb2
from executor.models import requestMetaInfo_pb2 as executor_dot_models_dot_requestMetaInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/BuyAgainViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n*executor/request/BuyAgainViewRequest.proto\x12 fkhp.data.layer.executor.request\x1a\x1b\x65xecutor/models/query.proto\x1a%executor/models/requestMetaInfo.proto\"\xb2\x01\n\x13\x42uyAgainViewRequest\x12\x11\n\torderType\x18\x01 \x01(\t\x12=\n\tqueryMeta\x18\x02 \x01(\x0b\x32*.fkhp.data.layer.executor.models.QueryMeta\x12I\n\x0frequestMetaInfo\x18\x03 \x01(\x0b\x32\x30.fkhp.data.layer.executor.models.RequestMetaInfoB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_query__pb2.DESCRIPTOR,executor_dot_models_dot_requestMetaInfo__pb2.DESCRIPTOR,])




_BUYAGAINVIEWREQUEST = _descriptor.Descriptor(
  name='BuyAgainViewRequest',
  full_name='fkhp.data.layer.executor.request.BuyAgainViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderType', full_name='fkhp.data.layer.executor.request.BuyAgainViewRequest.orderType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryMeta', full_name='fkhp.data.layer.executor.request.BuyAgainViewRequest.queryMeta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestMetaInfo', full_name='fkhp.data.layer.executor.request.BuyAgainViewRequest.requestMetaInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=149,
  serialized_end=327,
)

_BUYAGAINVIEWREQUEST.fields_by_name['queryMeta'].message_type = executor_dot_models_dot_query__pb2._QUERYMETA
_BUYAGAINVIEWREQUEST.fields_by_name['requestMetaInfo'].message_type = executor_dot_models_dot_requestMetaInfo__pb2._REQUESTMETAINFO
DESCRIPTOR.message_types_by_name['BuyAgainViewRequest'] = _BUYAGAINVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuyAgainViewRequest = _reflection.GeneratedProtocolMessageType('BuyAgainViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _BUYAGAINVIEWREQUEST,
  __module__ = 'executor.request.BuyAgainViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.BuyAgainViewRequest)
  ))
_sym_db.RegisterMessage(BuyAgainViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
