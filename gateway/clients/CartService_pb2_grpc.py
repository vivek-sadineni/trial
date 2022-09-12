# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.requests import AddToBasketRequest_pb2 as gateway_dot_requests_dot_AddToBasketRequest__pb2
from gateway.requests import AddToCartRequest_pb2 as gateway_dot_requests_dot_AddToCartRequest__pb2
from gateway.requests import ApplyCouponRequest_pb2 as gateway_dot_requests_dot_ApplyCouponRequest__pb2
from gateway.requests import AssignAddressToCartRequest_pb2 as gateway_dot_requests_dot_AssignAddressToCartRequest__pb2
from gateway.requests import CheckoutRequest_pb2 as gateway_dot_requests_dot_CheckoutRequest__pb2
from gateway.requests import GetRxProductFromCartRequest_pb2 as gateway_dot_requests_dot_GetRxProductFromCartRequest__pb2
from gateway.requests import RemoveFromBasketRequest_pb2 as gateway_dot_requests_dot_RemoveFromBasketRequest__pb2
from gateway.requests import RemoveFromCartRequest_pb2 as gateway_dot_requests_dot_RemoveFromCartRequest__pb2
from gateway.responses import AddToBasketResponse_pb2 as gateway_dot_responses_dot_AddToBasketResponse__pb2
from gateway.responses import AddToCartResponse_pb2 as gateway_dot_responses_dot_AddToCartResponse__pb2
from gateway.responses import ApplyCouponResponse_pb2 as gateway_dot_responses_dot_ApplyCouponResponse__pb2
from gateway.responses import AssignAddressToCartResponse_pb2 as gateway_dot_responses_dot_AssignAddressToCartResponse__pb2
from gateway.responses import CheckoutResponse_pb2 as gateway_dot_responses_dot_CheckoutResponse__pb2
from gateway.responses import GetCartResponse_pb2 as gateway_dot_responses_dot_GetCartResponse__pb2
from gateway.responses import RemoveFromBasketResponse_pb2 as gateway_dot_responses_dot_RemoveFromBasketResponse__pb2
from gateway.responses import RemoveFromCartResponse_pb2 as gateway_dot_responses_dot_RemoveFromCartResponse__pb2


class CartServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addToBasket = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/addToBasket',
        request_serializer=gateway_dot_requests_dot_AddToBasketRequest__pb2.AddToBasketRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_AddToBasketResponse__pb2.AddToBasketResponse.FromString,
        )
    self.addToCart = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/addToCart',
        request_serializer=gateway_dot_requests_dot_AddToCartRequest__pb2.AddToCartRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_AddToCartResponse__pb2.AddToCartResponse.FromString,
        )
    self.checkout = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/checkout',
        request_serializer=gateway_dot_requests_dot_CheckoutRequest__pb2.CheckoutRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_CheckoutResponse__pb2.CheckoutResponse.FromString,
        )
    self.removeFromBasket = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/removeFromBasket',
        request_serializer=gateway_dot_requests_dot_RemoveFromBasketRequest__pb2.RemoveFromBasketRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_RemoveFromBasketResponse__pb2.RemoveFromBasketResponse.FromString,
        )
    self.removeFromCart = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/removeFromCart',
        request_serializer=gateway_dot_requests_dot_RemoveFromCartRequest__pb2.RemoveFromCartRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_RemoveFromCartResponse__pb2.RemoveFromCartResponse.FromString,
        )
    self.applyCoupon = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/applyCoupon',
        request_serializer=gateway_dot_requests_dot_ApplyCouponRequest__pb2.ApplyCouponRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_ApplyCouponResponse__pb2.ApplyCouponResponse.FromString,
        )
    self.removeCoupon = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/removeCoupon',
        request_serializer=gateway_dot_requests_dot_ApplyCouponRequest__pb2.ApplyCouponRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_ApplyCouponResponse__pb2.ApplyCouponResponse.FromString,
        )
    self.getRxProductsFromCart = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/getRxProductsFromCart',
        request_serializer=gateway_dot_requests_dot_GetRxProductFromCartRequest__pb2.GetRxProductFromCartRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_GetCartResponse__pb2.GetCartResponse.FromString,
        )
    self.assignAddressToCart = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/assignAddressToCart',
        request_serializer=gateway_dot_requests_dot_AssignAddressToCartRequest__pb2.AssignAddressToCartRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_AssignAddressToCartResponse__pb2.AssignAddressToCartResponse.FromString,
        )
    self.getCart = channel.unary_unary(
        '/fkhp.gateway.layer.client.CartService/getCart',
        request_serializer=gateway_dot_requests_dot_AddToCartRequest__pb2.AddToCartRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_AddToCartResponse__pb2.AddToCartResponse.FromString,
        )


class CartServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addToBasket(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addToCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def checkout(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeFromBasket(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeFromCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def applyCoupon(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeCoupon(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRxProductsFromCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def assignAddressToCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CartServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addToBasket': grpc.unary_unary_rpc_method_handler(
          servicer.addToBasket,
          request_deserializer=gateway_dot_requests_dot_AddToBasketRequest__pb2.AddToBasketRequest.FromString,
          response_serializer=gateway_dot_responses_dot_AddToBasketResponse__pb2.AddToBasketResponse.SerializeToString,
      ),
      'addToCart': grpc.unary_unary_rpc_method_handler(
          servicer.addToCart,
          request_deserializer=gateway_dot_requests_dot_AddToCartRequest__pb2.AddToCartRequest.FromString,
          response_serializer=gateway_dot_responses_dot_AddToCartResponse__pb2.AddToCartResponse.SerializeToString,
      ),
      'checkout': grpc.unary_unary_rpc_method_handler(
          servicer.checkout,
          request_deserializer=gateway_dot_requests_dot_CheckoutRequest__pb2.CheckoutRequest.FromString,
          response_serializer=gateway_dot_responses_dot_CheckoutResponse__pb2.CheckoutResponse.SerializeToString,
      ),
      'removeFromBasket': grpc.unary_unary_rpc_method_handler(
          servicer.removeFromBasket,
          request_deserializer=gateway_dot_requests_dot_RemoveFromBasketRequest__pb2.RemoveFromBasketRequest.FromString,
          response_serializer=gateway_dot_responses_dot_RemoveFromBasketResponse__pb2.RemoveFromBasketResponse.SerializeToString,
      ),
      'removeFromCart': grpc.unary_unary_rpc_method_handler(
          servicer.removeFromCart,
          request_deserializer=gateway_dot_requests_dot_RemoveFromCartRequest__pb2.RemoveFromCartRequest.FromString,
          response_serializer=gateway_dot_responses_dot_RemoveFromCartResponse__pb2.RemoveFromCartResponse.SerializeToString,
      ),
      'applyCoupon': grpc.unary_unary_rpc_method_handler(
          servicer.applyCoupon,
          request_deserializer=gateway_dot_requests_dot_ApplyCouponRequest__pb2.ApplyCouponRequest.FromString,
          response_serializer=gateway_dot_responses_dot_ApplyCouponResponse__pb2.ApplyCouponResponse.SerializeToString,
      ),
      'removeCoupon': grpc.unary_unary_rpc_method_handler(
          servicer.removeCoupon,
          request_deserializer=gateway_dot_requests_dot_ApplyCouponRequest__pb2.ApplyCouponRequest.FromString,
          response_serializer=gateway_dot_responses_dot_ApplyCouponResponse__pb2.ApplyCouponResponse.SerializeToString,
      ),
      'getRxProductsFromCart': grpc.unary_unary_rpc_method_handler(
          servicer.getRxProductsFromCart,
          request_deserializer=gateway_dot_requests_dot_GetRxProductFromCartRequest__pb2.GetRxProductFromCartRequest.FromString,
          response_serializer=gateway_dot_responses_dot_GetCartResponse__pb2.GetCartResponse.SerializeToString,
      ),
      'assignAddressToCart': grpc.unary_unary_rpc_method_handler(
          servicer.assignAddressToCart,
          request_deserializer=gateway_dot_requests_dot_AssignAddressToCartRequest__pb2.AssignAddressToCartRequest.FromString,
          response_serializer=gateway_dot_responses_dot_AssignAddressToCartResponse__pb2.AssignAddressToCartResponse.SerializeToString,
      ),
      'getCart': grpc.unary_unary_rpc_method_handler(
          servicer.getCart,
          request_deserializer=gateway_dot_requests_dot_AddToCartRequest__pb2.AddToCartRequest.FromString,
          response_serializer=gateway_dot_responses_dot_AddToCartResponse__pb2.AddToCartResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.client.CartService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))