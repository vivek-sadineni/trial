import time
import uuid

import grpc
import sonora
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.OrderService_pb2_grpc import OrderServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.requests.ReturnOrderRequest_pb2 import ReturnOrderRequest
from gateway.responses.ReturnOrderResponse_pb2 import ReturnOrderResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def return_order(self, request: ReturnOrderRequest) -> ReturnOrderResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = OrderServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
            stub.returnOrder(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def return_order(self):
        req_data = ReturnOrderRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(), orderId="",
                                      invoiceId="", fullOrder="",
                                      name="Prachi", accountNumber="", ifsc="",
                                      salesReturnReasonId="", itemDetails=self.get_return_order_product_info(),
                                      typeOfPayment="", appliedWalletAmount="", isQuickCilver="")
        self.locust_request_handler("return_order", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="ACC1645829", userType="New", loggedIn="LOGGED_IN", org="FKH")

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
            "return_order": self.return_order
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class ReturnOrder(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
