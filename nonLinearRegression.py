"""
Created on 5/7/18

@author: YJccccc
"""
import pandas as pd
import statsmodels.api as sm

"""Simple Non-Linaer Regression Model
Using converted data (ln to all data (ms, fd, mwh))
"""
data = pd.read_csv('Data/dataCleanedForAnalysis_nonLinear1.csv', encoding="ISO-8859-1")
ms = data['ms']
fd = data['fd']
wh = data['wh']

model = sm.OLS(ms, wh).fit()
sumy = model.summary()
print(sumy)

model2 = sm.OLS(fd, wh).fit()
sumy2 = model2.summary()
print(sumy2)
