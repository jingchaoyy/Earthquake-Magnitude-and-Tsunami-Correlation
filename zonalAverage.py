"""
Created on 5/2/18

@author: Jingchao Yang
"""
import dataPrepro
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

earthquakeLat = dataPrepro.earthquake['LATITUDE']
earthquakeLatNotNan = earthquakeLat[pd.notnull(earthquakeLat)]
# print(len(earthquakeLatNotNan))

tsuLat = dataPrepro.tsu['LATITUDE']
tsuLatNotNan = tsuLat[pd.notnull(tsuLat)]
# print(len(tsuLatNotNan))


latsInterval = np.arange(-90, 100, 10)  # list for coordinate groups, interval for filtering data


earthquakeGroups = dataPrepro.contEventByAttWithInterval(latsInterval,earthquakeLatNotNan)
tsuGroups = dataPrepro.contEventByAttWithInterval(latsInterval,tsuLatNotNan)

'''Zonal Avg. Plot
Plotting Zonal Average, cont number of events
that happened in a specific latitude zone
'''

earthquakeTup = dataPrepro.getTup(earthquakeGroups)
tsuTup = dataPrepro.getTup(tsuGroups)

# sort the event tuple list by latitude
sortedearthquakeTup = sorted(earthquakeTup, key=lambda t: t[0])
sortTsuTup = sorted(tsuTup, key=lambda t: t[0])

eX, eY = [], []
for et in sortedearthquakeTup:
    eX.append(et[0])
    eY.append(et[1])

tX, tY = [], []
for tt in sortTsuTup:
    tX.append(tt[0])
    tY.append(tt[1])

fig, ax = plt.subplots()
ax.plot(eX, eY, 'r', label="Earthquake Count")
ax.plot(tX, tY, 'b', label="Tsunami Count")
legend = ax.legend(loc='upper left', shadow=True, fontsize='large')
plt.title('Zonal Average')
plt.xlabel('Lats')
plt.ylabel('Event Counts')
plt.show()
