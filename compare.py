import os
import sys
import codecs
from bs4 import BeautifulSoup
import urllib2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, date, time
from ast import literal_eval

cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
#"projectId": "fit5120-fb6c5"
#"projectId": "flood-aid-application-ad8dc"
#cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/flood-aid-application-ad8dc-ea95d186ef46.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()

alert_system_list = [
                     {"StationName": "SungaiSlim", "AlertLevel": 2700, "WarningLevel": 2730,"DangerLevel": 2800},
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
        
        if before:
            for i in range(len(alert_system_list)):
                if alert_system_list[i]["StationName"] == station_name:
                    alert = alert_system_list[i]["AlertLevel"]
                    warning = alert_system_list[i]["WarningLevel"]
                    danger = alert_system_list[i]["DangerLevel"]
                    before = False
                    pass
            
        doc_ref = db.collection("zzchecking").document(station_name)
        doc_ref.set({
            "Station_Name": station_name,
            "Date": cols[2].get_text(),
            "Time": cols[3].get_text(),
            "Alert_System": {
                "Alert_Level": alert,
                "Warning_Level": warning,
                "Danger_Level": danger
                },
            "Info": {
                "Water_Level": int(cols[4].get_text()),
                "RF_Level": {
                    "Monthly": int(cols[5].get_text()),
                    "Daily": int(cols[6].get_text())
                    }
                }
            })
    
