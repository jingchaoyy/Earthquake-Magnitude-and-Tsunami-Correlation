"""
Created on 5/1/18

@author: Jingchao Yang
"""
import dataPrepro
import pandas as pd

allData = dataPrepro.earthquake
# allData = dataPrepro.earthquakeLocationFilter
# print(allData)

# Eliminating all records without FOCAL_DEPTH
filteredData1 = allData[pd.notnull(allData['FOCAL_DEPTH'])]
# Only records with FOCAL_DEPTH and EQ_MAG_MS get collected (useful data)
filteredData = filteredData1[pd.notnull(filteredData1['EQ_MAG_MS'])]
print("Total data for analysis: ", len(filteredData))

focalDepth = filteredData['FOCAL_DEPTH']  # focalDepth data list
surfaceMagnitude = filteredData['EQ_MAG_MS']  # surfaceMagnitude data list
# print(focalDepth)
# print(surfaceMagnitude)

# Collect all observed tsu event in filtered data
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
