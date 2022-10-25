import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")
#r = requests.get("https://www.sport.pl/sport-hp/0,0.html")
#tasks = json.loads(r.text)
tabledata = r.json()

def creating_dictionary_userId_and_howmanytasks_completed(tabledata):
    userdictionary = dict()
    for i in tabledata:
        if i["completed"] == True:
            try:
                userdictionary[i["userId"]] += 1
            except:
                userdictionary[i["userId"]] = 1
    return userdictionary
def userId_List_With_Low_Tasks_Completed(userdictionary):
    userIdListWithLowTasksCompleted = []
    for j,k in userdictionary.items():
        if k == min(userdictionary.values()):
            userIdListWithLowTasksCompleted.append(j)
    return userIdListWithLowTasksCompleted

userdictionary = creating_dictionary_userId_and_howmanytasks_completed(tabledata)
userIdListWithLowTasksCompleted = userId_List_With_Low_Tasks_Completed(userdictionary)
print("Uzytkownik/cy", userIdListWithLowTasksCompleted,"zrobił/li najmniej zadań")