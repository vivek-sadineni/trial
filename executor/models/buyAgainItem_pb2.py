# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor/models/buyAgainItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from executor.models import listingInfo_pb2 as executor_dot_models_dot_listingInfo__pb2
from executor.models import productInfo_pb2 as executor_dot_models_dot_productInfo__pb2
from executor.models import buyAgainInfo_pb2 as executor_dot_models_dot_buyAgainInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executor/models/buyAgainItem.proto',
  package='fkhp.data.layer.executor.models',
  syntax='proto3',
  serialized_options=_b('\n\037fkhp.data.layer.executor.modelsP\001'),
  serialized_pb=_b('\n\"executor/models/buyAgainItem.proto\x12\x1f\x66khp.data.layer.executor.models\x1a!executor/models/listingInfo.proto\x1a!executor/models/productInfo.proto\x1a\"executor/models/buyAgainInfo.proto\"\xd9\x01\n\x0c\x42uyAgainItem\x12\x41\n\x0blistingInfo\x18\x01 \x01(\x0b\x32,.fkhp.data.layer.executor.models.ListingInfo\x12\x41\n\x0bproductInfo\x18\x02 \x01(\x0b\x32,.fkhp.data.layer.executor.models.ProductInfo\x12\x43\n\x0c\x62uyAgainInfo\x18\x03 \x01(\x0b\x32-.fkhp.data.layer.executor.models.BuyAgainInfoB#\n\x1f\x66khp.data.layer.executor.modelsP\x01\x62\x06proto3')
  ,
  dependencies=[executor_dot_models_dot_listingInfo__pb2.DESCRIPTOR,executor_dot_models_dot_productInfo__pb2.DESCRIPTOR,executor_dot_models_dot_buyAgainInfo__pb2.DESCRIPTOR,])




_BUYAGAINITEM = _descriptor.Descriptor(
  name='BuyAgainItem',
  full_name='fkhp.data.layer.executor.models.BuyAgainItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='listingInfo', full_name='fkhp.data.layer.executor.models.BuyAgainItem.listingInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productInfo', full_name='fkhp.data.layer.executor.models.BuyAgainItem.productInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyAgainInfo', full_name='fkhp.data.layer.executor.models.BuyAgainItem.buyAgainInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=178,
  serialized_end=395,
)

_BUYAGAINITEM.fields_by_name['listingInfo'].message_type = executor_dot_models_dot_listingInfo__pb2._LISTINGINFO
_BUYAGAINITEM.fields_by_name['productInfo'].message_type = executor_dot_models_dot_productInfo__pb2._PRODUCTINFO
_BUYAGAINITEM.fields_by_name['buyAgainInfo'].message_type = executor_dot_models_dot_buyAgainInfo__pb2._BUYAGAININFO
DESCRIPTOR.message_types_by_name['BuyAgainItem'] = _BUYAGAINITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuyAgainItem = _reflection.GeneratedProtocolMessageType('BuyAgainItem', (_message.Message,), dict(
  DESCRIPTOR = _BUYAGAINITEM,
  __module__ = 'executor.models.buyAgainItem_pb2'
  # @@protoc_insertion_point(class_scope:fkhp.data.layer.executor.models.BuyAgainItem)
  ))
_sym_db.RegisterMessage(BuyAgainItem)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
