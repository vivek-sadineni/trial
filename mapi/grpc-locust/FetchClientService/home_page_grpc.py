import time

import grpc
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.FetchClient_pb2_grpc import FetchClientStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.requests.FetchPageRequest_pb2 import FetchPageRequest
from gateway.responses.FetchResponse_pb2 import FetchResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.interceptors = [MetadataClientInterceptor()]

    def get_fetch_client(self, request: FetchPageRequest) -> FetchResponse:
        stub = FetchClientStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
        resp = stub.fetch(request=request)
        # print(resp)


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
        # print(req_data)
        self.locust_request_handler("get_fetch_client", req_data)

    def get_app_info(self):
        return AppInfo(appType=1, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="c1defbc5b983305d72dd32a3b3137e95", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="ACC1645829", userType="NEW", loggedIn="LOGGED_IN", org="FKH")

    def get_request(self):
        return {
            "userId": "5087245",
            "appVersion": "",
            "deviceId": "c1defbc5b983305d72dd32a3b3137e95",
            "csrf": "9cf44d9773fd4e2999e4a7aca8c03e00"
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
            print("exception:", e)
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


class HomePage(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
