import csv
import random
import warnings
import os
from requests.auth import HTTPDigestAuth
from locust import HttpUser, task, between

URI = "/index.php/orders/order/getOrderOTCMedItems?HBId=191626&calltype=N&rawFlg=1&UserID=418637&UpdatedBy=191626&WarehouseId=1"


class SastaSundarSearch(HttpUser):
    host = os.getenv('TARGET_URL', 'https://temp-preprod-win.customerapi.sastasundar.com')

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def cust_api_call(self):
        response = self.client.get(URI, auth=HTTPDigestAuth('jkH67#grA^$U_23JN', 'jhgt7r7R^&B4r&%$RG75'))
        print(response.text)
