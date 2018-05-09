"""
Created on 4/30/18

@author: Jingchao Yang
"""
import dataPrepro
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt
import dataFilter
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


# """Regression model regarding simple tsunami event counts
# by earthquake surface magnitude and focal depth
# """
# plt.subplot(211)
# plt.scatter(correlation.msX, correlation.msY)
# plt.title("Linear Regression")
# plt.xlabel("Surface Magnitude")
# plt.ylabel("Tsu Event_Count")
#
# npMS = np.array(correlation.msX)
# lr = LinearRegression()
# lr.fit(npMS.reshape(-1, 1), correlation.msY)
#
# y_pred = lr.predict(npMS.reshape(-1, 1))
# plt.plot(npMS, y_pred, color='red')
#
# ###################################
# plt.subplot(212)
# plt.scatter(correlation.fdX, correlation.fdY)
# plt.xlabel("Forcal Depth (km)")
# plt.ylabel("Tsu Event_Count")
#
# npFD = np.array(correlation.fdX)
# lr2 = LinearRegression()
# lr2.fit(npFD.reshape(-1, 1), correlation.fdY)
#
# y_pred2 = lr2.predict(npFD.reshape(-1, 1))
# plt.plot(npFD, y_pred2, color='red')
#
#
#
# plt.show()


"""Regression model regarding tsunami MWH Avg
by earthquake surface magnitude and focal depth
"""
plt.subplot(211)
plt.scatter(correlation.ms_mwhX, correlation.ms_mwhY)
plt.title("Linear Regression")
plt.xlabel("Surface Magnitude")
plt.ylabel("Max Water Height Avg (m)")

npMS = np.array(correlation.ms_mwhX)
# print OLS model for linear regression
smConstant = sm.add_constant(npMS)
model = sm.OLS(correlation.ms_mwhY, smConstant).fit()
sumy = model.summary()
print(sumy)

lr = LinearRegression()
lr.fit(npMS.reshape(-1, 1), correlation.ms_mwhY)

y_pred = lr.predict(npMS.reshape(-1, 1))
plt.plot(npMS, y_pred, color='red')

###################################
plt.subplot(212)
plt.scatter(correlation.fd_mwhX, correlation.fd_mwhY)
plt.xlabel("Forcal Depth (km)")
plt.ylabel("Max Water Height Avg (m)")

npFD = np.array(correlation.fd_mwhX)
# print OLS model for linear regression
fdConstant = sm.add_constant(npFD)
model2 = sm.OLS(correlation.fd_mwhY, fdConstant).fit()
sumy2 = model2.summary()
print(sumy2)

lr2 = LinearRegression()
lr2.fit(npFD.reshape(-1, 1), correlation.fd_mwhY)

y_pred2 = lr2.predict(npFD.reshape(-1, 1))
plt.plot(npFD, y_pred2, color='red')

plt.show()

"""Regression model regarding earthquakes that cause tsunamis
Model for earthquake surface magnitude earthquake forcal depth 
and tsunami maxWaterHeight
"""
# # earthquake land surface magnitude with tsu maxWaterHeightFilter
# npMS = np.array(dataFilter.surMagFilter)
# npWH = np.array(dataFilter.maxWaterHeightFilter)
#
# smConstant = sm.add_constant(npMS)
# model = sm.OLS(npWH, smConstant).fit()
# sumy = model.summary()
# print(sumy)
#
# plt.subplot(211)
# plt.scatter(npMS, npWH)
# plt.title("Linear Regression")
# plt.xlabel("Surface Magnitude")
# plt.ylabel("Tsu Max Water Height (m)")
#
# lr = LinearRegression()
# lr.fit(npMS.reshape(-1, 1), npWH)
#
# y_pred = lr.predict(npMS.reshape(-1, 1))
# plt.plot(npMS, y_pred, color='red')
#
# # earthquake forcal depth with tsu maxWaterHeightFilter
# npFD = np.array(dataFilter.fodepFilter)
#
# fdConstant = sm.add_constant(npFD)
# model2 = sm.OLS(npWH, fdConstant).fit()
# sumy2 = model2.summary()
# print(sumy2)
#
# plt.subplot(212)
# plt.scatter(npFD, npWH)
# plt.xlabel("Forcal Depth (km)")
# plt.ylabel("Tsu Max Water Height (m)")
#
# lr2 = LinearRegression()
# lr2.fit(npFD.reshape(-1, 1), npWH)
#
# y_pred2 = lr2.predict(npFD.reshape(-1, 1))
# plt.plot(npFD, y_pred2, color='red')
#
# plt.show()
