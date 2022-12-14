# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/requests/AssignPrescriptionToCartRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/requests/AssignPrescriptionToCartRequest.proto',
  package='fkhp.gateway.layer.client.requests',
  syntax='proto3',
  serialized_options=_b('\n\"fkhp.gateway.layer.client.requestsP\001'),
  serialized_pb=_b('\n6gateway/requests/AssignPrescriptionToCartRequest.proto\x12\"fkhp.gateway.layer.client.requests\"z\n\x1f\x41ssignPrescriptionToCartRequest\x12\x17\n\x0fprescriptionIds\x18\x01 \x03(\t\x12\x1d\n\x15prescriptionFileNames\x18\x02 \x03(\t\x12\x1f\n\x17isPrescriptionAvailable\x18\x03 \x01(\x08\x42&\n\"fkhp.gateway.layer.client.requestsP\x01\x62\x06proto3')
)




_ASSIGNPRESCRIPTIONTOCARTREQUEST = _descriptor.Descriptor(
  name='AssignPrescriptionToCartRequest',
  full_name='fkhp.gateway.layer.client.requests.AssignPrescriptionToCartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prescriptionIds', full_name='fkhp.gateway.layer.client.requests.AssignPrescriptionToCartRequest.prescriptionIds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prescriptionFileNames', full_name='fkhp.gateway.layer.client.requests.AssignPrescriptionToCartRequest.prescriptionFileNames', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isPrescriptionAvailable', full_name='fkhp.gateway.layer.client.requests.AssignPrescriptionToCartRequest.isPrescriptionAvailable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=94,
  serialized_end=216,
)

DESCRIPTOR.message_types_by_name['AssignPrescriptionToCartRequest'] = _ASSIGNPRESCRIPTIONTOCARTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssignPrescriptionToCartRequest = _reflection.GeneratedProtocolMessageType('AssignPrescriptionToCartRequest', (_message.Message,), dict(
  DESCRIPTOR = _ASSIGNPRESCRIPTIONTOCARTREQUEST,
  __module__ = 'gateway.requests.AssignPrescriptionToCartRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.gateway.layer.client.requests.AssignPrescriptionToCartRequest)
  ))
_sym_db.RegisterMessage(AssignPrescriptionToCartRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
