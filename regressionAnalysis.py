"""
Created on 4/30/18

@author: YJccccc
"""
import dataPrepro
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt

model = sm.OLS(dataPrepro.equakeList, dataPrepro.tsuList).fit()
sumy = model.summary()
print(sumy)

plt.scatter(dataPrepro.equakeList, dataPrepro.tsuList)
plt.xlabel("Earthquake")
plt.ylabel("Tsu")

npEquake = np.array(dataPrepro.equakeList)
lr = LinearRegression()
lr.fit(npEquake.reshape(-1,1), dataPrepro.tsuList)

y_pred = lr.predict(npEquake.reshape(-1,1))
plt.plot(npEquake, y_pred, color = 'red')

plt.show()