# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/request/pmp/RemoveComponentModelRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/request/pmp/RemoveComponentModelRequest.proto',
  package='fkhp.page.layer.request.pmp',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.request.pmpP\001'),
  serialized_pb=_b('\n2page/request/pmp/RemoveComponentModelRequest.proto\x12\x1b\x66khp.page.layer.request.pmp\"\\\n\x1bRemoveComponentModelRequest\x12\x0e\n\x06pageId\x18\x01 \x01(\t\x12\x11\n\tsectionId\x18\x02 \x01(\t\x12\x1a\n\x12sectionComponentId\x18\x03 \x01(\tB\x1f\n\x1b\x66khp.page.layer.request.pmpP\x01\x62\x06proto3')
)




_REMOVECOMPONENTMODELREQUEST = _descriptor.Descriptor(
  name='RemoveComponentModelRequest',
  full_name='fkhp.page.layer.request.pmp.RemoveComponentModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageId', full_name='fkhp.page.layer.request.pmp.RemoveComponentModelRequest.pageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionId', full_name='fkhp.page.layer.request.pmp.RemoveComponentModelRequest.sectionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sectionComponentId', full_name='fkhp.page.layer.request.pmp.RemoveComponentModelRequest.sectionComponentId', index=2,
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
  serialized_start=83,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['RemoveComponentModelRequest'] = _REMOVECOMPONENTMODELREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveComponentModelRequest = _reflection.GeneratedProtocolMessageType('RemoveComponentModelRequest', (_message.Message,), dict(
  DESCRIPTOR = _REMOVECOMPONENTMODELREQUEST,
  __module__ = 'page.request.pmp.RemoveComponentModelRequest_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.request.pmp.RemoveComponentModelRequest)
  ))
_sym_db.RegisterMessage(RemoveComponentModelRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
