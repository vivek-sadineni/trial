import csv
import random
import warnings
import os

from locust import HttpUser, task, between

SEARCH_LINK = "/search?q={param}"
device_id = "f21e21e1-a1bd-4b9e-a620-6da754085a9e"
body_get_otp = {
    "RequestHeader": {
        "AppType": "N",
        "AppVersion": "4.0.4",
        "AppVersionCode": "109",
        "DeviceId": "f21e21e1-a1bd-4b9e-a620-6da754085a9e",
        "DeviceDensity": "440",
        "DeviceDensityType": "xhdpi",
        "DeviceHeight": "2160",
        "DeviceWidth": "1080",
        "DeviceName": "Google Pixel 4a",
        "DeviceOsInfo": "12",
        "NetworkInfo": "Wifi",
        "AccessToken": "PDWZ5pStjE"
    },
    "RequestURI": {
        "Section": "regenerateOtp"
    },
    "Params": {
        "MobileNo": "9051026063",
        "UserIP": "",
        "UserAgent": "Dalvik/2.1.0 (Linux; U; Android 12; Pixel 4a Build/SQ1A.220205.002)",
        "CampaignId": "",
        "warehouseId": "",
        "PanIndia": "0",
        "Latitude": "",
        "Longitude": "",
        "Pincode": ""
    }
}

smallcase_char = "abcdefghijklmnopqrstuvwxyz"

def get_mobile_number():
    no = ""
    for i in range(0, 10):
        x = random.randint(5, 9)
        no = no + str(x)
    return no
def get_device_id():
    id = ""
    for ch in device_id:
        if 'a' <= ch <= 'z':
            id = id + random.choice(smallcase_char)
        elif '1' <= ch <= '9':
            id = id + str(random.randint(1,9))
        else:
            id = id + ch;
    print(id)
    return id;

class SastaSundarSearch(HttpUser):
    host = os.getenv('TARGET_URL', '')
    wait_time = between(1, 5)
    SEARCH_QUERIES = []

    def fetch_search_queries(self):
        files = [open("found + retail-customer + all-devices + all-scope + (2022-02-01 to 2022-02-08).csv"),
                 open("not-found + retail-customer + all-devices + all-scope + (2022-02-01 to 2022-02-08).csv")]
        for file in files:
            csv_reader = csv.reader(file)
            for name in csv_reader:
                self.SEARCH_QUERIES.append(name)

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False


    @task
    def sasta_sundar_search_query(self):
        body_get_otp["Params"]["MobileNo"] = get_mobile_number()
        body_get_otp["RequestHeader"]["DeviceId"] = get_device_id()
        response = self.client.post(
            "https://fkhp-preprod-api.sastasundar.com/sastasundar/customer/rest_customer/postData", json=body_get_otp)
        print(response.text)
