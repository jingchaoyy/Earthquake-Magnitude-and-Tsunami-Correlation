"""
Created on 5/4/18

@author: Jingchao Yang
"""

import dataFilter
import dataPrepro
import pandas as pd
import scipy.stats


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

"""Autocorrelation Coefficients
See plot.py
"""

"""Pearson Correlation
Check if the surface magnitude and focal depth of
an earthquake truly correlated to tsunami event (using MAXIMUM_WATER_HEIGHT)"""

cc1, p1 = scipy.stats.pearsonr(surMagFilterpd, maxWaterHeightFilterpd)
cc2, p2 = scipy.stats.pearsonr(fodepFilterpd, maxWaterHeightFilterpd)
print('\nPearson cc for surMagFilterpd and maxWaterHeightFilterpd:', cc1, 'p-value:', p1,
      '\nPearson cc for fodepFilterpd and maxWaterHeightFilterpd:', cc2, 'p-value:', p2)

"""Effective Sample Size"""
