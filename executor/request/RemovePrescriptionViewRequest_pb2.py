# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/request/RemovePrescriptionViewRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/request/RemovePrescriptionViewRequest.proto',
  package='fkhp.data.layer.executor.request',
  syntax='proto3',
  serialized_options=_b('\n fkhp.data.layer.executor.requestP\001'),
  serialized_pb=_b('\n4executor/request/RemovePrescriptionViewRequest.proto\x12 fkhp.data.layer.executor.request\"7\n\x1dRemovePrescriptionViewRequest\x12\x16\n\x0eprescriptionId\x18\x01 \x01(\tB$\n fkhp.data.layer.executor.requestP\x01\x62\x06proto3')
)




_REMOVEPRESCRIPTIONVIEWREQUEST = _descriptor.Descriptor(
  name='RemovePrescriptionViewRequest',
  full_name='fkhp.data.layer.executor.request.RemovePrescriptionViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prescriptionId', full_name='fkhp.data.layer.executor.request.RemovePrescriptionViewRequest.prescriptionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=90,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['RemovePrescriptionViewRequest'] = _REMOVEPRESCRIPTIONVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemovePrescriptionViewRequest = _reflection.GeneratedProtocolMessageType('RemovePrescriptionViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEPRESCRIPTIONVIEWREQUEST,
  __module__ = 'executor.request.RemovePrescriptionViewRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.request.RemovePrescriptionViewRequest)
  ))
_sym_db.RegisterMessage(RemovePrescriptionViewRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
