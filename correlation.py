"""
Created on 5/4/18

@author: Jingchao Yang
"""

import dataFilter
import dataPrepro


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

print(len(maxWaterHeightFilter), len(surMagFilter), len(fodepFilter))

"""Autocorrelation Coefficients
See plot.py
"""

"""Pearson Correlation
Check if the surface magnitude and focal depth of
an earthquake truly correlated to tsunami event (using MAXIMUM_WATER_HEIGHT)"""

"""Effective Sample Size"""
