import pymongo
import datetime
import re
import linecache
client = pymongo.Connection('localhost', 27017)
db = client.tourism_database
database = db.database
w= open('input2.txt','r')
i=0
hill=[]
tourist=[]
beach=[]
hotels=[]
for line in w.readlines():
    i=i+1
    if line=="Tourist places\n":
        input=linecache.getline('input2.txt',i+1).strip('0123456789.\n').split("-")     
        tourist.append(input[0])
    elif line=="Hill stations\n":
        state=linecache.getline('input2.txt',i+1).replace(":-",",").strip('.\n')
        hill.append(state.split(","))
    elif line=="Beach\n":
        beaches=linecache.getline('input2.txt',i+1).strip('.\n')
        beach.append(beaches)
    elif line=="hotels\n":
        hotel=linecache.getline('input2.txt',i+1).strip('.\n').split("-")
        hotels.append(hotel)
for j in range(len(hotels)):
    post={'Type':'Hotels','Place':hotels[j][0],'Name':hotels[j][1]}
    database.insert(post)
for j in range(len(hill)):
    for x in range(1,len(hill[j])):
        post={'Type':'HillStation','State':hill[j][0],'Name':hill[j][x]}
        database.insert(post)
for j in range(len(tourist)):	
	post={'Type':'Tourist','Name':tourist[j]}
	database.insert(post)
for j in range(len(beach)):	
	post={'Type':'Beaches','Name':beach[j]}
	database.insert(post)

