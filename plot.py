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
import dataFilter

X = dataFilter.tsuOnly['EQ_MAG_MS']
Y = dataFilter.tsuOnly['FOCAL_DEPTH']

plt.title('Tsunami Observation Regarding Earthquake Surface Magnitude and Focal Depth')
plt.scatter(X, Y)
plt.xlabel("Surface Magnitude")
plt.ylabel("Focal Depth (km)")
plt.show()
