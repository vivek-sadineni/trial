# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/response/pmp/RemoveComponentModelResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/response/pmp/RemoveComponentModelResponse.proto',
  package='fkhp.page.layer.response.pmp',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.response.pmpP\001'),
  serialized_pb=_b('\n4page/response/pmp/RemoveComponentModelResponse.proto\x12\x1c\x66khp.page.layer.response.pmp\".\n\x1cRemoveComponentModelResponse\x12\x0e\n\x06status\x18\x01 \x01(\tB \n\x1c\x66khp.page.layer.response.pmpP\x01\x62\x06proto3')
)




_REMOVECOMPONENTMODELRESPONSE = _descriptor.Descriptor(
  name='RemoveComponentModelResponse',
  full_name='fkhp.page.layer.response.pmp.RemoveComponentModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fkhp.page.layer.response.pmp.RemoveComponentModelResponse.status', index=0,
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
  serialized_start=86,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['RemoveComponentModelResponse'] = _REMOVECOMPONENTMODELRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveComponentModelResponse = _reflection.GeneratedProtocolMessageType('RemoveComponentModelResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVECOMPONENTMODELRESPONSE,
  __module__ = 'page.response.pmp.RemoveComponentModelResponse_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.response.pmp.RemoveComponentModelResponse)
  ))
_sym_db.RegisterMessage(RemoveComponentModelResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)