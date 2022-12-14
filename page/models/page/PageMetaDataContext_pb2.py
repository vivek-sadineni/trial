# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/page/PageMetaDataContext.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from page.models.enums import PageType_pb2 as page_dot_models_dot_enums_dot_PageType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/page/PageMetaDataContext.proto',
  package='fkhp.page.layer.models.page',
  syntax='proto3',
  serialized_options=_b('\n\033fkhp.page.layer.models.pageP\001'),
  serialized_pb=_b('\n*page/models/page/PageMetaDataContext.proto\x12\x1b\x66khp.page.layer.models.page\x1a page/models/enums/PageType.proto\"\xc5\x02\n\x13PageMetaDataContext\x12\x10\n\x08pageName\x18\x01 \x01(\t\x12\x11\n\tpageOwner\x18\x02 \x01(\t\x12\x13\n\x0bpageVersion\x18\x03 \x01(\t\x12\x38\n\x08pageType\x18\x04 \x01(\x0e\x32&.fkhp.page.layer.models.enums.PageType\x12v\n\x1brequiredRequestedParameters\x18\x05 \x03(\x0b\x32Q.fkhp.page.layer.models.page.PageMetaDataContext.RequiredRequestedParametersEntry\x1a\x42\n RequiredRequestedParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1f\n\x1b\x66khp.page.layer.models.pageP\x01\x62\x06proto3')
  ,
  dependencies=[page_dot_models_dot_enums_dot_PageType__pb2.DESCRIPTOR,])




_PAGEMETADATACONTEXT_REQUIREDREQUESTEDPARAMETERSENTRY = _descriptor.Descriptor(
  name='RequiredRequestedParametersEntry',
  full_name='fkhp.page.layer.models.page.PageMetaDataContext.RequiredRequestedParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fkhp.page.layer.models.page.PageMetaDataContext.RequiredRequestedParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='fkhp.page.layer.models.page.PageMetaDataContext.RequiredRequestedParametersEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=435,
)

_PAGEMETADATACONTEXT = _descriptor.Descriptor(
  name='PageMetaDataContext',
  full_name='fkhp.page.layer.models.page.PageMetaDataContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageName', full_name='fkhp.page.layer.models.page.PageMetaDataContext.pageName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageOwner', full_name='fkhp.page.layer.models.page.PageMetaDataContext.pageOwner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageVersion', full_name='fkhp.page.layer.models.page.PageMetaDataContext.pageVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageType', full_name='fkhp.page.layer.models.page.PageMetaDataContext.pageType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requiredRequestedParameters', full_name='fkhp.page.layer.models.page.PageMetaDataContext.requiredRequestedParameters', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PAGEMETADATACONTEXT_REQUIREDREQUESTEDPARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=435,
)

_PAGEMETADATACONTEXT_REQUIREDREQUESTEDPARAMETERSENTRY.containing_type = _PAGEMETADATACONTEXT
_PAGEMETADATACONTEXT.fields_by_name['pageType'].enum_type = page_dot_models_dot_enums_dot_PageType__pb2._PAGETYPE
_PAGEMETADATACONTEXT.fields_by_name['requiredRequestedParameters'].message_type = _PAGEMETADATACONTEXT_REQUIREDREQUESTEDPARAMETERSENTRY
DESCRIPTOR.message_types_by_name['PageMetaDataContext'] = _PAGEMETADATACONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageMetaDataContext = _reflection.GeneratedProtocolMessageType('PageMetaDataContext', (_message.Message,), dict(

  RequiredRequestedParametersEntry = _reflection.GeneratedProtocolMessageType('RequiredRequestedParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _PAGEMETADATACONTEXT_REQUIREDREQUESTEDPARAMETERSENTRY,
    __module__ = 'page.models.page.PageMetaDataContext_pb2'
    # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.page.PageMetaDataContext.RequiredRequestedParametersEntry)
    ))
  ,
  DESCRIPTOR = _PAGEMETADATACONTEXT,
  __module__ = 'page.models.page.PageMetaDataContext_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.page.layer.models.page.PageMetaDataContext)
  ))
_sym_db.RegisterMessage(PageMetaDataContext)
_sym_db.RegisterMessage(PageMetaDataContext.RequiredRequestedParametersEntry)


DESCRIPTOR._options = None
_PAGEMETADATACONTEXT_REQUIREDREQUESTEDPARAMETERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
