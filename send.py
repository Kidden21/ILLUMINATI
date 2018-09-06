import os
import sys
import codecs
from bs4 import BeautifulSoup
import urllib2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pyfcm import FCMNotification

def grab_token():
    db = firestore.client()
    docs = db.collection(u"devices").where(u"userId", u"==", u"testUser").get()
    tokens = []
    for doc in docs:
        data = doc.to_dict()
        tokens.append(data["token"])
    return tokens

cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

push_service = FCMNotification(api_key="AAAASPxj3ek:APA91bHtLxwS4_xgg1dekD-X0-3y9kwygL3sYy9-b9Y1uMmHpcNWoB7c2fkRqDmH6_zcmh7GiKBYQXSplv5kl7LK0egAkpKYH1Cfag8LaJaq9FRu1CvcB7NH6fa-xMK0ywGpH239IGxWG5gg1ZPXVBRJ_y6w29tdIw")

tokens = grab_token()

alert_system_list = [
                     {"StationName": "SungaiSlim", "AlertLevel": 2700, "WarningLevel": 2730,"DangerLevel": 2400},
                     {"StationName": "PasangApi_BaganDatok", "AlertLevel": 300, "WarningLevel": 330,"DangerLevel": 400},
                     {"StationName": "TasikBanding", "AlertLevel": 24700, "WarningLevel": 24769,"DangerLevel": 24838},
                     {"StationName": "BukitMerah", "AlertLevel": 900, "WarningLevel": 904,"DangerLevel": 914},
                     {"StationName": "KualaPari", "AlertLevel": 3500, "WarningLevel": 3530,"DangerLevel": 3600},
                     {"StationName": "TanjungRambutan", "AlertLevel": 6650, "WarningLevel": 6715,"DangerLevel": 6780},
                     {"StationName": "TanjungTualang", "AlertLevel": 1300, "WarningLevel": 1375,"DangerLevel": 1450},
                     {"StationName": "JambatanIskandar", "AlertLevel": 5400, "WarningLevel": 5424,"DangerLevel": 5480},
                     {"StationName": "KampungLintang", "AlertLevel": 3500, "WarningLevel": 3565,"DangerLevel": 3630},
                     {"StationName": "PondokTanjong", "AlertLevel": 1500, "WarningLevel": 1524,"DangerLevel": 1580},
                     {"StationName": "UluIjok", "AlertLevel": 3500, "WarningLevel": 3530,"DangerLevel": 3550},
                     {"StationName": "KgSgKuning", "AlertLevel": 1950, "WarningLevel": 2025,"DangerLevel": 2100},
                     {"StationName": "B14BatuKurau", "AlertLevel": 2400, "WarningLevel": 2470, "DangerLevel": 2540},
                     {"StationName": "KampungGajah", "AlertLevel": 650, "WarningLevel": 665,"DangerLevel": 700},
                     {"StationName": "Parit", "AlertLevel": 1980, "WarningLevel": 2070,"DangerLevel": 2160},
                     {"StationName": "TelukSena", "AlertLevel": 1100, "WarningLevel": 1190,"DangerLevel": 1280}
                     ]

for item in os.listdir("/Users/Kidden/Desktop/ILLUMINATI/LatestData")[1:]:
    html_file = codecs.open(r"/Users/Kidden/Desktop/ILLUMINATI/LatestData/" + item, "r")
    soup = BeautifulSoup(html_file, "lxml")
    table = soup.find("table")
    rows = table.find_all("tr")[1:]
    before = True
    
    for row in rows:
        cols = row.find_all("td")

        station_name = cols[1].get_text()
        print(station_name)
        if before:
            for i in range(len(alert_system_list)):
                if alert_system_list[i]["StationName"] == station_name:
                    alert = alert_system_list[i]["AlertLevel"]
                    warning = alert_system_list[i]["WarningLevel"]
                    danger = alert_system_list[i]["DangerLevel"]
                    before = False
                    pass

        if int(cols[4].get_text()) >= danger:
            for token in tokens:
                registration_id = token
                message_title = str(station_name) + ": Danger Level" 
                message_body = "The current water level is in level 3 (DANGER) with a water level of " + str(cols[4].get_text())
                result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
##            message_title = str(station_name) + ": Danger Level" 
##            message_body = "The current water level is in level 3 (DANGER) with a water level of " + str(cols[4].get_text())
##            result = push_service.notify_multiple_device(registration_id=tokens, message_title=message_title, message_body=message_body)
        elif int(cols[4].get_text()) >= warning:
            for token in tokens:
                registration_id = token
                message_title = str(station_name) + ": Warning Level"
                message_body = "The current water level is in level 2 (WARNING) with a water level of " + str(cols[4].get_text())
                result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
##            message_title = str(station_name) + ": Warning Level"
##            message_body = "The current water level is in level 2 (WARNING) with a water level of " + str(cols[4].get_text())
##            result = push_service.notify_multiple_device(registration_id=tokens, message_title=message_title, message_body=message_body)
        elif int(cols[4].get_text()) >= alert:
            for token in tokens:
                registration_id = token
                message_title = str(station_name) + ": Alert Level"
                message_body = "The current water level is in level 1 (ALERT) with a water level of " + str(cols[4].get_text())
                result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
##            message_title = str(station_name) + ": Alert Level"
##            message_body = "The current water level is in level 1 (ALERT) with a water level of " + str(cols[4].get_text())
##            result = push_service.notify_multiple_device(registration_id=tokens, message_title=message_title, message_body=message_body)


