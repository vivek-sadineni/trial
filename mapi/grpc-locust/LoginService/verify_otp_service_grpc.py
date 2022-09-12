import time
import uuid

import grpc
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.LoginService_pb2_grpc import LoginServiceStub
from gateway.models.app.AppInfo_pb2 import AppInfo
from gateway.models.device.DeviceInfo_pb2 import DeviceInfo
from gateway.requests.RegenerateOtpRequest_pb2 import RegenerateOtpRequest
from gateway.requests.VerifyOtpRequest_pb2 import VerifyOtpRequest
from gateway.requests.ChangePasswordRequest_pb2 import ChangePasswordRequest
from gateway.responses.RegenerateOtpResponse_pb2 import RegenerateOtpResponse
from gateway.responses.VerifyOtpResponse_pb2 import VerifyOtpResponse
from gateway.responses.ChangePasswordResponse_pb2 import ChangePasswordResponse


class TesterClient:

    def __init__(self):
        self.host = "34.100.234.141:80"
        self.channel = grpc.insecure_channel(self.host)

    def verify_otp(self, request: VerifyOtpRequest) -> VerifyOtpResponse:
        stub = LoginServiceStub(self.channel).verifyOtp
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
    def verify_otp(self):
        req_data = VerifyOtpRequest(appInfo=self.get_app_info(), deviceInfo=self.get_device_info(),
                                    otp="334567", mobileNumber="9354297301")
        self.locust_request_handler("verify_otp", req_data)

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
            "verify_otp": self.client.verify_otp
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class TesterUser(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()