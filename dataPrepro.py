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

# function that differes from contEventByAtt, contEventByAttWithInterval count events by regroup (reclassify) data first
def contEventByAttWithInterval(interval, att):
    eventObjs = []
    for i in att:
        flag = False  # set a flag to check if i satisfy one of objects in the eventObjs list
        if len(eventObjs) > 0:
            for j in eventObjs:
                # for loop, checking if i satisfy one of objects in the eventObjs list
                if int(float(i) * 1000) in range(j.att[0] * 1000, j.att[1] * 1000):
                    j.contEvent()
                    flag = True  # when i satisfies one of objects in the eventObjs list, set the flag to true

            if flag == False:  # create new object and count if i do not satisfy any existing eventObj
                for z in range(len(interval) - 1):
                    if int(float(i) * 1000) in range(interval[z] * 1000, interval[z + 1] * 1000):
                        e = EventObj()
                        e.att = ([interval[z], interval[z + 1]])
                        e.contEvent()
                        eventObjs.append(e)
        else:  # if no event object created in the eventObjectList, create one
            for y in range(len(interval) - 1):
                if int(float(i) * 1000) in range(interval[y] * 1000, interval[y + 1] * 1000):
                    e = EventObj()
                    e.att = ([interval[y], interval[y + 1]])
                    e.contEvent()
                    eventObjs.append(e)

    return eventObjs
