# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/UserLocationViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/UserLocationViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n0executor/response/UserLocationViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a\x19google/protobuf/any.proto\"9\n\x18UserLocationViewResponse\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x0f\n\x07pincode\x18\x02 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_USERLOCATIONVIEWRESPONSE = _descriptor.Descriptor(
  name='UserLocationViewResponse',
  full_name='fkhp.data.layer.executor.response.UserLocationViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='fkhp.data.layer.executor.response.UserLocationViewResponse.city', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pincode', full_name='fkhp.data.layer.executor.response.UserLocationViewResponse.pincode', index=1,
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
  serialized_start=114,
  serialized_end=171,
)

DESCRIPTOR.message_types_by_name['UserLocationViewResponse'] = _USERLOCATIONVIEWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserLocationViewResponse = _reflection.GeneratedProtocolMessageType('UserLocationViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERLOCATIONVIEWRESPONSE,
  __module__ = 'executor.response.UserLocationViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.UserLocationViewResponse)
  ))
_sym_db.RegisterMessage(UserLocationViewResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
