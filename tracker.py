
import sys
import json
import datetime
#This is how I get the current time and date. 
now = datetime.datetime.now()
current_time =now.strftime("%H:%M")
currentDateTime = str(datetime.date.today()) + " " + str(current_time)
#This opens and read the data.json file I have in the same directory. 
with open('data.json', "r") as f:
    data = json.load(f)
#idList is where all the unique IDs in the json file will be listed. 
idList = []
#This is the list of status for each task. 
statusTask = ["todo","done", "in-progress"]


for i in sys.argv:
    #This is only when the user adds a task. 
    if i == "add":
        #In other words if there is no data in the JSON file. Then append 1 with properties. 
        if len(data) <= 0:
            idList.append(1)
            data.append({"id" : 1,
                     "description" : sys.argv[2],
                     "status" : statusTask[0],
                     "createdAt" : str(currentDateTime),
                     "updatedAt" : "null"})
            print(f"Task added successfully (ID: {1})")
        else:    
            x = 0
            y = 1
            #This will extract all ID numbers from json file and put them in a list and sort them in order. 
            while x != len(data):
                id = data[x]["id"]
                idList.append(id)
                x += 1
            idList.sort()
            #The for loop will compare to see which ID number is availble based on idList. 
            for idnum in idList:
                if idnum == y:
                    y += 1
            #Finally this will append it to the data varaible which is the json data.         
            data.append({"id" : y,
                        "description" : sys.argv[2],
                        "status" : statusTask[0],
                        "createdAt" : str(currentDateTime),
                        "updatedAt" : "null"})
            print(f"Task added successfully (ID: {y})")
    #This will find the id that the user wants to update then it will update the description and update time. 
    elif i == "update":
        for unId in data:
            print(unId["id"])
            if unId["id"] == int(sys.argv[2]):
                unId["description"] = sys.argv[3]    
                unId["updatedAt"] = str(currentDateTime)   
    #This will find the id that the user wants to delete. Then it will delete it fomr json  list. 
    elif i == "delete":
        j = 0
        for unId in data:
            if unId["id"] == int(sys.argv[2]):
                del data[j]
            else:
                j += 1
    #This will mark status in progress if it mathces the ID. Mark-done is very similar. 
    elif i == "mark-in-progress":
        j = 0
        for unId in data:
            if unId["id"] == int(sys.argv[2]):
                 unId["status"] = statusTask[2]
            else:
                j += 1
    elif i == "mark-done":
        j = 0
        for unId in data:
            if unId["id"] == int(sys.argv[2]):
                 unId["status"] = statusTask[1]
            else:
                j += 1
    #This will either list all tasks or just list the ones that are done, todo or in-progress. 
    elif i == "list":
        if len(sys.argv) == 2:
            for unId in data:
                print(unId)
        else:
            for unId in data:
                if unId["status"] == sys.argv[2]:
                    print(unId)


                
#Next this will write that new json data to data.json. 

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

