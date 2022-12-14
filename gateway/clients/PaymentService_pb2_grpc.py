# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.requests import PaymentGatewayRequest_pb2 as gateway_dot_requests_dot_PaymentGatewayRequest__pb2
from gateway.requests import PaymentProcessRequest_pb2 as gateway_dot_requests_dot_PaymentProcessRequest__pb2
from gateway.responses import PaymentGatewayResponse_pb2 as gateway_dot_responses_dot_PaymentGatewayResponse__pb2
from gateway.responses import PaymentProcessResponse_pb2 as gateway_dot_responses_dot_PaymentProcessResponse__pb2


class PaymentServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.paymentProcess = channel.unary_unary(
        '/fkhp.gateway.layer.client.PaymentService/paymentProcess',
        request_serializer=gateway_dot_requests_dot_PaymentProcessRequest__pb2.PaymentProcessRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_PaymentProcessResponse__pb2.PaymentProcessResponse.FromString,
        )
    self.paymentGateway = channel.unary_unary(
        '/fkhp.gateway.layer.client.PaymentService/paymentGateway',
        request_serializer=gateway_dot_requests_dot_PaymentGatewayRequest__pb2.PaymentGatewayRequest.SerializeToString,
        response_deserializer=gateway_dot_responses_dot_PaymentGatewayResponse__pb2.PaymentGatewayResponse.FromString,
        )


class PaymentServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def paymentProcess(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def paymentGateway(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PaymentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'paymentProcess': grpc.unary_unary_rpc_method_handler(
          servicer.paymentProcess,
          request_deserializer=gateway_dot_requests_dot_PaymentProcessRequest__pb2.PaymentProcessRequest.FromString,
          response_serializer=gateway_dot_responses_dot_PaymentProcessResponse__pb2.PaymentProcessResponse.SerializeToString,
      ),
      'paymentGateway': grpc.unary_unary_rpc_method_handler(
          servicer.paymentGateway,
          request_deserializer=gateway_dot_requests_dot_PaymentGatewayRequest__pb2.PaymentGatewayRequest.FromString,
          response_serializer=gateway_dot_responses_dot_PaymentGatewayResponse__pb2.PaymentGatewayResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.client.PaymentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
