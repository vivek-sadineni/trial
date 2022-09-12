# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway/clients/OrderService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gateway.requests import CreateOrderRequest_pb2 as gateway_dot_requests_dot_CreateOrderRequest__pb2
from gateway.requests import CancelOrderRequest_pb2 as gateway_dot_requests_dot_CancelOrderRequest__pb2
from gateway.requests import ReturnOrderRequest_pb2 as gateway_dot_requests_dot_ReturnOrderRequest__pb2
from gateway.requests import OrderSuccessRequest_pb2 as gateway_dot_requests_dot_OrderSuccessRequest__pb2
from gateway.requests import OrderDetailRequest_pb2 as gateway_dot_requests_dot_OrderDetailRequest__pb2
from gateway.requests import CancelReasonsRequest_pb2 as gateway_dot_requests_dot_CancelReasonsRequest__pb2
from gateway.requests import ReturnReasonsRequest_pb2 as gateway_dot_requests_dot_ReturnReasonsRequest__pb2
from gateway.requests import ReturnMediumRequest_pb2 as gateway_dot_requests_dot_ReturnMediumRequest__pb2
from gateway.requests import LastOrderDetailRequest_pb2 as gateway_dot_requests_dot_LastOrderDetailRequest__pb2
from gateway.responses import CreateOrderResponse_pb2 as gateway_dot_responses_dot_CreateOrderResponse__pb2
from gateway.responses import CancelOrderResponse_pb2 as gateway_dot_responses_dot_CancelOrderResponse__pb2
from gateway.responses import ReturnOrderResponse_pb2 as gateway_dot_responses_dot_ReturnOrderResponse__pb2
from gateway.responses import OrderSuccessResponse_pb2 as gateway_dot_responses_dot_OrderSuccessResponse__pb2
from gateway.responses import OrderDetailResponse_pb2 as gateway_dot_responses_dot_OrderDetailResponse__pb2
from gateway.responses import CancelReasonsResponse_pb2 as gateway_dot_responses_dot_CancelReasonsResponse__pb2
from gateway.responses import ReturnReasonsResponse_pb2 as gateway_dot_responses_dot_ReturnReasonsResponse__pb2
from gateway.responses import ReturnMediumListResponse_pb2 as gateway_dot_responses_dot_ReturnMediumListResponse__pb2
from gateway.responses import LastOrderDetailResponse_pb2 as gateway_dot_responses_dot_LastOrderDetailResponse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway/clients/OrderService.proto',
  package='fkhp.gateway.layer.client',
  syntax='proto3',
  serialized_options=_b('\n\031fkhp.gateway.layer.clientP\001'),
  serialized_pb=_b('\n\"gateway/clients/OrderService.proto\x12\x19\x66khp.gateway.layer.client\x1a)gateway/requests/CreateOrderRequest.proto\x1a)gateway/requests/CancelOrderRequest.proto\x1a)gateway/requests/ReturnOrderRequest.proto\x1a*gateway/requests/OrderSuccessRequest.proto\x1a)gateway/requests/OrderDetailRequest.proto\x1a+gateway/requests/CancelReasonsRequest.proto\x1a+gateway/requests/ReturnReasonsRequest.proto\x1a*gateway/requests/ReturnMediumRequest.proto\x1a-gateway/requests/LastOrderDetailRequest.proto\x1a+gateway/responses/CreateOrderResponse.proto\x1a+gateway/responses/CancelOrderResponse.proto\x1a+gateway/responses/ReturnOrderResponse.proto\x1a,gateway/responses/OrderSuccessResponse.proto\x1a+gateway/responses/OrderDetailResponse.proto\x1a-gateway/responses/CancelReasonsResponse.proto\x1a-gateway/responses/ReturnReasonsResponse.proto\x1a\x30gateway/responses/ReturnMediumListResponse.proto\x1a/gateway/responses/LastOrderDetailResponse.proto2\xfa\t\n\x0cOrderService\x12\x80\x01\n\x0b\x63reateOrder\x12\x36.fkhp.gateway.layer.client.requests.CreateOrderRequest\x1a\x37.fkhp.gateway.layer.client.response.CreateOrderResponse\"\x00\x12\x80\x01\n\x0b\x63\x61ncelOrder\x12\x36.fkhp.gateway.layer.client.requests.CancelOrderRequest\x1a\x37.fkhp.gateway.layer.client.response.CancelOrderResponse\"\x00\x12\x80\x01\n\x0breturnOrder\x12\x36.fkhp.gateway.layer.client.requests.ReturnOrderRequest\x1a\x37.fkhp.gateway.layer.client.response.ReturnOrderResponse\"\x00\x12\x8a\x01\n\x13getOrderSuccessView\x12\x37.fkhp.gateway.layer.client.requests.OrderSuccessRequest\x1a\x38.fkhp.gateway.layer.client.response.OrderSuccessResponse\"\x00\x12\x83\x01\n\x0egetOrderDetail\x12\x36.fkhp.gateway.layer.client.requests.OrderDetailRequest\x1a\x37.fkhp.gateway.layer.client.response.OrderDetailResponse\"\x00\x12\x94\x01\n\x1bgetOrderCancellationReasons\x12\x38.fkhp.gateway.layer.client.requests.CancelReasonsRequest\x1a\x39.fkhp.gateway.layer.client.response.CancelReasonsResponse\"\x00\x12\x8e\x01\n\x15getReturnOrderReasons\x12\x38.fkhp.gateway.layer.client.requests.ReturnReasonsRequest\x1a\x39.fkhp.gateway.layer.client.response.ReturnReasonsResponse\"\x00\x12\x93\x01\n\x18getReturnOrderMediumList\x12\x37.fkhp.gateway.layer.client.requests.ReturnMediumRequest\x1a<.fkhp.gateway.layer.client.response.ReturnMediumListResponse\"\x00\x12\x8f\x01\n\x12getLastOrderDetail\x12:.fkhp.gateway.layer.client.requests.LastOrderDetailRequest\x1a;.fkhp.gateway.layer.client.response.LastOrderDetailResponse\"\x00\x42\x1d\n\x19\x66khp.gateway.layer.clientP\x01\x62\x06proto3')
  ,
  dependencies=[gateway_dot_requests_dot_CreateOrderRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_CancelOrderRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_ReturnOrderRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_OrderSuccessRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_OrderDetailRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_CancelReasonsRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_ReturnReasonsRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_ReturnMediumRequest__pb2.DESCRIPTOR,gateway_dot_requests_dot_LastOrderDetailRequest__pb2.DESCRIPTOR,gateway_dot_responses_dot_CreateOrderResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_CancelOrderResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_ReturnOrderResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_OrderSuccessResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_OrderDetailResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_CancelReasonsResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_ReturnReasonsResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_ReturnMediumListResponse__pb2.DESCRIPTOR,gateway_dot_responses_dot_LastOrderDetailResponse__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_ORDERSERVICE = _descriptor.ServiceDescriptor(
  name='OrderService',
  full_name='fkhp.gateway.layer.client.OrderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=882,
  serialized_end=2156,
  methods=[
  _descriptor.MethodDescriptor(
    name='createOrder',
    full_name='fkhp.gateway.layer.client.OrderService.createOrder',
    index=0,
    containing_service=None,
    input_type=gateway_dot_requests_dot_CreateOrderRequest__pb2._CREATEORDERREQUEST,
    output_type=gateway_dot_responses_dot_CreateOrderResponse__pb2._CREATEORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='cancelOrder',
    full_name='fkhp.gateway.layer.client.OrderService.cancelOrder',
    index=1,
    containing_service=None,
    input_type=gateway_dot_requests_dot_CancelOrderRequest__pb2._CANCELORDERREQUEST,
    output_type=gateway_dot_responses_dot_CancelOrderResponse__pb2._CANCELORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='returnOrder',
    full_name='fkhp.gateway.layer.client.OrderService.returnOrder',
    index=2,
    containing_service=None,
    input_type=gateway_dot_requests_dot_ReturnOrderRequest__pb2._RETURNORDERREQUEST,
    output_type=gateway_dot_responses_dot_ReturnOrderResponse__pb2._RETURNORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getOrderSuccessView',
    full_name='fkhp.gateway.layer.client.OrderService.getOrderSuccessView',
    index=3,
    containing_service=None,
    input_type=gateway_dot_requests_dot_OrderSuccessRequest__pb2._ORDERSUCCESSREQUEST,
    output_type=gateway_dot_responses_dot_OrderSuccessResponse__pb2._ORDERSUCCESSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getOrderDetail',
    full_name='fkhp.gateway.layer.client.OrderService.getOrderDetail',
    index=4,
    containing_service=None,
    input_type=gateway_dot_requests_dot_OrderDetailRequest__pb2._ORDERDETAILREQUEST,
    output_type=gateway_dot_responses_dot_OrderDetailResponse__pb2._ORDERDETAILRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getOrderCancellationReasons',
    full_name='fkhp.gateway.layer.client.OrderService.getOrderCancellationReasons',
    index=5,
    containing_service=None,
    input_type=gateway_dot_requests_dot_CancelReasonsRequest__pb2._CANCELREASONSREQUEST,
    output_type=gateway_dot_responses_dot_CancelReasonsResponse__pb2._CANCELREASONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getReturnOrderReasons',
    full_name='fkhp.gateway.layer.client.OrderService.getReturnOrderReasons',
    index=6,
    containing_service=None,
    input_type=gateway_dot_requests_dot_ReturnReasonsRequest__pb2._RETURNREASONSREQUEST,
    output_type=gateway_dot_responses_dot_ReturnReasonsResponse__pb2._RETURNREASONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getReturnOrderMediumList',
    full_name='fkhp.gateway.layer.client.OrderService.getReturnOrderMediumList',
    index=7,
    containing_service=None,
    input_type=gateway_dot_requests_dot_ReturnMediumRequest__pb2._RETURNMEDIUMREQUEST,
    output_type=gateway_dot_responses_dot_ReturnMediumListResponse__pb2._RETURNMEDIUMLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='getLastOrderDetail',
    full_name='fkhp.gateway.layer.client.OrderService.getLastOrderDetail',
    index=8,
    containing_service=None,
    input_type=gateway_dot_requests_dot_LastOrderDetailRequest__pb2._LASTORDERDETAILREQUEST,
    output_type=gateway_dot_responses_dot_LastOrderDetailResponse__pb2._LASTORDERDETAILRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERSERVICE)

DESCRIPTOR.services_by_name['OrderService'] = _ORDERSERVICE

# @@protoc_insertion_point(module_scope)