import csv
import random
import warnings
import os
from requests.auth import HTTPDigestAuth
from locust import HttpUser, task, between

URI = "/index.php/settings/healthbuddy/getHealthBuddyDetails?userID=418689"


class SastaSundarSearch(HttpUser):
    host = os.getenv('TARGET_URL', 'https://temp-preprod.customerapi.sastasundar.com')

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def cust_api_call(self):
        response = self.client.get(URI, auth=HTTPDigestAuth('admin', '1234'))
        # print(response.text)
