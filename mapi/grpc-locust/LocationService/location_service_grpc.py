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

from gateway.clients.LocationService_pb2_grpc import LocationServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.requests.SetLocationByPincodeRequest_pb2 import SetLocationByPincodeRequest
from gateway.requests.SetCurrentLocationRequest_pb2 import SetCurrentLocationRequest
from gateway.responses.SetLocationByPincodeResponse_pb2 import SetLocationByPincodeResponse
from gateway.responses.SetCurrentLocationResponse_pb2 import SetCurrentLocationResponse


class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.channel = grpc.insecure_channel(self.host)

    def set_location_pincode(self, request: SetLocationByPincodeRequest) -> SetLocationByPincodeResponse:
        stub = LocationServiceStub(self.channel).setLocationByPincode
        resp, call = stub.with_call(request=request)
        print(call)
        print(resp)
        self.channel.close()

    def set_current_location(self, request: SetCurrentLocationRequest) -> SetCurrentLocationResponse:
        stub = LocationServiceStub(self.channel).setCurrentLocation
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
    def set_location_pincode(self):
        req_data = SetLocationByPincodeRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                               pincode="201304")
        self.locust_request_handler("set_location_pincode", req_data)

    @task
    def set_current_location(self):
        req_data = SetCurrentLocationRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                             longitude="", latitude="")
        self.locust_request_handler("set_current_location", req_data)

    def get_app_info(self):
        return AppInfo(appType=2, appVersion="1")

    def get_device_info(self):
        return DeviceInfo(deviceId="11514df1934cf6e6acf178afe1918bce", deviceIP="0.0.0.0")

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
            "set_location_pincode": self.client.set_location_pincode,
            "set_current_location": self.client.set_current_location
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()