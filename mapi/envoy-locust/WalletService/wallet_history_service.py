import time
import uuid

import grpc
import sonora
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.WalletService_pb2_grpc import WalletServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.models.page.PaginationInfo_pb2 import PaginationInfo
from gateway.requests.WalletHistoryRequest_pb2 import WalletHistoryRequest
from gateway.responses.WalletHistoryResponse_pb2 import WalletHistoryResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def wallet_history(self, request: WalletHistoryRequest) -> WalletHistoryResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = WalletServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
            stub.getWalletHistory(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def wallet_history(self):
        req_data = WalletHistoryRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                        userInfo=self.get_user_info(), paginationInfo=self.get_pagination_info())
        self.locust_request_handler("wallet_history", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="", userType="NEW", loggedIn="LOGGED_IN", org="FKH")

    def get_pagination_info(self):
        return PaginationInfo(pageNumber=3, pageSize=2, hasMore=True)
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
            "wallet_history": self.client.wallet_history
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class WalletHistory(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()