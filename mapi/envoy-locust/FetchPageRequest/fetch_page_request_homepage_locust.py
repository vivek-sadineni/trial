import json
import warnings
import os
import sonora.client

from locust import HttpUser, task

body = {
    "path": "/home-page",
    "appInfo": {
        "appVersion": "1",
        "appType": "MSITE"
    },
    "deviceInfo": {
        "deviceId": "9bd56fcd9e5578832771829300af556c",
        "deviceIP": "0.0.0.0"
    },
    "userInfo": {
        "accountId": "",
        "userType": "New",
        "loggedIn": "LOGGED_IN",
        "org": "FKH"
    },
    "request": {
        "userId": "",
        "appVersion": "1",
        "deviceId": "9bd56fcd9e5578832771829300af556c",
        "csrf": "40ba6efb9ce843dca939183ea3b4971d"
    },
    "fetchPageReactionType": "NAVIGATE_TO_PAGE"
}

header_object = {
    "x-client": "mapi",
    "x-csrf-test-name": "0228f2e755cc4f2593c42ccfc26236f0",
    "x-timestamp": "142433",
    "x-user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/104.0.0.0 Mobile Safari/537.36 ",
    "x-cookie": "_fbp=fb.1.1661241781083.484329401; moe_uuid=c7bb2d7f-dc2e-4cff-8aee-f367a8bc6d8b; isPanIndia=Y; "
                "cartsynch=0; UserLocationPincode=560103; LocationSkipped=0; IsLab=0; WHId=1; "
                "PanIndiaCityName=Others; userLocation=Others; PanIndiaStateName=Others; PanIndiaStateCode=OT; "
                "PanIndiaCityID=6310; UIVAL=AwEGeA%3D%3D; cisession_in_com=5d0e9ccc5189c144c310efe560752480; "
                "PanIndiaStateID=37; sspl_csrf=0228f2e755cc4f2593c42ccfc26236f0 "
}


class FetchPageHomepage(HttpUser):
    host = os.getenv('TARGET_URL', 'https://fkh.nl-demo.com/')

    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False

    @task
    def get_homepage(self):
        self.client.post("", data=json.dumps(body), auth=None, headers=header_object)
