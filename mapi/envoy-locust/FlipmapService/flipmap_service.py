import time
import uuid

import grpc
import sonora

from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.FlipMapService_pb2_grpc import FlipMapServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.models.user.UserAddress_pb2 import UserAddress
from gateway.requests.AddressFromLocationPointRequest_pb2 import AddressFromLocationPointRequest
from gateway.requests.AddressSuggestionRequest_pb2 import AddressSuggestionRequest
from gateway.requests.GeocodingRequest_pb2 import GeocodingRequest
from gateway.responses.AddressFromLocationPointResponse_pb2 import AddressFromLocationPointResponse
from gateway.responses.AddressSuggestionResponse_pb2 import AddressSuggestionResponse
from gateway.responses.GeocodingResponse_pb2 import GeocodingResponse


class TesterClient:

    def address_from_location_point(self, request: AddressFromLocationPointRequest) -> AddressFromLocationPointResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = FlipMapServiceStub(self.channel).reverseGeocoding
            resp, call = stub.with_call(request=request)
        # print(call)
        # print(resp)
        self.channel.close()

    def address_suggestion(self, request: AddressSuggestionRequest) -> AddressSuggestionResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = FlipMapServiceStub(self.channel).addressSuggestion
            resp, call = stub.with_call(request=request)
        # print(call)
        # print(resp)
        self.channel.close()

    def geocoding(self, request: GeocodingRequest) -> GeocodingResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = FlipMapServiceStub(self.channel).geocoding
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
    def address_from_location_point(self):
        req_data = AddressFromLocationPointRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                                   userAddress=self.get_user_address(), latitude="", longitude="")
        self.locust_request_handler("address_from_location_point", req_data)

    @task
    def address_suggestion(self):
        req_data = AddressSuggestionRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                            userAddress=self.get_user_address(), text="FKH", type=1, region="", count=3)
        self.locust_request_handler("address_suggestion", req_data)

    @task
    def geocoding(self):
        req_data = GeocodingRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                    userAddress=self.get_user_address(), address="1234, Noida")
        self.locust_request_handler("remove_address", req_data)

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
            "address_from_location_point": self.client.address_from_location_point,
            "address_suggestion": self.client.address_suggestion,
            "geocoding": self.client.geocoding
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()
