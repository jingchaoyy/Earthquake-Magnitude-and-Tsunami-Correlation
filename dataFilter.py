"""
Created on 5/1/18

@author: Jingchao Yang
"""
import dataPrepro
import pandas as pd

"""######First part of data filtering, simple selecting data by column name ######"""

allData = dataPrepro.earthquake
# allData = dataPrepro.earthquakeLocationFilter
# print(allData)

# Eliminating all records without FOCAL_DEPTH
filteredData1 = allData[pd.notnull(allData['FOCAL_DEPTH'])]
# Only records with FOCAL_DEPTH and EQ_MAG_MS get collected (useful data)
filteredData = filteredData1[pd.notnull(filteredData1['EQ_MAG_MS'])]
# print("Total data for analysis: ", len(filteredData))

focalDepth = filteredData['FOCAL_DEPTH']  # focalDepth data list
surfaceMagnitude = filteredData['EQ_MAG_MS']  # surfaceMagnitude data list
# print(focalDepth)
# print(surfaceMagnitude)

# Collecting all observed tsu events (by earthquake) in filtered data
tsuOnly = filteredData[pd.notnull(filteredData['FLAG_TSUNAMI'])]
# print("Total observed: ",len(tsu))

oriTsu = filteredData['FLAG_TSUNAMI']
tsu0 = oriTsu.fillna(0)  # fill all NaN with 0, meaning no Tsu
tsu = tsu0.replace('Tsu', 1)  # replacing 'Tsu' to 1, and generate new tsunami data list
# print(tsu)

# concat all three columns to create a new panda df
# https://stackoverflow.com/questions/20017236/join-three-pandas-data-frames-into-one
merge = pd.concat([focalDepth, surfaceMagnitude, tsu], axis=1)

# print(merge)

# create new csv with filtered data, ready for further analysis
# merge.to_csv('Data/filteredLocation.csv', encoding='utf-8', index=False)


"""###### Second part of data filtering, applying table join ######"""


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


tsuWithEarthquake = tsuOnly
tsuWithEarthquakeDatelist = eventList(tsuWithEarthquake)
# print(tsuWithEarthquakeDatelist[0])

# getting all tsu data from data pre-processing import
allTsu = dataPrepro.tsu
allTsuDateList = eventList(allTsu)
# print(allTsuDateList[0])


'''similar to join table function in ArcGIS, based on data and hour of 
earthquake and tsunami events from two seperate tables
'''
maxWaterHeight = []
for i in tsuWithEarthquakeDatelist:
    for j in allTsuDateList:
        if i == j:  # when date matches, output corresponding MAXIMUM_WATER_HEIGHT
            mwh = allTsu['MAXIMUM_WATER_HEIGHT'][allTsuDateList.index(j)]
            maxWaterHeight.append(mwh)

# convert pandas data frame to regular list
surMag = tsuWithEarthquake['EQ_MAG_MS'].values.tolist()
fodep = tsuWithEarthquake['FOCAL_DEPTH'].values.tolist()

# final filtered data sets
maxWaterHeightFilter, surMagFilter, fodepFilter = [], [], []
for k in range(len(maxWaterHeight)):
    if str(maxWaterHeight[k]) != 'nan':  # filtering nan data
        maxWaterHeightFilter.append(maxWaterHeight[k])
        surMagFilter.append(surMag[k])
        fodepFilter.append(fodep[k])

print("total records after filtering:", len(maxWaterHeightFilter), len(surMagFilter), len(fodepFilter))

'''create csv including final filtered data for correlation analysis
including surface magnitude, focal depth from earthquake tabke,
and max water height from tsu table
'''
surMagFilterpd = pd.DataFrame(surMagFilter)  # convert list to pandas df
fodepFilterpd = pd.DataFrame(fodepFilter)
maxWaterHeightFilterpd = pd.DataFrame(maxWaterHeightFilter)
merge = pd.concat([surMagFilterpd, fodepFilterpd, maxWaterHeightFilterpd], axis=1)
# merge.to_csv('Data/dataCleanedForAnalysis.csv', encoding='utf-8', index=False)
