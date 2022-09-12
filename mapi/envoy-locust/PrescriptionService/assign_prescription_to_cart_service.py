import time
import uuid

import grpc
import sonora
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.PrescriptionService_pb2_grpc import PrescriptionServiceStub
from gateway.requests.AssignPrescriptionToCartRequest_pb2 import AssignPrescriptionToCartRequest
from gateway.responses.AssignPrescriptionToCartResponse_pb2 import AssignPrescriptionToCartResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def assign_prescription(self, request: AssignPrescriptionToCartRequest) -> AssignPrescriptionToCartResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = PrescriptionServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
            stub.assignPrescriptionToCart(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def assign_prescription(self):
        req_data = AssignPrescriptionToCartRequest(prescriptionId="1234", prescriptionFileNames="Test",
                                                   isPrescriptionAvailable=True)
        self.locust_request_handler("assign_prescription", req_data)


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
            "assign_prescription": self.client.assign_prescription
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class AssignPrescriptionToCart(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()