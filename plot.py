"""
Created on 4/30/18

@author: Jingchao Yang
"""
from matplotlib import pyplot as plt

'''Time Series Plot
Plotting basic unfiltered time seris data 
for earthquake and tsu event from 1900 to present
'''
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

'''Scatter Plot
Plotting all earthquake caused tsu event, 
and set x,y to surface magnitude, focal depth
'''
# import dataFilter
#
# X = dataFilter.tsuOnly['EQ_MAG_MS']
# Y = dataFilter.tsuOnly['FOCAL_DEPTH']
#
# plt.title('Tsunami Observation Regarding Earthquake Surface Magnitude and Focal Depth')
# plt.scatter(X, Y)
# plt.xlabel("Surface Magnitude")
# plt.ylabel("Focal Depth (km)")
# plt.show()  # cluster is how tsu caused by specific surface magnitude, focal depth of an earthquake

"""Autocorrelation Plot
Plotting for earthquake surface magnitude
earthquake forcal depth and tsunami maxWaterHeight"""
import dataFilter
from statsmodels.tsa.stattools import acf

# lag=N/5
lags = int(len(dataFilter.surMagFilter) / 5)
# adopting autocorrelation function
acfsurMag = acf(dataFilter.surMagFilter, nlags=lags)
# print('AOT autocorrelation coefficients:', acfAOT)
acffodep = acf(dataFilter.fodepFilter, nlags=lags)
# print('ENSO autocorrelation coefficients:', acfENSO)
acfmaxWaterHeight = acf(dataFilter.maxWaterHeightFilter, nlags=lags)
# print('TS autocorrelation coefficients:', acfTS)

lagSeries = list(range(0, lags + 1))

plt.subplot(311)
plt.plot(lagSeries, acfsurMag, label='Surface Magnitude')
plt.legend(loc='best')
plt.title('Autocorrelation Coefficients')
plt.subplot(312)
plt.plot(lagSeries, acffodep, label='Focal Depth')
plt.legend(loc='best')
plt.subplot(313)
plt.plot(lagSeries, acfmaxWaterHeight, label='Max Water Height')
plt.legend(loc='best')
plt.xlabel('Lag')
plt.show()

"""decompose, trend"""
