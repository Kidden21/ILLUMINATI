import os
import codecs
from bs4 import BeautifulSoup
import urllib2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, date, time
from ast import literal_eval

cred = credentials.Certificate("/Users/Kidden/Desktop/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()

doc_ref = db.collection(u"BaganDatuk").document(u"2011-2")

item_list = []
doc = doc_ref.get()
data = doc.to_dict()
for key, value in data.iteritems():
    temp = [key, value]
    item_list.append(temp)
print(item_list)
print(item_list[0][1])
