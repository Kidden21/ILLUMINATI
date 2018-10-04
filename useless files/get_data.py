import os
import sys
import codecs
from bs4 import BeautifulSoup
import urllib2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

<<<<<<< HEAD
cred = credentials.Certificate("/Users/bebechin/Desktop/ILLUMINATI/fit5120-4aadd-0e23c690ae70.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-4aadd",
    })

db = firestore.client()
docs = db.collection(u"B14BatuKurau").get()
=======
cred = credentials.Certificate("/Users/Kidden/Desktop/ILLUMINATI/fit5120-ddc5582972f2.json")
firebase_admin.initialize_app(cred, {
    "projectId": "fit5120-fb6c5",
    })

db = firestore.client()
docs = db.collection(u"Parit").get()
>>>>>>> 8b71ee6134c43ad44ef023a901b0a120e19111ed
date = []
water_level = []
for doc in docs:
    data = doc.to_dict()
    date.append(data["Date"])
    info = data["Info"]
    water_level.append(info["Water_Level"])

item_list = {}
item_list["date"] = date
item_list["water_level"] = water_level

df = pd.DataFrame(item_list)
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
dg = df.groupby(pd.Grouper(key="date", freq="1M")).sum()
dg.index = dg.index.strftime("%B")


<<<<<<< HEAD
month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

print(len(dg))






=======
print(dg.iloc[0]["water_level"])


month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
>>>>>>> 8b71ee6134c43ad44ef023a901b0a120e19111ed

##label = ['Adventure', 'Action', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical',
##         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', 'Multiple Genres', 'Reality']
##no_movies = [
##    941,
##    854,
##    4595,
##    2125,
##    942,
##    509,
##    548,
##    149,
##    1952,
##    161,
##    64,
##    61,
##    35,
##    5
##]
##
##def plot_bar_x():
##    # this is for plotting purpose
##    index = np.arange(len(label))
##    plt.bar(index, no_movies)
##    plt.xlabel('Genre', fontsize=5)
##    plt.ylabel('No of Movies', fontsize=5)
##    plt.xticks(index, label, fontsize=5, rotation=30)
##    plt.title('Market Share for Each Genre 1995-2017')
##    plt.show()
##
##plot_bar_x()


