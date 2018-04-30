"""
Created on 4/30/18

@author: YJccccc
"""
import dataPrepro
from matplotlib import pyplot as plt

'''Time Series Plot'''
EarthquakePlot, = plt.plot(dataPrepro.timeLine, dataPrepro.equakeList, 'r', label="Earthquake")
TsunamiPlot, = plt.plot(dataPrepro.timeLine, dataPrepro.tsuList, 'b', label="Tsunami")
# adding legends
first_legend = plt.legend(handles=[EarthquakePlot], loc=1)
ax = plt.gca().add_artist(first_legend)
plt.legend(handles=[TsunamiPlot], loc=4)
plt.title('Time Series')
plt.xlabel('Year')
plt.ylabel('Event Counts')
plt.show()

'''Trend Plot'''
# decomposition = seasonal_decompose(equakeList)
# trend = decomposition.trend
# seasonal = decomposition.seasonal
# residual = decomposition.resid
#
# plt.subplot(411)
# plt.plot(timeLine)
# plt.title('Original Time Series')
# plt.subplot(412)
# plt.plot(trend)
# plt.title('Trend')
# plt.subplot(413)
# plt.plot(seasonal)
# plt.title('Seasonality')
# plt.subplot(414)
# plt.plot(residual)
# plt.title('Residuals')
# plt.tight_layout()
# plt.show()