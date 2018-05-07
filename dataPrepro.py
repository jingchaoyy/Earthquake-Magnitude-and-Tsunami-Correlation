"""
Created on 4/29/18

@author: Jingchao Yang
"""
import pandas as pd


class EventObj:
    att = 0
    cont = 0

    def change_att(self, new_att):
        self.att = new_att

    def contEvent(self):
        self.cont += 1


def contEventByAtt(att):
    atts, eventObjs = [], []
    for i in att:
        if i in atts:
            for j in eventObjs:
                if j.att == i:
                    j.contEvent()

        else:
            atts.append(i)
            e = EventObj()
            e.att = i
            e.contEvent()
            eventObjs.append(e)

    # for k in eventObjs:
    #     print(k.year, k.cont)
    return eventObjs


def eventToList(event):
    eventList = []
    for i in range(len(event)):
        eventList.append(event[i].cont)
    return eventList


"""Data read from 1900 to 2018"""

timeLine = list(range(1900, 2019))
# print(timeLine)

earthquake = pd.read_csv('Data/signif1900Outlier.csv')
eYear = earthquake['YEAR']
earthquakeEvent = contEventByAtt(eYear)

tsu = pd.read_csv('Data/tsevent1900Outlier.csv', encoding="ISO-8859-1")
sYear = tsu['YEAR']
TsuEvent = contEventByAtt(sYear)
# print("\nNumber of earthquake events from 1900 to presents",len(earthquakeEvent))
# print("Number of tsunami events from 1900 to presents",len(TsuEvent))

earthquakeLocationFilter = pd.read_csv('Data/signif1900Filtered.csv')
eYearLocationFiltered = earthquakeLocationFilter['YEAR']
earthquakeEventLocationFiltered = contEventByAtt(eYearLocationFiltered)
# print("Number of selected earthquake by location events from 1900 to presents",len(earthquakeEventLocationFiltered))

equakeList = eventToList(earthquakeEvent)
tsuList = eventToList(TsuEvent)
equakeLocationFilteredList = eventToList(earthquakeEventLocationFiltered)

# print("\nNumber of earthquakes from 1900 to presents",equakeList)
# print("\nNumber of tsunamis from 1900 to presents",tsuList)
# # earthquakes that happened close to the shore
# print("\nSelected earthquakes by location from 1900 to presents",equakeLocationFilteredList)
