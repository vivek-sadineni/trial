# -*- coding: utf-8 -*-

"""
This contains to load test of Url-Mapping of gRPC call with locust.
"""

import time
import uuid

import grpc
import sonora
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.WalletService_pb2_grpc import WalletServiceStub
from gateway.requests.PreWalletInfoRequest_pb2 import PreWalletInfoRequest
from gateway.responses.PreWalletInfoResponse_pb2 import PreWalletInfoResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def pre_wallet_info(self, request: PreWalletInfoRequest) -> PreWalletInfoResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = WalletServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
            stub.preWalletInfo(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def pre_wallet_info(self):
        req_data = PreWalletInfoRequest(mobileNumber="9811371549")
        self.locust_request_handler("pre_wallet_info", req_data)

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
            "pre_wallet_info": self.client.pre_wallet_info
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class PreWalletInfo(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()