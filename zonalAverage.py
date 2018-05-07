"""
Created on 5/2/18

@author: Jingchao Yang
"""
import dataPrepro
import numpy as np
import pandas as pd

earthquakeLat = dataPrepro.earthquake['LATITUDE']
earthquakeLatNotNan = earthquakeLat[pd.notnull(earthquakeLat)]
# print(len(earthquakeLatNotNan))

tsuLat = dataPrepro.tsu['LATITUDE']
tsuLatNotNan = tsuLat[pd.notnull(tsuLat)]
# print(len(tsuLatNotNan))


latsInterval = np.arange(-90, 100, 10)  # list for coordinate groups, interval for filtering data


earthquakeGroups = dataPrepro.contEventByAttWithInterval(latsInterval,earthquakeLatNotNan)
tsuGroups = dataPrepro.contEventByAttWithInterval(latsInterval,tsuLatNotNan)


def getTup(group):  # convering ranged group to avg lat with count
    tup = []
    for group in group:
        m = (group.att[0] + group.att[1]) / 2
        tup.append((m, group.cont))
    return tup
