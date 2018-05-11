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

"""Correlation for tsunami max water height avg by interval
of earthquake surface magnitude and focal depth
"""
# group earthquake attributes with wave height
ms_mwh = zip(dataFilter.surMagFilter, dataFilter.maxWaterHeightFilter)
fd_mwh = zip(dataFilter.fodepFilter, dataFilter.maxWaterHeightFilter)


# getting the average wave height by interval set to surface magnitude or focal depth
def getAvg(interval, group):  # function that similar to contEventByAttWithInterval in dataPrepro
    test1, test2 = [], []  # test1 for recording interval, test2 for MWH average
    for i in group:
        flag = False
        if len(test1) > 0:
            for j in range(len(test1)):
                if int(float(i[0]) * 1000) in range(test1[j][0] * 1000, test1[j][1] * 1000):
                    test2[j] = (test2[j] + i[1]) / 2
                    flag = True
            if flag == False:
                for k in range(len(interval) - 1):
                    if int(float(i[0]) * 1000) in range(interval[k] * 1000, interval[k + 1] * 1000):
                        test1.append((interval[k], interval[k + 1]))
                        test2.append(i[1])
        else:
            for z in range(len(interval) - 1):
                if int(float(i[0]) * 1000) in range(interval[z] * 1000, interval[z + 1] * 1000):
                    test1.append((interval[z], interval[z + 1]))
                    test2.append(i[1])
    test3 = []
    for y in test1:
        test3.append((y[0] + y[1]) / 2)

    # sort the tuple for later regression or correlation analysis
    sort = sorted(zip(test3, test2), key=lambda t: t[0])

    # seperate the tuple
    x, y = [], []
    for k in sort:
        x.append(k[0])
        y.append(k[1])

    return x, y


ms_mwhX, ms_mwhY = getAvg(msInterval, ms_mwh)
fd_mwhX, fd_mwhY = getAvg(fdInterval, fd_mwh)

ms_mwhcc1, ms_mwhp1 = pearsonr(ms_mwhX, ms_mwhY)
fd_mwhcc2, fd_mwhp2 = pearsonr(fd_mwhX, fd_mwhY)
print('\nPearson cc for Surface_Magnitude and Avg Max_Water_Height:', ms_mwhcc1, 'p-value:', ms_mwhp1,
      '\nPearson cc for Focal_Depth and Avg Max_Water_Height:', fd_mwhcc2, 'p-value:', fd_mwhp2)

ms_mwhscc1, ms_mwhsp1 = spearmanr(ms_mwhX, ms_mwhY)
fd_mwhscc2, fd_mwhsp2 = spearmanr(fd_mwhX, fd_mwhY)
print('\nSpearman cc for Surface_Magnitude and Avg Max_Water_Height:', ms_mwhscc1, 'p-value:', ms_mwhsp1,
      '\nSpearman cc for Focal_Depth and Avg Max_Water_Height:', fd_mwhscc2, 'p-value:', fd_mwhsp2)

"""Pearson Correlation
Check if the a tsunami event (using MAXIMUM_WATER_HEIGHT) is
truly correlated to the surface magnitude and focal depth of
an earthquake"""
cc1, p1 = pearsonr(dataFilter.surMagFilterpd, dataFilter.maxWaterHeightFilterpd)
cc2, p2 = pearsonr(dataFilter.fodepFilterpd, dataFilter.maxWaterHeightFilterpd)
print('\nPearson cc for Surface_Magnitude and Max_Water_Height:', cc1[0], 'p-value:', p1[0],
      '\nPearson cc for Focal_Depth and Max_Water_Height:', cc2[0], 'p-value:', p2[0])

"""Spearman’s Rank Correlation
Evaluates the monotonic relationship
"""
scc1, sp1 = spearmanr(dataFilter.surMagFilterpd, dataFilter.maxWaterHeightFilterpd)
scc2, sp2 = spearmanr(dataFilter.fodepFilterpd, dataFilter.maxWaterHeightFilterpd)
print('\nSpearman’s rank cc for Surface_Magnitude and Max_Water_Height:', scc1, 'p-value:', sp1,
      '\nSpearman’s rank cc for Focal_Depth and Max_Water_Height:', scc2, 'p-value:', sp2)
