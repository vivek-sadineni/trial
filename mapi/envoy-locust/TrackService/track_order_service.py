import time
import uuid

import grpc
import sonora
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.TrackService_pb2_grpc import TrackServiceStub
from gateway.requests.TrackOrderRequest_pb2 import TrackOrderRequest
from gateway.responses.TrackOrderResponse_pb2 import TrackOrderResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def get_track_order_request(self, request: TrackOrderRequest) -> TrackOrderResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = TrackServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
            stub.getTrackOrderDetails(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def get_track_order_request(self):
        req_data = TrackOrderRequest(orderId="")
        self.locust_request_handler("get_track_order_request", req_data)


    def locust_request_handler(self, grpc_name, req_data):
        req_func = self._get_request_function(grpc_name)
        start = time.time()
        result = None
        try:
            result = req_func(req_data)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_failure.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0, exception=e)
        else:
            total = int((time.time() - start) * 1000)
            self.user.environment.events.request_success.fire(
                request_type="grpc", name=grpc_name, response_time=total, response_length=0)
        return result

    def _get_request_function(self, grpc_name):
        req_func_map = {
            "get_track_order_request": self.get_track_order_request
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TrackOrder(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
