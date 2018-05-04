"""
Created on 4/30/18

@author: Jingchao Yang
"""
import dataPrepro
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import correlation

"""Regression model regarding simple time series"""
# model = sm.OLS(dataPrepro.equakeList, dataPrepro.tsuList).fit()
# sumy = model.summary()
# print(sumy)
#
# plt.scatter(dataPrepro.equakeList, dataPrepro.tsuList)
# plt.xlabel("Earthquake")
# plt.ylabel("Tsu")
#
# npEquake = np.array(dataPrepro.equakeList)
# lr = LinearRegression()
# lr.fit(npEquake.reshape(-1, 1), dataPrepro.tsuList)
#
# y_pred = lr.predict(npEquake.reshape(-1, 1))
# plt.plot(npEquake, y_pred, color='red')
#
# plt.show()

"""Regression model regarding earthquakes that cause tsunamis
Model for earthquake surface magnitude earthquake forcal depth 
and tsunami maxWaterHeight
"""
# earthquake land surface magnitude with tsu maxWaterHeightFilter
model = sm.OLS(correlation.surMagFilter, correlation.maxWaterHeightFilter).fit()
sumy = model.summary()
print(sumy)

plt.subplot(211)
plt.scatter(correlation.surMagFilter, correlation.maxWaterHeightFilter)
plt.title("Linear Regression")
plt.xlabel("Surface Magnitude")
plt.ylabel("Tsu Max Water Height")

npMS = np.array(correlation.surMagFilter)
lr = LinearRegression()
lr.fit(npMS.reshape(-1, 1), correlation.maxWaterHeightFilter)

y_pred = lr.predict(npMS.reshape(-1, 1))
plt.plot(npMS, y_pred, color='red')

# earthquake forcal depth with tsu maxWaterHeightFilter
model2 = sm.OLS(correlation.fodepFilter, correlation.maxWaterHeightFilter).fit()
sumy2 = model2.summary()
print(sumy2)

plt.subplot(212)
plt.scatter(correlation.fodepFilter, correlation.maxWaterHeightFilter)
plt.xlabel("Forcal Depth")
plt.ylabel("Tsu Max Water Height")

npFD = np.array(correlation.fodepFilter)
lr2 = LinearRegression()
lr2.fit(npFD.reshape(-1, 1), correlation.maxWaterHeightFilter)

y_pred2 = lr2.predict(npFD.reshape(-1, 1))
plt.plot(npFD, y_pred2, color='red')

plt.show()