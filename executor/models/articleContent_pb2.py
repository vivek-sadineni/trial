# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/articleContent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import multiMediaInfo_pb2 as executor_dot_models_dot_multiMediaInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/articleContent.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n$executor/models/articleContent.proto\x12\x1f\x66khp.data.layer.executor.models\x1a$executor/models/multiMediaInfo.proto\"\x83\x01\n\x0e\x41rticleContent\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x10shortDescription\x18\x02 \x01(\t\x12H\n\x0b\x64\x65scription\x18\x03 \x03(\x0b\x32\x33.fkhp.data.layer.executor.models.ArticleDescription\"d\n\x12\x41rticleDescription\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t\x12>\n\x05image\x18\x02 \x01(\x0b\x32/.fkhp.data.layer.executor.models.MultiMediaInfoB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_multiMediaInfo__pb2.DESCRIPTOR,])




_ARTICLECONTENT = _descriptor.Descriptor(
  name='ArticleContent',
  full_name='fkhp.data.layer.executor.models.ArticleContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fkhp.data.layer.executor.models.ArticleContent.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shortDescription', full_name='fkhp.data.layer.executor.models.ArticleContent.shortDescription', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='fkhp.data.layer.executor.models.ArticleContent.description', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=112,
  serialized_end=243,
)


_ARTICLEDESCRIPTION = _descriptor.Descriptor(
  name='ArticleDescription',
  full_name='fkhp.data.layer.executor.models.ArticleDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detail', full_name='fkhp.data.layer.executor.models.ArticleDescription.detail', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='fkhp.data.layer.executor.models.ArticleDescription.image', index=1,
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
  serialized_start=245,
  serialized_end=345,
)

_ARTICLECONTENT.fields_by_name['description'].message_type = _ARTICLEDESCRIPTION
_ARTICLEDESCRIPTION.fields_by_name['image'].message_type = executor_dot_models_dot_multiMediaInfo__pb2._MULTIMEDIAINFO
DESCRIPTOR.message_types_by_name['ArticleContent'] = _ARTICLECONTENT
DESCRIPTOR.message_types_by_name['ArticleDescription'] = _ARTICLEDESCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArticleContent = _reflection.GeneratedProtocolMessageType('ArticleContent', (_message.Message,), dict(
  DESCRIPTOR = _ARTICLECONTENT,
  __module__ = 'executor.models.articleContent_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.ArticleContent)
  ))
_sym_db.RegisterMessage(ArticleContent)

ArticleDescription = _reflection.GeneratedProtocolMessageType('ArticleDescription', (_message.Message,), dict(
  DESCRIPTOR = _ARTICLEDESCRIPTION,
  __module__ = 'executor.models.articleContent_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.ArticleDescription)
  ))
_sym_db.RegisterMessage(ArticleDescription)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
