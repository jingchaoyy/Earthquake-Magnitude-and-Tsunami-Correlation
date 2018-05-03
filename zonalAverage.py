"""
Created on 5/2/18

@author: Jingchao Yang
"""
import dataPrepro
import numpy as np
import pandas as pd

earthquakeLat = dataPrepro.earthquake['LATITUDE']
tsuLat = dataPrepro.tsu['LATITUDE']

latsInterval = np.arange(-90, 100, 10)


def contEventByAtt(att):
    attRanges, eventObjs = [], []
    for i in att:
        print(i)
        if i is not None:
            if len(attRanges) > 0:
                for j in attRanges:
                    if i in range(j[0], j[1]):
                        for k in eventObjs:
                            if j == k.att:
                                k.contEvent()
                else:
                    for z in range(len(latsInterval) - 1):
                        if float(i) * 1000 in range(latsInterval[z] * 1000, latsInterval[z + 1] * 1000):
                            attRanges.append((latsInterval[z], latsInterval[z + 1]))
                            e = dataPrepro.EventObj()
                            e.att = (latsInterval[z] / latsInterval[z + 1])
                            e.contEvent()
                            eventObjs.append(e)
            else:
                for y in range(len(latsInterval) - 1):
                    if float(i) * 1000 in range(latsInterval[y] * 1000, latsInterval[y + 1] * 1000):
                        attRanges.append((latsInterval[y], latsInterval[y + 1]))
                        e = dataPrepro.EventObj()
                        e.att = (latsInterval[y] / latsInterval[y + 1])
                        e.contEvent()
                        eventObjs.append(e)

    return eventObjs


test = contEventByAtt(earthquakeLat)
# for t in test:
#     print(t.att, t.cont)
