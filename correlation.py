"""
Created on 5/4/18

@author: Jingchao Yang
"""

import dataFilter
import dataPrepro
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import numpy as np

"""Time Series Correlation
Getting the pearson cc for time series based event count
"""
tcc1, tp1 = pearsonr(dataPrepro.equakeList, dataPrepro.tsuList)
print('\nPearson cc for all Earthquake and all Tsunami:', tcc1, 'p-value:', tp1)

"""Autocorrelation Coefficients
See plot.py
"""

"""Correlation for tsunami events count by interval
of earthquake surface magnitude and focal depth
"""
msInterval = np.arange(0, 11, 1)
fdInterval = np.arange(0, 210, 10)

# count events after grouping surface magnitude value
msIntervalCount = dataPrepro.contEventByAttWithInterval(msInterval, dataFilter.surMagFilter)
fdIntervalCount = dataPrepro.contEventByAttWithInterval(fdInterval, dataFilter.fodepFilter)

# convert event object to tuple list
msIntervalTup = dataPrepro.getTup(msIntervalCount)
fdIntervalTup = dataPrepro.getTup(fdIntervalCount)


# add value as zero if no event happened in a specific range
def add_zero(interval, tuples):
    test = []
    for i in range(len(interval) - 1):
        test.append(((interval[i] + interval[i + 1]) / 2, 0))

    for j in tuples:
        for k in test:
            if j[0] == k[0]:
                test.remove(k)

    return test


# sort the event tuple list by latitude
sortedMSIntervalTup = sorted(msIntervalTup + add_zero(msInterval, msIntervalTup), key=lambda t: t[0])
# print(sortedMSIntervalTup)
sortFDIntervalTup = sorted(fdIntervalTup + add_zero(fdInterval, fdIntervalTup), key=lambda t: t[0])
# print(sortFDIntervalTup)

msX, msY = [], []  # separate tuple to two lists
for et in sortedMSIntervalTup:
    msX.append(et[0])
    msY.append(et[1])

fdX, fdY = [], []
for tt in sortFDIntervalTup:
    fdX.append(tt[0])
    fdY.append(tt[1])

msIntervalcc1, msIntervalp1 = pearsonr(msX, msY)
fdIntervalcc2, fdIntervalp2 = pearsonr(fdX, fdY)
print('\nPearson cc for Surface_Magnitude and Tsunami_Count:', msIntervalcc1, 'p-value:', msIntervalp1,
      '\nPearson cc for Focal_Depth and Tsunami_Count:', fdIntervalcc2, 'p-value:', fdIntervalp2)

"""Pearson Correlation
Check if the a tsunami event (using MAXIMUM_WATER_HEIGHT) is
truly correlated to the surface magnitude and focal depth of
an earthquake"""
cc1, p1 = pearsonr(dataFilter.surMagFilterpd, dataFilter.maxWaterHeightFilterpd)
cc2, p2 = pearsonr(dataFilter.fodepFilterpd, dataFilter.maxWaterHeightFilterpd)
print('\nPearson cc for Surface_Magnitude and Max_Water_Height:', cc1, 'p-value:', p1,
      '\nPearson cc for Focal_Depth and Max_Water_Height:', cc2, 'p-value:', p2)

"""Spearman’s Rank Correlation
Evaluates the monotonic relationship
"""
scc1, sp1 = spearmanr(dataFilter.surMagFilterpd, dataFilter.maxWaterHeightFilterpd)
scc2, sp2 = spearmanr(dataFilter.fodepFilterpd, dataFilter.maxWaterHeightFilterpd)
print('\nSpearman’s rank cc for Surface_Magnitude and Max_Water_Height:', scc1, 'p-value:', sp1,
      '\nSpearman’s rank cc for Focal_Depth and Max_Water_Height:', scc2, 'p-value:', sp2)
