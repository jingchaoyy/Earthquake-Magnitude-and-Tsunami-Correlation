"""
Created on 4/30/18

@author: Jingchao Yang
"""
from matplotlib import pyplot as plt

'''Time Series Plot'''
# import dataPrepro
# fig, ax = plt.subplots()
# ax.plot(dataPrepro.timeLine, dataPrepro.equakeList, 'r', label="Earthquake")
# ax.plot(dataPrepro.timeLine, dataPrepro.equakeLocationFilteredList, 'g', label="Earthquake Filtered")
# ax.plot(dataPrepro.timeLine, dataPrepro.tsuList, 'b', label="Tsunami")
#
# legend = ax.legend(loc='upper left', shadow=True, fontsize='large')
#
# plt.title('Time Series')
# plt.xlabel('Year')
# plt.ylabel('Event Counts')
# plt.show()

'''Scatter Plot'''
# import dataFilter
#
# X = dataFilter.tsuOnly['EQ_MAG_MS']
# Y = dataFilter.tsuOnly['FOCAL_DEPTH']
#
# plt.title('Tsunami Observation Regarding Earthquake Surface Magnitude and Focal Depth')
# plt.scatter(X, Y)
# plt.xlabel("Surface Magnitude")
# plt.ylabel("Focal Depth (km)")
# plt.show()

'''Zonal Avg. Plot'''
import zonalAverage

group1= zonalAverage.earthquakeGroups
group2= zonalAverage.tsuGroups

earthquakeTup = zonalAverage.getTup(group1)
tsuTup = zonalAverage.getTup(group2)

sortedearthquakeTup = sorted(earthquakeTup, key=lambda t:t[0])
sortTsuTup = sorted(tsuTup, key=lambda t:t[0])

eX, eY = [],[]
for et in sortedearthquakeTup:
    eX.append(et[0])
    eY.append(et[1])

tX, tY = [],[]
for tt in sortTsuTup:
    tX.append(tt[0])
    tY.append(tt[1])

# plt.title('Zonal Average')
# plt.plot(eX, eY)
# plt.plot(tX, tY)
# plt.xlabel("Lats")
# plt.ylabel("Counts")
# plt.show()


fig, ax = plt.subplots()
ax.plot(eX, eY, 'r', label="Earthquake Count")
ax.plot(tX, tY, 'b', label="Tsunami Count")

legend = ax.legend(loc='upper left', shadow=True, fontsize='large')

plt.title('Zonal Average')
plt.xlabel('Lats')
plt.ylabel('Event Counts')
plt.show()
