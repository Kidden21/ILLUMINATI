import os
import codecs
from bs4 import BeautifulSoup
from datetime import datetime, date, time
from operator import truediv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pyfcm import FCMNotification
import math

def degreetoRadian(degrees):
    return degrees * math.pi / 180

def distance(x1, y1, x2, y2):
    earthradiusKM = 6371
    x = degreetoRadian(x1-x2)
    y = degreetoRadian(y1-y2)

    X = degreetoRadian(x)
    Y = degreetoRadian(y)

    a = math.sin(x/2) * math.sin(x/2) + math.sin(y/2) * math.sin(y/2) * math.cos(X) * math.cos(Y)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earthradiusKM * c

def grab_token():
    db = firestore.client()
    docs = db.collection(u"devices").where(u"userId", u"==", u"testUser").get()
    tokens = []
    for doc in docs:
        data = doc.to_dict()
        tokens.append(data["token"])
    return tokens

def calculation(wL1, wL2, t1, t2):
    wL = abs(int(wL1) - int(wL2))
    t1 = datetime.strptime(t1, "%H:%M")
    t2 = datetime.strptime(t2, "%H:%M")
    t = (t2 - t1)
    t = (t.seconds//60)
    result = truediv(wL, t)
    return round(result, 2)

cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()

push_service = FCMNotification(api_key="AAAASPxj3ek:APA91bHtLxwS4_xgg1dekD-X0-3y9kwygL3sYy9-b9Y1uMmHpcNWoB7c2fkRqDmH6_zcmh7GiKBYQXSplv5kl7LK0egAkpKYH1Cfag8LaJaq9FRu1CvcB7NH6fa-xMK0ywGpH239IGxWG5gg1ZPXVBRJ_y6w29tdIw")

tokens = grab_token()

alert_system_list = [
                     {"StationName": "SungaiSlim", "AlertLevel": 2100, "WarningLevel": 2200,"DangerLevel": 2300, "Latitude": 3.826389, "Longitude": 101.411111, "Population_Score": 1},
                     {"StationName": "PasangApi_BaganDatok", "AlertLevel": 300, "WarningLevel": 330,"DangerLevel": 400, "Latitude": 3.988158, "Longitude": 100.765469, "Population_Score": 1},
                     {"StationName": "TasikBanding", "AlertLevel": 24700, "WarningLevel": 24769,"DangerLevel": 24838, "Latitude": 5.550586, "Longitude": 101.352733, "Population_Score": 1},
                     {"StationName": "BukitMerah", "AlertLevel": 900, "WarningLevel": 904,"DangerLevel": 914, "Latitude": 5.0183, "Longitude": 100.652778, "Population_Score": 1},
                     {"StationName": "KualaPari", "AlertLevel": 3500, "WarningLevel": 3530,"DangerLevel": 3600, "Latitude": 4.57804, "Longitude": 101.06891, "Population_Score": 2},
                     {"StationName": "TanjungRambutan", "AlertLevel": 6650, "WarningLevel": 6715,"DangerLevel": 6780, "Latitude": 4.668042, "Longitude": 101.157006, "Population_Score": 2},
                     {"StationName": "TanjungTualang", "AlertLevel": 1300, "WarningLevel": 1375,"DangerLevel": 1450, "Latitude": 4.322222, "Longitude": 101.075, "Population_Score": 2},
                     {"StationName": "JambatanIskandar", "AlertLevel": 5400, "WarningLevel": 5424,"DangerLevel": 5480, "Latitude": 4.8194, "Longitude": 100.965278, "Population_Score": 1},
                     {"StationName": "KampungLintang", "AlertLevel": 3500, "WarningLevel": 3565,"DangerLevel": 3630, "Latitude": 4.9375, "Longitude": 101.102778, "Population_Score": 1},
                     {"StationName": "PondokTanjong", "AlertLevel": 1500, "WarningLevel": 1524,"DangerLevel": 1580, "Latitude": 5.01185, "Longitude": 100.73116, "Population_Score": 1},
                     {"StationName": "UluIjok", "AlertLevel": 3500, "WarningLevel": 3530,"DangerLevel": 3550, "Latitude": 5.120606, "Longitude": 100.804141, "Population_Score": 1},
                     {"StationName": "KgSgKuning", "AlertLevel": 1950, "WarningLevel": 2025,"DangerLevel": 2100, "Latitude": None, "Longitude": None, "Population_Score": 1},
                     {"StationName": "B14BatuKurau", "AlertLevel": 2000, "WarningLevel": 2050, "DangerLevel": 2100, "Latitude": 4.977639, "Longitude": 100.779222, "Population_Score": 1},
                     {"StationName": "KampungGajah", "AlertLevel": 650, "WarningLevel": 665,"DangerLevel": 700, "Latitude": 4.1796, "Longitude": 100.929925, "Population_Score": 1},
                     {"StationName": "Parit", "AlertLevel": 1980, "WarningLevel": 2070,"DangerLevel": 2160, "Latitude": 4.4722, "Longitude": 100.9046, "Population_Score": 1},
                     {"StationName": "TelukSena", "AlertLevel": 1100, "WarningLevel": 1190,"DangerLevel": 1280, "Latitude": 4.2559, "Longitude": 100.89938, "Population_Score": 1},
                     {"StationName": "BaganDatuk", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": None, "Longitude": None, "Population_Score": 1},
                     {"StationName": "BukitLarut", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 4.850194, "Longitude": 100.783528, "Population_Score": 1},
                     {"StationName": "ChangkatJong", "AlertLevel": 310, "WarningLevel": 340,"DangerLevel": 350, "Latitude": None, "Longitude": None, "Population_Score": 1},
                     {"StationName": "Emp.Cenderoh", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": None, "Longitude": None, "Population_Score": 1},
                     {"StationName": "FeldaIjok", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.163611, "Longitude": 100.7675, "Population_Score": 1},
                     {"StationName": "GuaTempurung", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 4.434278, "Longitude": 101.190831, "Population_Score": 2},
                     {"StationName": "KampongLalang", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.604167, "Longitude": 101.080556, "Population_Score": 1},
                     {"StationName": "KelianGunungIjok", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.149722, "Longitude": 100.885, "Population_Score": 1},
                     {"StationName": "KgPantaiBesar", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.086666, "Longitude": 100.859722, "Population_Score": 1},
                     {"StationName": "KgSahom", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 4.385847, "Longitude": 101.21458, "Population_Score": 2},
                     {"StationName": "KgSempeneh", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 4.925277, "Longitude": 100.828055, "Population_Score": 1},
                     {"StationName": "KgSgRambutan", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.275188, "Longitude": 100.780361, "Population_Score": 1},
                     {"StationName": "KualaKenderong", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.416667, "Longitude": 101.154167, "Population_Score": 1},
                     {"StationName": "LadangSeldings", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.247222, "Longitude": 100.729722, "Population_Score": 1},
                     {"StationName": "LojiAirSgBayor", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.258888, "Longitude": 100.831666, "Population_Score": 1},
                     {"StationName": "PulauPangkor", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 4.246305, "Longitude": 100.55425, "Population_Score": 1},
                     {"StationName": "RumahJPSAlorPongsu", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.046388, "Longitude": 100.590555, "Population_Score": 1},
                     {"StationName": "Samagagah", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.066667, "Longitude": 100.536944, "Population_Score": 1},
                     {"StationName": "Selama", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 5.216667, "Longitude": 100.6833, "Population_Score": 1},
                     {"StationName": "SgArakgBatu20", "AlertLevel": 2350, "WarningLevel": 2380,"DangerLevel": 2450, "Latitude": 5.0325, "Longitude": 100.79, "Population_Score": 1},
                     {"StationName": "SgKurauPondokTanjung", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": None, "Longitude": None, "Population_Score": 1},
                     {"StationName": "SgSelamaGuaPetai", "AlertLevel": 1450, "WarningLevel": 1465,"DangerLevel": 1500, "Latitude": 5.237222, "Longitude": 100.72, "Population_Score": 1},
                     {"StationName": "SungaiBil", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 3.835331, "Longitude": 101.4941, "Population_Score": 1},
                     {"StationName": "UluSlim", "AlertLevel": None, "WarningLevel": None,"DangerLevel": None, "Latitude": 3.865642, "Longitude": 101.448064, "Population_Score": 1}
                     ]

for item in os.listdir("/Users/Kidden/Desktop/ILLUMINATI/LatestData")[1:]:
    html_file = codecs.open(r"/Users/Kidden/Desktop/ILLUMINATI/LatestData/" + item, "r")
    soup = BeautifulSoup(html_file, "lxml")
    table = soup.find("table")
    rows = table.find_all("tr")[-2:]
    row = table.find_all("tr")[-1]
    before = True
    water_level = []

    col = row.find_all("td")
    
    station_name = col[1].get_text()

    if before:
        for i in range(len(alert_system_list)):
            if alert_system_list[i]["StationName"] == station_name:
                alert = alert_system_list[i]["AlertLevel"]
                warning = alert_system_list[i]["WarningLevel"]
                danger = alert_system_list[i]["DangerLevel"]
                population = alert_system_list[i]["Population_Score"]
                before = False
                pass

    if alert == None or warning == None or danger == None:
        break
    
    if int(col[4].get_text()) <= alert:
        score = 1
        multiplier = False
        
    elif int(col[4].get_text()) >= alert and int(col[4].get_text()) <= danger:
        score = 2
        multiplier = False
        if int(col[4].get_text()) >= warning:
            message_title = str(station_name) + ": Warning Level"
            message_body = "The current water level is in level 2 (WARNING) with a water level of " + str(col[4].get_text())
        if int(col[4].get_text()) >= alert:
            message_title = str(station_name) + ": Alert Level"
            message_body = "The current water level is in level 1 (ALERT) with a water level of " + str(col[4].get_text())
        for token in tokens:
            result = push_service.notify_single_device(registration_id=token, message_title=message_title, message_body=message_body)
            
    elif int(col[4].get_text()) >= danger:
        score = 3
        multiplier = True
        if  multiplier:
            final_score = score * population
            if final_score == 3 or final_score == 6:
                print("Loss of Property less, injury may present, few setup of flood relief centre")
            elif final_score == 9:
                print("Loss of property is medium, Injury and death casualties may present, proper flood relief centre may required")
            elif final_score == 12 or final_score == 15:
                print("Loss of property is high, injury and death casualties present, huge and big facility for flood relief centre")
        for item in rows:
            cols = item.find_all("td")
            
            water_level.append([cols[3].get_text(), cols[4].get_text()])

        docs = db.collection(u"data_analysis").where(u"Location", u"==", station_name).get()
        for doc in docs:
            data = doc.to_dict()
            count = data["count"]
        
            
        if len(water_level) == 2:
            if water_level[0][1] == water_level[1][1]:
                count = 0
                status = str("green")
                doc_ref = db.collection("data_analysis").document(station_name)
                doc_ref.set({
                    "Location": station_name,
                    "Date": col[2].get_text(),
                    "Time": cols[3].get_text(),
                    "Increment": 0,
                    "Message": u"Water Level remains unchanged in this 15 minutes",
                    "Flood_Status": u"Normal",
                    "Population_Score": population,
                    "Flood_Severity": 1,
                    "Flood_Risk_Score": final_score,
                    "count": count
                    })
                
            elif water_level[0][1] > water_level[1][1]:
                level_per_min = calculation(water_level[0][1], water_level[1][1], water_level[0][0], water_level[1][0])
                count = 0
                doc_ref = db.collection("data_analysis").document(station_name)
                doc_ref.set({
                    "Location": station_name,
                    "Date": col[2].get_text(),
                    "Time": cols[3].get_text(),
                    "Increment": level_per_min,
                    "Message": u"Water Level decreasing at a rate " + str(level_per_min) + " cm/min",
                    "Flood_Status": u"Normal",
                    "Population_Score": population,
                    "Flood_Severity": 2,
                    "Flood_Risk_Score": final_score,
                    "count": count
                    })

            elif water_level[0][1] < water_level[1][1]:
                level_per_min = calculation(water_level[0][1], water_level[1][1], water_level[0][0], water_level[1][0])
                count += 1
                doc_ref = db.collection("data_analysis").document(station_name)
                doc_ref.set({
                    "Location": station_name,
                    "Date": col[2].get_text(),
                    "Time": cols[3].get_text(),
                    "Increment": level_per_min,
                    "Message": u"Water Level increasing at a rate " + str(level_per_min) + " cm/min",
                    "Flood_Status": u"Warning",
                    "Population_Score": population,
                    "Flood_Severity": 3,
                    "Flood_Risk_Score": final_score,
                    "count": count
                    })          


        if count >= 5:
            doc_ref = db.collection("data_analysis").document(station_name)
            doc_ref.set({
                "Location": station_name,
                "Date": col[2].get_text(),
                "Time": cols[3].get_text(),
                "Increment": level_per_min,
                "Message": u"Flood might exist!!!",
                "Flood_Status": u"Danger",
                "Population_Score": population,
                "Flood_Severity": 3,
                "Flood_Risk_Score": final_score,
                "count": count
                }) 
        
        for token in tokens:
            message_title = str(station_name) + ": Danger Level" 
            message_body = "The current water level is in level 3 (DANGER) with a water level of " + str(col[4].get_text())
            result = push_service.notify_single_device(registration_id=token, message_title=message_title, message_body=message_body)
'''
    if multiplier:
        final_score = score * population
        if final_score == 3 or final_score == 6:
            print("Loss of Property less, injury may present, few setup of flood relief centre")
        elif final_score == 9:
            print("Loss of property is medium, Injury and death casualties may present, proper flood relief centre may required")
        elif final_score == 12 or final_score == 15:
            print("Loss of property is high, injury and death casualties present, huge and big facility for flood relief centre")
'''

        
        
