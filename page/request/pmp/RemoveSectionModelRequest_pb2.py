# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/pmp/RemoveSectionModelRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/request/pmp/RemoveSectionModelRequest.proto',
  package='fkhp.page.layer.request.pmp',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.request.pmpP\001'),
  serialized_pb=_b('\n0page/request/pmp/RemoveSectionModelRequest.proto\x12\x1b\x66khp.page.layer.request.pmp\">\n\x19RemoveSectionModelRequest\x12\x0e\n\x06pageId\x18\x01 \x01(\t\x12\x11\n\tsectionId\x18\x02 \x01(\tB\x1f\n\x1b\x66khp.page.layer.request.pmpP\x01\x62\x06proto3')
)




_REMOVESECTIONMODELREQUEST = _descriptor.Descriptor(
  name='RemoveSectionModelRequest',
  full_name='fkhp.page.layer.request.pmp.RemoveSectionModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageId', full_name='fkhp.page.layer.request.pmp.RemoveSectionModelRequest.pageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionId', full_name='fkhp.page.layer.request.pmp.RemoveSectionModelRequest.sectionId', index=1,
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
  serialized_start=81,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['RemoveSectionModelRequest'] = _REMOVESECTIONMODELREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveSectionModelRequest = _reflection.GeneratedProtocolMessageType('RemoveSectionModelRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVESECTIONMODELREQUEST,
  __module__ = 'page.request.pmp.RemoveSectionModelRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.pmp.RemoveSectionModelRequest)
  ))
_sym_db.RegisterMessage(RemoveSectionModelRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
