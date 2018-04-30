"""
Created on 4/29/18

@author: YJccccc
"""
import pandas as pd

class EventObj:
    year = 0
    cont = 0

    def change_year(self, new_year):
        self.year = new_year

    def contEvent(self):
        self.cont += 1

def contEventByYear(year):
    years, eventObjs = [], []
    for i in year:
        if i in years:
            for j in eventObjs:
                if j.year == i:
                    j.contEvent()

        else:
            years.append(i)
            e = EventObj()
            e.year = i
            e.contEvent()
            eventObjs.append(e)

    # for k in eventObjs:
    #     print(k.year, k.cont)
    return eventObjs

earthquake = pd.read_csv('Data/signif1900.csv')
eYear = earthquake['YEAR']
earthquakeEvent = contEventByYear(eYear)

tsu = pd.read_csv('Data/tsevent1900.csv', encoding = "ISO-8859-1")
sYear = tsu['YEAR']
TsuEvent = contEventByYear(sYear)
# print(len(earthquakeEvent),len(TsuEvent))

equakeList, tsuList = [],[]
for i in range(len(earthquakeEvent)):
    equakeList.append(earthquakeEvent[i].cont)
    tsuList.append(TsuEvent[i].cont)

timeLine = list(range(1900,2019))