import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")
#r = requests.get("https://www.sport.pl/sport-hp/0,0.html")
#tasks = json.loads(r.text)
def count_task_frequency(tasks):
    completedtasksFrequencyByUser = dict()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedtasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedtasksFrequencyByUser[entry["userId"]] = 1
    return completedtasksFrequencyByUser
def users_with_top_completed_tasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTasks = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTasks):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)
    return usersIdWithMaxCompletedAmountOfTasks
# get_keys_with_top_values przydstna funkcja na przyszlosc
def get_keys_with_top_values(my_dict):
    [key for key, value in my_dict.items() if value == max(my_dict.values())]
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = users_with_top_completed_tasks(completedTaskFrequencyByUser)
"""
# sposob 1
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()
for user in users:
    print(usersWithTopCompletedTasks)
    if (user["id"] in usersWithTopCompletedTasks):
        print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownika o imieniu:", user["id"])
        usersWithTopCompletedTasks.remove(user["id"])
"""
# sposob 2
for userId in usersWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o imieniu: ", user[0]["name"])

# sposob 3
