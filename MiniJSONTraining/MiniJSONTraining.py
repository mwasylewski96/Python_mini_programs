import json
import pprint #Do ladnego wyswietlania
"Mini program zapisujący film do formatu JSON a potem odczytujący plik JSON z powrotem do Pythona"

meczePolskinaMundialach = {
    "mundial_2006" : ("Polska - Ekwador 0-2","Polska - Niemcy 0-1", "Polska - Kostaryka 2-0"),
    "mundial_2010" : None,
    "mundial_2014" : None,
    "mundial_2018" : ("Polska - Senegal 1-2","Polska - Kolumbia 0-3", "Polska - Japonia 1-0")
}
for i in meczePolskinaMundialach:
    print(i, meczePolskinaMundialach[i])

print("")

zakodujwJSONmeczePolskinaMundialach = json.dumps(meczePolskinaMundialach, ensure_ascii=False)

with open("Polska Na mundialach w XX wieku.json", "w", encoding="UTF-8") as plik:
    plik.write(zakodujwJSONmeczePolskinaMundialach)

with open("Polska Na mundialach w XX wieku.json", encoding="UTF-8") as plik:
    odczytywanieJSONMeczePolskinaMundialach = json.load(plik)

odczytywanieJSONMeczePolskinaMundialach["mundial_2006"] = tuple(odczytywanieJSONMeczePolskinaMundialach["mundial_2006"])
odczytywanieJSONMeczePolskinaMundialach["mundial_2018"] = tuple(odczytywanieJSONMeczePolskinaMundialach["mundial_2006"])


# for line in odczytywanieJSONMeczePolskinaMundialach:
#     print(line, odczytywanieJSONMeczePolskinaMundialach[line])
pprint.pprint(odczytywanieJSONMeczePolskinaMundialach)

