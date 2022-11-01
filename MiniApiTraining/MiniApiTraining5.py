"""
API - Application Programming Interface 
"""
import requests
import webbrowser
params = {"limit": 3}
r = requests.get("https://api.thecatapi.com/v1/images/search?breed_id=acur",params)
dataCats = r.json()
urllist = []
for cat in dataCats:
    print(cat["url"])
    urllist.append(cat["url"])
for url in urllist:
    webbrowser.open(url)

