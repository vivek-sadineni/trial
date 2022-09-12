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

from gateway.clients.PaymentService_pb2_grpc import PaymentServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.requests.PaymentGatewayRequest_pb2 import PaymentGatewayRequest
from gateway.responses.PaymentGatewayResponse_pb2 import PaymentGatewayResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor

class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.interceptors = [MetadataClientInterceptor()]

    def payment_gateway(self, request: PaymentGatewayRequest) -> PaymentGatewayResponse:
        stub = PaymentServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
        stub.paymentGateway(request=request)

class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def payment_gateway(self):
        req_data = PaymentGatewayRequest(deviceInfo=self.get_device_info(), appInfo=self.get_app_info(),
                                         userInfo=self.get_user_info())
        self.locust_request_handler("payment_gateway", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="", userType="New", loggedIn="LOGGED_IN", org="FKH")

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
            "payment_gateway": self.client.payment_gateway
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
