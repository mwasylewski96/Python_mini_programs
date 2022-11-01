"""
API - Application Programming Interface 
"""
import json.decoder
import requests
from pprint import pprint
import webbrowser
params = {"api_key": "3a88aeb23ef11e070e3749574bda14edad374dde", "country" : "pl", "year" : 2019, "month": 12}
r = requests.get("https://calendarific.com/api/v2/holidays",params)
try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
finally:
    #for each in content["response"]:
    for i in content["response"]["holidays"]:
        print(i["name"],">>>>", i["date"]["datetime"])

