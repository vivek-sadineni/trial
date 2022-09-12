# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/GeocodingViewRepsonse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2
from executor.models import multiMediaInfo_pb2 as executor_dot_models_dot_multiMediaInfo__pb2
from executor.models import actionResponse_pb2 as executor_dot_models_dot_actionResponse__pb2
from executor.models import coordinateInfo_pb2 as executor_dot_models_dot_coordinateInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/GeocodingViewRepsonse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n-executor/response/GeocodingViewRepsonse.proto\x12!fkhp.data.layer.executor.response\x1a\x19google/protobuf/any.proto\x1a executor/models/statusInfo.proto\x1a$executor/models/multiMediaInfo.proto\x1a$executor/models/actionResponse.proto\x1a$executor/models/coordinateInfo.proto\"\xb4\x01\n\x15GeocodingViewResponse\x12G\n\x0e\x61\x63tionResponse\x18\x01 \x01(\x0b\x32/.fkhp.data.layer.executor.models.ActionResponse\x12R\n\x0e\x64omainResponse\x18\x02 \x01(\x0b\x32:.fkhp.data.layer.executor.response.GeocodingDomainResponse\"\\\n\x17GeocodingDomainResponse\x12\x41\n\x08location\x18\x01 \x01(\x0b\x32/.fkhp.data.layer.executor.models.CoordinateInfoB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_multiMediaInfo__pb2.DESCRIPTOR,executor_dot_models_dot_actionResponse__pb2.DESCRIPTOR,executor_dot_models_dot_coordinateInfo__pb2.DESCRIPTOR,])




_GEOCODINGVIEWRESPONSE = _descriptor.Descriptor(
  name='GeocodingViewResponse',
  full_name='fkhp.data.layer.executor.response.GeocodingViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actionResponse', full_name='fkhp.data.layer.executor.response.GeocodingViewResponse.actionResponse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domainResponse', full_name='fkhp.data.layer.executor.response.GeocodingViewResponse.domainResponse', index=1,
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
  serialized_start=260,
  serialized_end=440,
)


_GEOCODINGDOMAINRESPONSE = _descriptor.Descriptor(
  name='GeocodingDomainResponse',
  full_name='fkhp.data.layer.executor.response.GeocodingDomainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='fkhp.data.layer.executor.response.GeocodingDomainResponse.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=442,
  serialized_end=534,
)

_GEOCODINGVIEWRESPONSE.fields_by_name['actionResponse'].message_type = executor_dot_models_dot_actionResponse__pb2._ACTIONRESPONSE
_GEOCODINGVIEWRESPONSE.fields_by_name['domainResponse'].message_type = _GEOCODINGDOMAINRESPONSE
_GEOCODINGDOMAINRESPONSE.fields_by_name['location'].message_type = executor_dot_models_dot_coordinateInfo__pb2._COORDINATEINFO
DESCRIPTOR.message_types_by_name['GeocodingViewResponse'] = _GEOCODINGVIEWRESPONSE
DESCRIPTOR.message_types_by_name['GeocodingDomainResponse'] = _GEOCODINGDOMAINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeocodingViewResponse = _reflection.GeneratedProtocolMessageType('GeocodingViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _GEOCODINGVIEWRESPONSE,
  __module__ = 'executor.response.GeocodingViewRepsonse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.GeocodingViewResponse)
  ))
_sym_db.RegisterMessage(GeocodingViewResponse)

GeocodingDomainResponse = _reflection.GeneratedProtocolMessageType('GeocodingDomainResponse', (_message.Message,), dict(
  DESCRIPTOR = _GEOCODINGDOMAINRESPONSE,
  __module__ = 'executor.response.GeocodingViewRepsonse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.GeocodingDomainResponse)
  ))
_sym_db.RegisterMessage(GeocodingDomainResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
