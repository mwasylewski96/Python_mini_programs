# Własny pomysł na program do szukania pracowników którzy zrobili ponad połowę
# wykonanych poprawnie zadań spośród wszystkich zleconych.
# Każdemu pracownikowi dajemy premię 1000 zł
import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")
workers = r.json()

def CreatingDictionaryCompletedTasksForWorkers(workers):
    workers_counting_completed_tasks = dict()
    for worker in workers:
        if worker["completed"] == True:
            try:
                workers_counting_completed_tasks[worker["userId"]] += 1
            except KeyError:
                workers_counting_completed_tasks[worker["userId"]] = 1
    return workers_counting_completed_tasks

def CreatingListOfGoodWorkers(workers_counting_completed_tasks):
    list_of_good_workers = list()
    for each_worker_key, each_worker_value in workers_counting_completed_tasks.items():
        if each_worker_value > 10:
            list_of_good_workers.append(each_worker_key)
    return list_of_good_workers

def ParametersOfWorkersToGetFromJSONPlaceHolder(list_of_good_workers):
    ParameterToRequestForJSON = ""
    lenofworkers = len(list_of_good_workers)
    counterworker = 0
    for one_guy in list_of_good_workers:
        if counterworker != lenofworkers:
            ParameterToRequestForJSON = ParameterToRequestForJSON + "id=" + str(one_guy) + "&"
            counterworker += 1
        if counterworker == lenofworkers:
            ParameterToRequestForJSON = ParameterToRequestForJSON + "id=" + str(one_guy)
    print(ParameterToRequestForJSON)

    return ParameterToRequestForJSON

"MAIN PROGRAM"
workers_counting_completed_tasks = CreatingDictionaryCompletedTasksForWorkers(workers)
list_of_good_workers = CreatingListOfGoodWorkers(workers_counting_completed_tasks)
ParameterToRequestForJSON = ParametersOfWorkersToGetFromJSONPlaceHolder(list_of_good_workers)
r = requests.get("https://jsonplaceholder.typicode.com/users", params=ParameterToRequestForJSON)
goodworkers = r.json()
for each_good_worker in goodworkers:
    print("Premię w postaci 1000 zł wręczamy:",each_good_worker["name"])

