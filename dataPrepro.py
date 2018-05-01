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

timeLine = list(range(1900,2019))
print(timeLine)

earthquake = pd.read_csv('Data/signif1900.csv')
eYear = earthquake['YEAR']
earthquakeEvent = contEventByYear(eYear)

tsu = pd.read_csv('Data/tsevent1900.csv', encoding = "ISO-8859-1")
sYear = tsu['YEAR']
TsuEvent = contEventByYear(sYear)
print("\nNumber of earthquake events from 1900 to presents",len(earthquakeEvent))
print("Number of tsunami events from 1900 to presents",len(TsuEvent))


earthquakeLocationFilter = pd.read_csv('Data/signif1900Filtered.csv')
eYearLocationFiltered = earthquakeLocationFilter['YEAR']
earthquakeEventLocationFiltered = contEventByYear(eYearLocationFiltered)
print("Number of selected earthquake by location events from 1900 to presents",len(earthquakeEventLocationFiltered))

equakeList, tsuList, equakeLocationFilteredList = [],[],[]
for i in range(len(earthquakeEvent)):
    equakeList.append(earthquakeEvent[i].cont)
    tsuList.append(TsuEvent[i].cont)
    equakeLocationFilteredList.append(earthquakeEventLocationFiltered[i].cont)

print("\nNumber of earthquakes from 1900 to presents",equakeList)
print("\nNumber of tsunamis from 1900 to presents",tsuList)
# earthquakes that happened close to the shore
print("\nSelected earthquakes by location from 1900 to presents",equakeLocationFilteredList)



