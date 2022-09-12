# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/response/PhonePeProcessViewResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import statusInfo_pb2 as executor_dot_models_dot_statusInfo__pb2
from executor.models import pgInfo_pb2 as executor_dot_models_dot_pgInfo__pb2
from executor.models import bankInfo_pb2 as executor_dot_models_dot_bankInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/response/PhonePeProcessViewResponse.proto',
  package='fkhp.data.layer.executor.response',
  syntax='proto3',
  serialized_options=_b('\n!fkhp.data.layer.executor.responseP\001'),
  serialized_pb=_b('\n2executor/response/PhonePeProcessViewResponse.proto\x12!fkhp.data.layer.executor.response\x1a executor/models/statusInfo.proto\x1a\x1c\x65xecutor/models/pgInfo.proto\x1a\x1e\x65xecutor/models/bankInfo.proto\"\x87\x01\n\x1aPhonePeProcessViewResponse\x12?\n\nstatusInfo\x18\x01 \x01(\x0b\x32+.fkhp.data.layer.executor.models.StatusInfo\x12\x11\n\tactionUrl\x18\x02 \x01(\t\x12\x15\n\rtransactionId\x18\x03 \x01(\tB%\n!fkhp.data.layer.executor.responseP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_statusInfo__pb2.DESCRIPTOR,executor_dot_models_dot_pgInfo__pb2.DESCRIPTOR,executor_dot_models_dot_bankInfo__pb2.DESCRIPTOR,])




_PHONEPEPROCESSVIEWRESPONSE = _descriptor.Descriptor(
  name='PhonePeProcessViewResponse',
  full_name='fkhp.data.layer.executor.response.PhonePeProcessViewResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusInfo', full_name='fkhp.data.layer.executor.response.PhonePeProcessViewResponse.statusInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actionUrl', full_name='fkhp.data.layer.executor.response.PhonePeProcessViewResponse.actionUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transactionId', full_name='fkhp.data.layer.executor.response.PhonePeProcessViewResponse.transactionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=186,
  serialized_end=321,
)

_PHONEPEPROCESSVIEWRESPONSE.fields_by_name['statusInfo'].message_type = executor_dot_models_dot_statusInfo__pb2._STATUSINFO
DESCRIPTOR.message_types_by_name['PhonePeProcessViewResponse'] = _PHONEPEPROCESSVIEWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PhonePeProcessViewResponse = _reflection.GeneratedProtocolMessageType('PhonePeProcessViewResponse', (_message.Message,), dict(
  DESCRIPTOR = _PHONEPEPROCESSVIEWRESPONSE,
  __module__ = 'executor.response.PhonePeProcessViewResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.response.PhonePeProcessViewResponse)
  ))
_sym_db.RegisterMessage(PhonePeProcessViewResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
