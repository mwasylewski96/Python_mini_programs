import json
import requests
import pprint
import webbrowser
from datetime import datetime, timedelta
"""
API - Application Programming Interface 
"""
#time stamp - znak czasu
# 1 stycznia 1970
# w sekundach

#mini malnie 7 punktów
#posegregowane malejąco
#z ostatniego tygodnia
#kategorii python

timeBefore = timedelta(days=7)
searchDate = datetime.today() - timeBefore
searchDate = int(searchDate.timestamp())

params = {"site": "stackoverflow", "sort": "votes", "order": "desc", "fromdate" : searchDate, "tagged": "python", "min": 7}
r = requests.get("https://api.stackexchange.com/2.3/questions", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])