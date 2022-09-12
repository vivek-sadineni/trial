# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from page.request import FetchRequest_pb2 as page_dot_request_dot_FetchRequest__pb2
from page.response import FetchPageResponse_pb2 as page_dot_response_dot_FetchPageResponse__pb2


class PageServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.fetchPage = channel.unary_unary(
        '/fkhp.page.layer.client.PageService/fetchPage',
        request_serializer=page_dot_request_dot_FetchRequest__pb2.FetchRequest.SerializeToString,
        response_deserializer=page_dot_response_dot_FetchPageResponse__pb2.FetchPageResponse.FromString,
        )


class PageServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def fetchPage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'fetchPage': grpc.unary_unary_rpc_method_handler(
          servicer.fetchPage,
          request_deserializer=page_dot_request_dot_FetchRequest__pb2.FetchRequest.FromString,
          response_serializer=page_dot_response_dot_FetchPageResponse__pb2.FetchPageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fkhp.page.layer.client.PageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))