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


latsInterval = np.arange(-90, 100, 10)  # list for coordinate groups


def contEventByAtt(att):
    eventObjs = []
    for i in att:
        flag = False  # set a flag to check if i satisfy one of objects in the eventObjs list
        if len(eventObjs) > 0:
            for j in eventObjs:
                # for loop, checking if i satisfy one of objects in the eventObjs list
                if int(float(i) * 1000) in range(j.att[0] * 1000, j.att[1] * 1000):
                    j.contEvent()
                    flag = True  # when i satisfies one of objects in the eventObjs list, set the flag to true

            if flag == False:  # create new object and count if i do not satisfy any existing eventObj
                for z in range(len(latsInterval) - 1):
                    if int(float(i) * 1000) in range(latsInterval[z] * 1000, latsInterval[z + 1] * 1000):
                        e = dataPrepro.EventObj()
                        e.att = ([latsInterval[z], latsInterval[z + 1]])
                        e.contEvent()
                        eventObjs.append(e)
        else:  # if no event object created in the eventObjectList, create one
            for y in range(len(latsInterval) - 1):
                if int(float(i) * 1000) in range(latsInterval[y] * 1000, latsInterval[y + 1] * 1000):
                    e = dataPrepro.EventObj()
                    e.att = ([latsInterval[y], latsInterval[y + 1]])
                    e.contEvent()
                    eventObjs.append(e)

    return eventObjs


earthquakeGroups = contEventByAtt(earthquakeLatNotNan)
tsuGroups = contEventByAtt(tsuLatNotNan)


def getTup(group):  # convering ranged group to avg lat with count
    tup = []
    for group in group:
        m = (group.att[0] + group.att[1]) / 2
        tup.append((m, group.cont))
    return tup
