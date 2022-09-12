import time
import uuid

import grpc
import sonora

from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.CartService_pb2_grpc import CartServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.models.AddToCartItemInfo_pb2 import AddToCartItemInfo
from gateway.requests.AddToCartRequest_pb2 import AddToCartRequest
from gateway.responses.AddToCartResponse_pb2 import AddToCartResponse


class TesterClient:

    def add_to_cart(self, request: AddToCartRequest) -> AddToCartResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = CartServiceStub(self.channel).addToCart
            resp, call = stub.with_call(request=request)
        # print(call)
        # print(resp)
        self.channel.close()


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def add_to_cart(self):
        req_data = AddToCartRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                    addToCartItemInfo=self.add_to_cart_item_info(), userInfo=self.get_user_info())
        self.locust_request_handler("add_to_cart", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")

    def get_user_info(self):
        return UserInfo(accountId="", userType="New", loggedIn="LOGGED_IN", org="FKH")

    def add_to_cart_item_info(self):
        return AddToCartItemInfo(productId="", quantity=1, referenceOrderId="", productType=1)

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
            "add_to_cart": self.client.add_to_cart
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class AddToCart(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
