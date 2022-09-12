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

from gateway.clients.AddressService_pb2_grpc import AddressServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserAddress_pb2 import UserAddress
from gateway.requests.AddAddressRequest_pb2 import AddAddressRequest
from gateway.requests.EditAddressRequest_pb2 import EditAddressRequest
from gateway.requests.RemoveAddressRequest_pb2 import RemoveAddressRequest
from gateway.requests.NearestAreaRequest_pb2 import NearestAreaRequest
from gateway.requests.AddressBookRequest_pb2 import AddressBookRequest
from gateway.responses.AddAddressResponse_pb2 import AddAddressResponse
from gateway.responses.EditAddressResponse_pb2 import EditAddressResponse
from gateway.responses.RemoveAddressResponse_pb2 import RemoveAddressResponse
from gateway.responses.NearestAreaResponse_pb2 import NearestAreaResponse
from gateway.responses.AddressBookResponse_pb2 import AddressBookResponse




class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.channel = grpc.insecure_channel(self.host)

    def add_address(self, request: AddAddressRequest) -> AddAddressResponse:
        stub = AddressServiceStub(self.channel).addAddress
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def edit_address(self, request: EditAddressRequest) -> EditAddressResponse:
        stub = AddressServiceStub(self.channel).editAddress
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def remove_address(self, request: RemoveAddressRequest) -> RemoveAddressResponse:
        stub = AddressServiceStub(self.channel).removeAddress
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def nearest_area(self, request: NearestAreaRequest) -> NearestAreaResponse:
        stub = AddressServiceStub(self.channel).NearestArea
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def get_address_book(self, request: AddressBookRequest) -> AddressBookResponse:
        stub = AddressServiceStub(self.channel).getAddressBook
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
    def add_address(self):
        req_data = AddAddressRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                userAddress=self.get_user_address())
        self.locust_request_handler("add_address", req_data)

    @task
    def edit_address(self):
        req_data = EditAddressRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                     userAddress=self.get_user_address())
        self.locust_request_handler("edit_address", req_data)

    @task
    def remove_address(self):
        req_data = RemoveAddressRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(), addressId="1")
        self.locust_request_handler("remove_address", req_data)

    @task
    def nearest_area(self):
        req_data = NearestAreaRequest(pincode="201304")
        self.locust_request_handler("nearest_area", req_data)

    @task
    def get_address_book(self):
        req_data = AddressBookRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info())
        self.locust_request_handler("get_address_book", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")

    def get_user_address(self):
        return UserAddress(name="Prachi", mobileNumber="9354297301", address="114,Duplex, Swarnim Vihar",
                           landmark="", pinCode="201304", city="Noida", area="Sector-82", addressType=0)

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
            "add_address": self.client.add_address,
            "edit_address": self.client.edit_address,
            "remove_address": self.client.remove_address,
            "nearest_area": self.client.nearest_area,
            "get_address_book": self.client.get_address_book
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
