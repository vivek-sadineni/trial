# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/BuyAgainViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from executor.models import listingInfo_pb2 as executor_dot_models_dot_listingInfo__pb2
from executor.models import buyAgainItem_pb2 as executor_dot_models_dot_buyAgainItem__pb2
from executor.models import pageMetaInfo_pb2 as executor_dot_models_dot_pageMetaInfo__pb2
from executor.models import buyAgainInfo_pb2 as executor_dot_models_dot_buyAgainInfo__pb2
from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/BuyAgainViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n,executor/response/BuyAgainViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a\x19google/protobuf/any.proto\x1a!executor/models/listingInfo.proto\x1a\"executor/models/buyAgainItem.proto\x1a\"executor/models/pageMetaInfo.proto\x1a\"executor/models/buyAgainInfo.proto\x1a executor/models/statusInfo.proto\"\xdd\x01\n\x14\x42uyAgainViewResponse\x12\x43\n\x0cpageMetaInfo\x18\x01 \x01(\x0b\x32-.fkhp.data.layer.executor.models.PageMetaInfo\x12?\n\x08listings\x18\x02 \x03(\x0b\x32-.fkhp.data.layer.executor.models.BuyAgainItem\x12?\n\nstatusInfo\x18\x03 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfoB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,executor_dot_models_dot_listingInfo__pb2.DESCRIPTOR,executor_dot_models_dot_buyAgainItem__pb2.DESCRIPTOR,executor_dot_models_dot_pageMetaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_buyAgainInfo__pb2.DESCRIPTOR,executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,])




_BUYAGAINVIEWRESPONSE = _descriptor.Descriptor(
  name='BuyAgainViewResponse',
  full_name='fkhp.data.layer.executor.response.BuyAgainViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageMetaInfo', full_name='fkhp.data.layer.executor.response.BuyAgainViewResponse.pageMetaInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listings', full_name='fkhp.data.layer.executor.response.BuyAgainViewResponse.listings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.BuyAgainViewResponse.statusInfo', index=2,
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
  serialized_start=288,
  serialized_end=509,
)

_BUYAGAINVIEWRESPONSE.fields_by_name['pageMetaInfo'].message_type = executor_dot_models_dot_pageMetaInfo__pb2._PAGEMETAINFO
_BUYAGAINVIEWRESPONSE.fields_by_name['listings'].message_type = executor_dot_models_dot_buyAgainItem__pb2._BUYAGAINITEM
_BUYAGAINVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
DESCRIPTOR.message_types_by_name['BuyAgainViewResponse'] = _BUYAGAINVIEWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuyAgainViewResponse = _reflection.GeneratedProtocolMessageType('BuyAgainViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUYAGAINVIEWRESPONSE,
  __module__ = 'executor.response.BuyAgainViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.BuyAgainViewResponse)
  ))
_sym_db.RegisterMessage(BuyAgainViewResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)