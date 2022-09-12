import time

import grpc
import sonora.client

from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.FetchClient_pb2_grpc import FetchClientStub
from gateway.requests.FetchPageRequest_pb2 import FetchPageRequest
from gateway.responses.FetchResponse_pb2 import FetchResponse
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from mapi.MetadataClientInterceptor import MetadataClientInterceptor

header_object = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://fkh.nl-demo.com',
    'Referer': 'https://fkh.nl-demo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/grpc-web+proto',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-client': 'mapi',
    'x-cookie': '_fbp=fb.1.1661241781083.484329401; isPanIndia=Y; cartsynch=0; WHId=10; UserLocationPincode=560103; PanIndiaCityName=Bangalore; userLocation=Karnataka; PanIndiaStateName=Karnataka; PanIndiaStateCode=KA; PanIndiaCityID=20122; LocationSkipped=0; IsLab=0; PanIndiaStateID=16; UIVAL=AwYAdA%3D%3D; cisession_in_com=4d118b7af5cd52f54b60ade9f6523160; GuestUserID=mqob8uq649jh1ittvdhji0lck2; PHPSESSID=mqob8uq649jh1ittvdhji0lck2; moe_uuid=c7bb2d7f-dc2e-4cff-8aee-f367a8bc6d8b; sspl_csrf=dde6e7944df8451fb369c7446b1492ac',
    'x-csrf-test-name': 'dde6e7944df8451fb369c7446b1492ac',
    'x-grpc-web': '1',
    'x-timestamp': '142433',
    'x-user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
}


class FetchClient:

    def fetch(self, request: FetchPageRequest) -> FetchResponse:
        # interceptors = [MetadataClientInterceptor()]
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            # channel = grpc.intercept_channel(channel, *interceptors)
            # print("request for gateway")
            # print(request)
            stub = FetchClientStub(channel).fetch
            resp, call = stub.with_call(request=request, metadata=header_object)
            # print(call)
            # print(resp)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def fetch(self):
        req_data = FetchPageRequest(path="/home-page", appInfo=self.get_app_info(),
                                    deviceInfo=self.get_device_info(),
                                    userInfo=self.get_user_info(), request=self.get_request(), fetchPageReactionType=8)
        self.locust_request_handler("fetch", req_data)

    def get_app_info(self):
        req_data = AppInfo(appVersion="1", appType=2)
        return req_data

    def get_device_info(self):
        return DeviceInfo(deviceId="4d118b7af5cd52f54b60ade9f6523160", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="", userType="New", loggedIn="LOGGED_IN", org="FKH")

    def get_request(self):
        return {
            "userId": "",
            "appVersion": "1",
            "deviceId": "4d118b7af5cd52f54b60ade9f6523160",
            "csrf": "dde6e7944df8451fb369c7446b1492ac"
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
            "fetch": self.client.fetch,
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class FetchPage(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = FetchClient()
