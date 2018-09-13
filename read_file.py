import os
import codecs
from bs4 import BeautifulSoup
import urllib2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, date, time

def str_to_date(d, t):
    d = d.replace("/", "")
    t = t.replace(":", "")
    hour = (t[0] + t[1])
    minute = (t[2] + t[3])
    day = (d[0] + d[1])
    month = (d[2] + d[3])
    year = (d[4] + d[5] + d[6] + d[7])
    result = year + "-" + month + "-" + day + " " + hour + ":" + minute
    return result

def check_year(d):
    d = d.replace("/", "")
    year = int(d[4] + d[5] + d[6] + d[7])
    return year

def check_duplicate(datetime, item_list):
    if len(item_list) == 0:
        return False
    for item in item_list:
        if datetime == item:
            return True
    return False
        
cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()

for folder in os.listdir("/Users/Kidden/Desktop/ILLUMINATI/PublicInfoBanjir")[1:]:
    for year in os.listdir(r"/Users/Kidden/Desktop/ILLUMINATI/PublicInfoBanjir/" + folder)[1:]:
        counter = 1
        data = []
        for filename in os.listdir(r"/Users/Kidden/Desktop/ILLUMINATI/PublicInfoBanjir/" + folder + "/" + year)[1:]:
            html_file = codecs.open(r"/Users/Kidden/Desktop/ILLUMINATI/PublicInfoBanjir/" + folder + "/" + year + "/" + filename, "r")
            soup = BeautifulSoup(html_file, "lxml")
            table = soup.find("table")
            rows = table.find_all("tr")[1:]

            
            for row in rows:
                cols = row.find_all("td")

                check = check_year(cols[2].get_text())
                
                if check == int(year):
                    datetime = str_to_date(cols[2].get_text(), cols[3].get_text())
                    duplicate = check_duplicate(datetime, data)

                    if not duplicate:
                        doc_ref = db.collection(folder).document(year + "-" + str(counter))
                        doc_ref.set({
                            "Station_Name": cols[1].get_text(),
                            "Date": datetime,
                            "Info":{
                                "Water_Level": int(cols[4].get_text()),
                                "RF_Level": {
                                    "Monthly": int(cols[5].get_text()),
                                    "Daily": int(cols[6].get_text())
                                    }
                                }
                            })
                        counter += 1
                        data.append(datetime)


'''

for filename in os.listdir("/Users/Kidden/Desktop/PublicInfoBanjir")[1:]:
    html_file = codecs.open(r"/Users/Kidden/Desktop/PublicInfoBanjir/" + filename, "r")
    soup = BeautifulSoup(html_file, "lxml")
    table = soup.find("table")
    rows = table.find_all("tr")[1:]

    for row in rows:
        cols = row.find_all("td")

        station_name = cols[1].get_text()
        station_date_time = str_to_date(cols[2].get_text(), cols[3].get_text())

        docs = db.collection(station_name).get()
        for doc in docs:
            data = doc.to_dict()
            if data["Date"] != station_date_time:
                doc_ref = db.collection(station_name).add({
                    "Station Name": station_name,
                    "Date": station_date_time,
                    "Info": {
                        "Water Level": int(cols[4].get_text()),
                        "RF Level": {
                            "Monthly": int(cols[5].get_text()),
                            "Daily": int(cols[6].get_text())
                            }
                        }
                    })


data.append({
"Station Name": cols[1].get_text(),
"Date": cols[2].get_text(),
"Time": cols[3].get_text(),
"Water Level": cols[4].get_text(),
"RF Level (month)": cols[5].get_text(),
"RF Level (daily)": cols[6].get_text()
})

#print(data[1])

#for item in data:
#doc_ref = db.collection(folder).document(year)
#doc_ref.set(data)

html_file = codecs.open("parit.html", "r")
soup = BeautifulSoup(html_file, "lxml")
table = soup.find("table")
rows = table.find_all("tr")[1:-1]

data = []
for row in rows:
    cols = row.find_all("td")
    data.append({
        "Station Name": cols[1].get_text(),
        "Date": cols[2].get_text(),
        "Time": cols[3].get_text(),
        "Water Level": cols[4].get_text(),
        "RF Level (month)": cols[5].get_text(),
        "RF Level (daily)": cols[6].get_text()
        })

print(data)
'''
