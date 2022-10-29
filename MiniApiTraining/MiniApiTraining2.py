import json
import requests
import pprint
"""
API - Application Programming Interface 
"""
#mini malnie 15 punktów
#posegregowane malejąco
#z ostatniego tygodnia
#kategorii python
params = {"site": "stackoverflow", "sort": "votes", "order": "desc", "fromdate" : "2022-10-20", "tagged": "python", "min": 7}
r = requests.get("https://api.stackexchange.com/2.3/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint.pprint(questions)