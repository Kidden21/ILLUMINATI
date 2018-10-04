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
from pyfcm import FCMNotification

def grab_info(item_list):
    if item_list == None:
        return False
    rf_level = item_list["RF Level"]
    rf_level_monthly = rf_level["Monthly"]
    rf_level_daily = rf_level["Daily"]
    water_level = item_list["Water Level"]
    return rf_level_monthly, rf_level_daily, water_level

cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()
docs = db.collection(u"devices").where(u"userId", u"==", u"testUser").get()
token = []
for doc in docs:
    data = doc.to_dict()
    token.append(data["token"])
    
'''
try:
    for doc in docs:
        data = doc.to_dict()

        info = data["Info"]
        value1, value2, value3 = grab_info(info)
        if int(value3) >= 914:
            doc_ref = db.collection(u"ZZChecking").document(u"BukitMerah")
            doc_ref.set({
                "Water level": "Danger"
                })
        elif int(value3) >= 904:
            doc_ref = db.collection(u"ZZChecking").document(u"BukitMerah")
            doc_ref.set({
                "Water level": "Warning"
                })
        elif int(value3) >= 900:
            doc_ref = db.collection(u"ZZChecking").document(u"BukitMerah")
            doc_ref.set({
                "Water level": "Alert"
                })
except google.appengine.api.urlfetch_errors.DeadlineExceededError:
    pass
'''

    


