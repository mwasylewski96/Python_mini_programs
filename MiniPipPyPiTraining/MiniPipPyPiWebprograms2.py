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

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = users_with_top_completed_tasks(completedTaskFrequencyByUser)
    print("Wręczamy ciasteczko mistrzunia dyscypliny do uzytkownikow o id:", usersWithTopCompletedTasks)
    print(completedTaskFrequencyByUser)