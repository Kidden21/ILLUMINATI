import math
from decimal import *

#https://gps-coordinates.org/distance-between-coordinates.php

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

x1 = 3.0613374
y1 = 101.60814700000003
x2 = 3.0648608
y2 = 101.60098249999999

result = distance(x1, y1, x2, y2)
result_m = result * 1000
print(result)
print(result_m)
