import time
import uuid

import grpc
import sonora
from locust import task
from locust import User
from locust import TaskSet

from gateway.clients.PrescriptionService_pb2_grpc import PrescriptionServiceStub
from gateway.models.UploadPrescriptionFile_pb2 import UploadPrescriptionFile
from gateway.requests.UploadPrescriptionRequest_pb2 import UploadPrescriptionRequest
from gateway.responses.UploadPrescriptionResponse_pb2 import UploadPrescriptionResponse
from mapi.MetadataClientInterceptor import MetadataClientInterceptor


class TesterClient:

    def upload_prescription(self, request: UploadPrescriptionRequest) -> UploadPrescriptionResponse:
        with sonora.client.insecure_web_channel(
                f"https://fkh.nl-demo.com/"
        ) as channel:
            stub = PrescriptionServiceStub(grpc.intercept_channel(grpc.insecure_channel(self.host), *self.interceptors))
            stub.uploadPrescription(request=request)


class PerfTaskSet(TaskSet):

    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task
    def upload_prescription(self):
        req_data = UploadPrescriptionRequest(files=self.upload_prescription_file())
        self.locust_request_handler("upload_prescription", req_data)

    def upload_prescription_file(self):
        return UploadPrescriptionFile(name="test", data=120)

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
            "upload_prescription": self.client.upload_prescription
        }
        if grpc_name not in req_func_map:
            raise ValueError(f"gRPC name not supported [{grpc_name}]")
        return req_func_map[grpc_name]


class UploadPrescription(User):
    tasks = [PerfTaskSet]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = TesterClient()