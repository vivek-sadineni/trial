import csv
import random
import warnings
import os
from requests.auth import HTTPDigestAuth
from locust import HttpUser, task, between

URI = "/index.php/orders/order/getOrderOTCMedItems?HBId=191626&calltype=N&rawFlg=1&UserID=418637&UpdatedBy=191626&WarehouseId=1"


class SastaSundarSearch(HttpUser):
    host = os.getenv('TARGET_URL', 'https://temp-preprod.customerapi.sastasundar.com')

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def cust_api_call(self):
        self.client.get(URI, auth=HTTPDigestAuth('admin', '1234'))
        # print(response.text)
