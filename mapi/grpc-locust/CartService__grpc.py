import time
import uuid

import grpc
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.CartService_pb2_grpc import CartServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserInfo_pb2 import UserInfo
from gateway.models.AddToCartItemInfo_pb2 import AddToCartItemInfo
from gateway.requests.AddToBasketRequest_pb2 import AddToBasketRequest
from gateway.requests.AddToCartRequest_pb2 import AddToCartRequest
from gateway.requests.CheckoutRequest_pb2 import CheckoutRequest
from gateway.requests.RemoveFromCartRequest_pb2 import RemoveFromCartRequest
from gateway.requests.RemoveFromBasketRequest_pb2 import RemoveFromBasketRequest
from gateway.requests.ApplyCouponRequest_pb2 import ApplyCouponRequest
from gateway.requests.GetRxProductFromCartRequest_pb2 import GetRxProductFromCartRequest
from gateway.requests.AssignAddressToCartRequest_pb2 import AssignAddressToCartRequest
from gateway.responses.AddToBasketResponse_pb2 import AddToBasketResponse
from gateway.responses.AddToCartResponse_pb2 import AddToCartResponse
from gateway.responses.CheckoutResponse_pb2 import CheckoutResponse
from gateway.responses.RemoveFromBasketResponse_pb2 import RemoveFromBasketResponse
from gateway.responses.RemoveFromCartResponse_pb2 import RemoveFromCartResponse
from gateway.responses.ApplyCouponResponse_pb2 import ApplyCouponResponse
from gateway.responses.AssignAddressToCartResponse_pb2 import AssignAddressToCartResponse
from gateway.responses.GetCartResponse_pb2 import GetCartResponse


class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.channel = grpc.insecure_channel(self.host)

    def add_to_basket(self, request: AddToBasketRequest) -> AddToBasketResponse:
        stub = CartServiceStub(self.channel).addToBasket
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def add_to_cart(self, request: AddToCartRequest) -> AddToCartResponse:
        stub = CartServiceStub(self.channel).addToCart
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def checkout(self, request: CheckoutRequest) -> CheckoutResponse:
        stub = CartServiceStub(self.channel).checkout
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def remove_from_basket(self, request: RemoveFromBasketRequest) -> RemoveFromBasketResponse:
        stub = CartServiceStub(self.channel).removeFromBasket
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def remove_from_cart(self, request: RemoveFromCartRequest) -> RemoveFromCartResponse:
        stub = CartServiceStub(self.channel).removeFromCart
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def apply_coupon(self, request: ApplyCouponRequest) -> ApplyCouponResponse:
        stub = CartServiceStub(self.channel).applyCoupon
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def remove_coupon(self, request: ApplyCouponRequest) -> ApplyCouponResponse:
        stub = CartServiceStub(self.channel).applyCoupon
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def get_rxproducts_from_cart(self, request: GetRxProductFromCartRequest) -> GetCartResponse:
        stub = CartServiceStub(self.channel).getRxProductsFromCart
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def assign_address_to_cart(self, request: AssignAddressToCartRequest) -> AssignAddressToCartResponse:
        stub = CartServiceStub(self.channel).getRxProductsFromCart
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def get_cart(self, request: AddToCartRequest) -> AddToCartResponse:
        stub = CartServiceStub(self.channel).getCart
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def add_to_basket(self):
        req_data = AddToBasketRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                userInfo=self.get_user_info())
        self.locust_request_handler("add_to_basket", req_data)

    @task
    def add_to_cart(self):
        req_data = AddToCartRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                     addToCartItemInfo=self.add_to_cart_item_info(), userInfo=self.get_user_info())
        self.locust_request_handler("add_to_cart", req_data)

    @task
    def checkout(self):
        req_data = CheckoutRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(), userInfo=self.get_user_info())
        self.locust_request_handler("checkout", req_data)

    @task
    def remove_from_basket(self):
        req_data = RemoveFromBasketRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                productId="", userInfo=self.get_user_info())
        self.locust_request_handler("remove_from_basket", req_data)

    @task
    def remove_from_cart(self):
        req_data = RemoveFromCartRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info())
        self.locust_request_handler("remove_from_cart", req_data)

    @task
    def apply_coupon(self):
        req_data = ApplyCouponRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                      userInfo=self.get_user_info(), couponCode="")
        self.locust_request_handler("apply_coupon", req_data)

    @task
    def get_rxproducts_from_cart(self):
        req_data = GetRxProductFromCartRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                               userInfo=self.get_user_info(), userId="")
        self.locust_request_handler("get_rxproducts_from_cart", req_data)

    @task
    def assign_address_to_cart(self):
        req_data = AssignAddressToCartRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info())
        self.locust_request_handler("assign_address_to_cart", req_data)

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
            "add_to_basket": self.client.add_address,
            "add_to_cart": self.client.edit_address,
            "checkout": self.client.remove_address,
            "remove_from_basket": self.client.nearest_area,
            "remove_from_cart": self.client.get_address_book,
            "apply_coupon": self.apply_coupon,
            "get_rxproducts_from_cart": self.get_rxproducts_from_cart,
            "assign_address_to_cart": self.assign_address_to_cart


        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
