# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gateway.clients import test_pb2 as gateway_dot_clients_dot_test__pb2


class TestServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.test = channel.unary_unary(
        '/fkhp.gateway.layer.test.TestServer/test',
        request_serializer=gateway_dot_clients_dot_test__pb2.TestRequest.SerializeToString,
        response_deserializer=gateway_dot_clients_dot_test__pb2.TestResponse.FromString,
        )


class TestServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def test(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TestServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'test': grpc.unary_unary_rpc_method_handler(
          servicer.test,
          request_deserializer=gateway_dot_clients_dot_test__pb2.TestRequest.FromString,
          response_serializer=gateway_dot_clients_dot_test__pb2.TestResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.gateway.layer.test.TestServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
