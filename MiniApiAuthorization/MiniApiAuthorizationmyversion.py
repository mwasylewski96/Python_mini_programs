"""
API - Application Programming Interface 
"""
import json
import requests
import Credentials
def get_JSON_request(r):
    try:
        data = r.json()
    except json.JSONDecodeError():
        print("Zly format danych")
    else:
        return data
def get_one_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search", headers=Credentials.headers)
    return get_JSON_request(r)
def get_favourites_cats(userId):
    params = {"sub_id": userId}
    r = requests.get("https://api.thecatapi.com/v1/favourites", params, headers=Credentials.headers)
    return get_JSON_request(r)
def post_choiced_cat(userId, randomowy_kot):
    CatID = {"image_id": randomowy_kot,"sub_id": userId}
    r = requests.post("https://api.thecatapi.com/v1/favourites/", json=CatID, headers=Credentials.headers)
    return

userId = "marsjanix"
name = "Marcin"

print("Witaj:", name)
print("Twoj nick to:", userId)

randomowy_kot = get_one_cat()
print("Witaj! Oto przykładowy kotek:",randomowy_kot[0]["url"])
favourites_cats_status = get_favourites_cats(userId)
def printing_all_cats(favourites_cats_status):
    for cat in favourites_cats_status:
        print(cat)
    return favourites_cats_status
print("Twoje ulubione kotki to:")
printing_all_cats(favourites_cats_status)
print("Czy wylosowany kotek jest ok? Tak/Nie")
choice = input()
if choice.capitalize() == "Tak":
    post_choiced_cat(userId, randomowy_kot[0]["id"])
    print("A więc tego kotka dodam do ulubionych:", randomowy_kot[0]["url"])
else:
    print("Szkoda, że nie :/")