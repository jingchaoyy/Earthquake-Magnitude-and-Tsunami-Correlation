"""
Created on 5/1/18

@author: YJccccc
"""
import dataPrepro
import pandas as pd

allData = dataPrepro.earthquake
# print(allData)

# Eliminating all records without FOCAL_DEPTH
filteredData1 = allData[pd.notnull(allData['FOCAL_DEPTH'])]
# Only records with FOCAL_DEPTH and EQ_MAG_MS get collected (useful data)
filteredData = filteredData1[pd.notnull(filteredData1['EQ_MAG_MS'])]
print("Total data for analysis: ",len(filteredData))

focalDepth = filteredData['FOCAL_DEPTH']  # focalDepth data list
surfaceMagnitude = filteredData['EQ_MAG_MS']  # surfaceMagnitude data list
# print(focalDepth)
# print(surfaceMagnitude)

# Collect all observed tsu event in filtered data
tsu = filteredData[pd.notnull(filteredData['FLAG_TSUNAMI'])]
# print("Total observed: ",len(tsu))
