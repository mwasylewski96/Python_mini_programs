import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")
#r = requests.get("https://www.sport.pl/sport-hp/0,0.html")
#tasks = json.loads(r.text)
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszystko ok")
    print(tasks[0])
