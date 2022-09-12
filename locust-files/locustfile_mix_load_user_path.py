import csv
import random
import warnings
import os

from locust import HttpUser, task, between

device_id = "f21e21e1-a1bd-4b9e-a620-6da754085a9e"
body = {
        "csrf_test_name": "a4d5e94ce85672980f550924161b7f52"
}
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}
cookies = {
    "cookie": '''T=TI164922685845700296292883240291767363571549416617245158015905844352; Network-Type=4g; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; _gcl_au=1.1.1577513354.1654787934; WHId=1; cartsynch=0; InitForMob=false; pagerefresh=N; prescriptionId=; PHPSESSID=dr7as2hgeviuao2us520jsg172; addressTypName=; PanIndiaStateCode=WB; PanIndiaStateID=35; PanIndiaCityName=Kolkata; PanIndiaCityID=806; isPanIndia=N; LocationSkipped=0; IsLab=1; UserLocationPincode=700156; PanIndiaStateName=West%20Bengal; userLocation=West%20Bengal; _ga=GA1.1.101759026.1654787985; MembershipId=null; CardStatus=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19211%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1660416624%7C12%7CMCAAMB-1660416624%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1659819024s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Afurniture%25253Abeds-more%25253Abeds%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fflipkart-perfect-homes-sonore-engineered-wood-single-box-bed%25252Fp%25252Fitmdf04030a1%2526ot%253DA; SN=VIE02AEDFBEC394CEAA205AC62FD28F9F4.TOKE66E39E4860E41F28A6CDA258044B284.1659811945.LO; S=d1t19BlFgIjVCAwETdj8/P09NPz1rksS+D9G0TQQXYDqpdumcxd+UZuTm90FRDOBqzM5T7VBylLvvgA7I2PJXE/U1AA==; sspl_csrf=a4d5e94ce85672980f550924161b7f52; browserPopUpData=[null,"2022-08-08T10:37:49.237Z"]; GuestUserID=dr7as2hgeviuao2us520jsg172; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; cisession_in_com=3cf04e64ece42dd84631780b3ac7145e; UIVAL=AgAAdV1bEw5sFhI%3D; addressId=0; revisedCart=N; searchTxt=; _ga_PXT3VW5F62=GS1.1.1659955087.2.1.1659958258.49''',
}
SEARCH_LINK = "https://search.sastasundar.com/search?q={param}"

cookies_product = {
    "cookie": '''T=TI164922685845700296292883240291767363571549416617245158015905844352; Network-Type=4g; pxcts=96d08337-b573-11ec-94f4-5458434c6246; _pxvid=96d07630-b573-11ec-94f4-5458434c6246; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; _gcl_au=1.1.1577513354.1654787934; WHId=1; cartsynch=0; InitForMob=false; pagerefresh=N; prescriptionId=; PHPSESSID=dr7as2hgeviuao2us520jsg172; addressTypName=; PanIndiaStateCode=WB; PanIndiaStateID=35; PanIndiaCityName=Kolkata; PanIndiaCityID=806; isPanIndia=N; LocationSkipped=0; IsLab=1; UserLocationPincode=700156; PanIndiaStateName=West%20Bengal; userLocation=West%20Bengal; _ga=GA1.1.101759026.1654787985; MembershipId=null; CardStatus=null; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19211%7CMCMID%7C03547093981926272024322102480078472856%7CMCAAMLH-1660416624%7C12%7CMCAAMB-1660416624%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1659819024s%7CNONE%7CMCAID%7CNONE; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Afurniture%25253Abeds-more%25253Abeds%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Fflipkart-perfect-homes-sonore-engineered-wood-single-box-bed%25252Fp%25252Fitmdf04030a1%2526ot%253DA; SN=VIE02AEDFBEC394CEAA205AC62FD28F9F4.TOKE66E39E4860E41F28A6CDA258044B284.1659811945.LO; S=d1t19BlFgIjVCAwETdj8/P09NPz1rksS+D9G0TQQXYDqpdumcxd+UZuTm90FRDOBqzM5T7VBylLvvgA7I2PJXE/U1AA==; sspl_csrf=a4d5e94ce85672980f550924161b7f52; browserPopUpData=[null,"2022-08-08T10:37:49.237Z"]; GuestUserID=dr7as2hgeviuao2us520jsg172; profileUpdated=N; lab_booking_count=null; cookie_consent=Y; myorderpagevisitFK=Y; cisession_in_com=3cf04e64ece42dd84631780b3ac7145e; UIVAL=AgAAdV1bEw5sFhI%3D; addressId=0; searchTxt=; revisedCart=Y; _ga_PXT3VW5F62=GS1.1.1659961021.3.1.1659961045.36'''
}
product_body = {
    "productId":"66905",
    "warehouseId":"1",
    "apptype":"M",
    "panindia":"0",
    "pincode":"700156",
    "csrf_test_name":"a4d5e94ce85672980f550924161b7f52"
}

body_hpw = {
    "page": 1,
    "panindia": 0,
    "warehouseId": "1",
    "pincode": 700120,
    "userId": "4937724",
    "profileId": "",
    "app_type": "N",
    "app_version": "4.0.4",
    "app_version_code": 109,
    "resolution_type": "xhdpi",
    "deviceId": "81653dce-0dd2-4201-8916-4aecbdd89269",
    "IsLab": 1
}
class SastaSundarSearch(HttpUser):
    host = os.getenv('TARGET_URL', '')
    SEARCH_QUERIES = []
    def on_start(self):
        warnings.filterwarnings("ignore")
        self.client.verify = False
        self.fetch_search_queries()
    def fetch_search_queries(self):
        files = [open("locust-files/found + retail-customer + all-devices + all-scope + (2022-02-01 to 2022-02-08).csv"),
                 open("locust-files/not-found + retail-customer + all-devices + all-scope + (2022-02-01 to 2022-02-08).csv")]
        for file in files:
            csv_reader = csv.reader(file)
            for name in csv_reader:
                self.SEARCH_QUERIES.append(name)
    @task
    def mix_load(self):
        var = random.randint(0, 555)
        if var <= 345:
            self.client.post("https://catalog.sastasundar.com/home/getmasterhomewidgets", json=body_hpw)
        elif var <= 395:
            self.client.get(SEARCH_LINK.format(param=random.choice(self.SEARCH_QUERIES)))
        elif var < 513:
            self.client.post("https://healthplus.flipkart.com/index.php/webapi/product/getProductDetails",
                                        headers=headers, data=product_body, cookies=cookies_product)
        elif var <= 530:
            self.client.post(
                "http://healthplus.flipkart.com/index.php/webapi/fkh_app_in_app/dochkLogging_app_in_app",
                headers=headers, json=body, cookies=cookies)
            self.client.post("http://healthplus.flipkart.com/index.php/webapi/location/get_user_location",
                             headers=headers, json=body, cookies=cookies)
        elif var <= 555:
            browse_selector = random.randint(0, 4)
            if browse_selector == 0:
                self.client.get("https://search.sastasundar.com/search_reserved_keyword?q=covidessentialproduct"
                                "&panindia=0&appversion=4.0.4&apptype=N&aggregated=1&device=2&m=0&pincode=700156&wh=1"
                                "&timestamp=1485138143")
            elif browse_selector == 1:
                self.client.get("https://search.sastasundar.com/product_filter/?category_id=1114&selectedDosage=Gift"
                                 "+Health+Box&page=1&size=30&device=2&panindia=0&wh=1&pincode=700156&format=2"
                                 "&includeGiftable=1&aggregated=0&token=&app_version=4.0.3&app_version_code=108"
                                 "&timestamp=1624223751")
            elif browse_selector == 2:
                self.client.get("https://search.sastasundar.com/similar_products?product_id=2543&wh=1&panindia=0"
                                 "&pincode=700156&device=2&ptype=P&size=30&timestamp=359924824")
            elif browse_selector == 3:
                self.client.get("https://search.sastasundar.com/similar_products?product_id=66905&wh=1&panindia=0"
                                 "&pincode=700156&device=2&size=30&document_id=66905&timestamp=359712929")
            elif browse_selector == 4:
                self.client.get("https://search.sastasundar.com/bought_together?product_id=66905&wh=1&panindia=0"
                                 "&pincode=700156&device=2&size=30&document_id=66905&timestamp=359713634")

