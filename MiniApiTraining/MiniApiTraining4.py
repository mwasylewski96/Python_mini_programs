"""
API - Application Programming Interface 
"""
import requests

#Program pobierający wybrana przez użytkownika liczbe losowych faktów o kotach
print("Ile wyświetlić faktów o kotach? (max = 500)")
howmany = input()
params = {"amount": howmany, "animal_type": "cat"}
r = requests.get("https://cat-fact.herokuapp.com/facts/random",params)

def WritingCatFacts():
    counter = 1
    dataCats = r.json()
    for datafact in dataCats:
        for eachfact in datafact:
            if eachfact == "text":
                print("Fakt nr:",counter,":", datafact[eachfact])
                counter += 1

WritingCatFacts()
