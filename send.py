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

push_service = FCMNotification(api_key="firebase_admin.messaging")

message_title = "Uber Update!"
message_body = "Hello World!"
result = push_service.send(message_title)

cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()


