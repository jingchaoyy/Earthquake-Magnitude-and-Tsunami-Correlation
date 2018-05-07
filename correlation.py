"""
Created on 5/4/18

@author: Jingchao Yang
"""

import dataFilter
import dataPrepro
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import numpy as np


# getting date info for events
def eventList(event):
    year = event['YEAR']
    month = event['MONTH']
    day = event['DAY']
    hour = event['HOUR']
    date = zip(year, month, day, hour)
    dateList = []
    for i in date:
        dateList.append(i)
    return dateList


tsuWithEarthquake = dataFilter.tsuOnly
tsuWithEarthquakeDatelist = eventList(tsuWithEarthquake)
# print(tsuWithEarthquakeDatelist[0])

allTsu = dataPrepro.tsu
allTsuDateList = eventList(allTsu)
# print(allTsuDateList[0])

maxWaterHeight = []
# similar to join table function in ArcGIS
for i in tsuWithEarthquakeDatelist:
    for j in allTsuDateList:
        if i == j:  # when date matches, output corresponding MAXIMUM_WATER_HEIGHT
            mwh = allTsu['MAXIMUM_WATER_HEIGHT'][allTsuDateList.index(j)]
            maxWaterHeight.append(mwh)

# convert pandas data frame to regular list
surMag = tsuWithEarthquake['EQ_MAG_MS'].values.tolist()
fodep = tsuWithEarthquake['FOCAL_DEPTH'].values.tolist()

maxWaterHeightFilter, surMagFilter, fodepFilter = [], [], []
for k in range(len(maxWaterHeight)):
    if str(maxWaterHeight[k]) != 'nan':  # filtering nan data
        maxWaterHeightFilter.append(maxWaterHeight[k])
        surMagFilter.append(surMag[k])
        fodepFilter.append(fodep[k])

print("total records after filtering:", len(maxWaterHeightFilter), len(surMagFilter), len(fodepFilter))

# create csv for knn analysis
surMagFilterpd = pd.DataFrame(surMagFilter)
fodepFilterpd = pd.DataFrame(fodepFilter)
maxWaterHeightFilterpd = pd.DataFrame(maxWaterHeightFilter)
merge = pd.concat([surMagFilterpd, fodepFilterpd, maxWaterHeightFilterpd], axis=1)
# merge.to_csv('Data/dataCleanedForAnalysis.csv', encoding='utf-8', index=False)

"""Time Series Correlation
Getting the pearson cc for time series based event count
"""
tcc1, tp1 = pearsonr(dataPrepro.equakeList, dataPrepro.tsuList)
# cc2, p2 = pearsonr(fodepFilterpd, maxWaterHeightFilterpd)
print('\nPearson cc for all Earthquake and all Tsunami:', tcc1, 'p-value:', tp1)

"""Autocorrelation Coefficients
See plot.py
"""

"""Pearson Correlation
Check if the a tsunami event (using MAXIMUM_WATER_HEIGHT) is
truly correlated to the surface magnitude and focal depth of
an earthquake"""
cc1, p1 = pearsonr(surMagFilterpd, maxWaterHeightFilterpd)
cc2, p2 = pearsonr(fodepFilterpd, maxWaterHeightFilterpd)
print('\nPearson cc for surMagFilterpd and maxWaterHeightFilterpd:', cc1, 'p-value:', p1,
      '\nPearson cc for fodepFilterpd and maxWaterHeightFilterpd:', cc2, 'p-value:', p2)

"""Spearman’s Rank Correlation
Evaluates the monotonic relationship
"""
scc1, sp1 = spearmanr(surMagFilterpd, maxWaterHeightFilterpd)
scc2, sp2 = spearmanr(fodepFilterpd, maxWaterHeightFilterpd)
print('\nSpearman’s rank cc for surMagFilterpd and maxWaterHeightFilterpd:', scc1, 'p-value:', sp1,
      '\nSpearman’s rank cc for fodepFilterpd and maxWaterHeightFilterpd:', scc2, 'p-value:', sp2)

"""Sum MWH"""
dataInterval = np.arange(0, 190, 10)
print(dataInterval)

