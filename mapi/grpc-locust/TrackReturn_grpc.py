# -*- coding: utf-8 -*-

"""
This contains to load test of Url-Mapping of gRPC call with locust.
"""

import time
import uuid

import grpc
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.TrackService_pb2_grpc import TrackServiceStub
from gateway.requests.TrackReturnRequest_pb2 import TrackReturnRequest
from gateway.responses.TrackReturnResponse_pb2 import TrackReturnResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor

class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.interceptors = [MetadataClientInterceptor()]

    def get_track_return_request(self, request: TrackReturnRequest) -> TrackReturnRequest:
        stub = TrackServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
        stub.getTrackReturnDetails(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def get_track_return_request(self):
        req_data = TrackReturnRequest(orderId="", productId="")
        self.locust_request_handler("get_track_return_request", req_data)


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
            "get_track_return_request": self.get_track_return_request
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
