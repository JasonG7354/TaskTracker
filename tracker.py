
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
statusTask = ["done", "todo", "in-progress"]


cliArgs = len(sys.argv)


for i in sys.argv:
    #This is only when the user adds a task. 
    if i == "add":
        #In other words if there is no data in the JSON file. Then append 1 with properties. 
        if len(data) <= 0:
            idList.append(1)
            data.append({"id" : 1,
                     "description" : sys.argv[2],
                     "status" : "null",
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
                        "status" : "null",
                        "createdAt" : str(currentDateTime),
                        "updatedAt" : "null"})
            print(f"Task added successfully (ID: {y})")
    

#Next this will write that new json data to data.json. 

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)




'''
print (mainList)


InputTask = input('Enter your task:')
InitialTaskList = [InputTask]

addinput = input("Enter your input")
InitialTaskList.append(addinput)

addinput = input("Enter your input")
InitialTaskList.append(addinput)

deleteTask = int(input("Which task would you like to delete?"))

InitialTaskList.pop(deleteTask)

editTask = int(input("Which task would you like to update?"))
editTaskValue = input("Enter your new updated task")
InitialTaskList[editTask] = editTaskValue

print(InitialTaskList)
'''