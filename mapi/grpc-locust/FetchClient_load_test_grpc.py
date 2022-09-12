# -*- coding: utf-8 -*-

"""
This contains to load test of Url-Mapping of gRPC call with locust.
"""

import time

import grpc
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.FetchClient_pb2_grpc import FetchClientStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.models.page.PaginationInfo_pb2 import PaginationInfo
from gateway.models.page.ElementContext_pb2 import ElementContext
from gateway.requests.FetchPageRequest_pb2 import FetchPageRequest
from gateway.responses.FetchResponse_pb2 import FetchResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.interceptors = [MetadataClientInterceptor()]

    def get_fetch_client(self, request: FetchPageRequest) -> FetchResponse:
        stub = FetchClientStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
        stub.fetch(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def get_fetch_client(self):
        req_data = FetchPageRequest(path="/home-page", appInfo=self.get_app_info(),
                                    deviceInfo=self.get_device_info(),
                                    userInfo=self.get_user_info(), request=self.get_request(), fetchPageReactionType=8)
        self.locust_request_handler("get_fetch_client", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="7a010de3d0b7e0762927106327eed042", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="", userType="NEW", loggedIn="LOGGED_IN", org="FKH")

    def get_element_context_info(self):
        return ElementContext(pageId="4", sectionId="", uiComponentId="", uiElementId="")

    def get_pagination_info(self):
        return PaginationInfo(pageNumber=3, pageSize=2, hasMore=True)

    def get_request(self):
        return {
            "userId": "",
            "appVersion": "1",
            "deviceId": "7a010de3d0b7e0762927106327eed042",
            "csrf": "d7ef3d98fbf0431e9818149341b8c5bc"
        }

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
            "get_fetch_client": self.client.get_fetch_client,
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
