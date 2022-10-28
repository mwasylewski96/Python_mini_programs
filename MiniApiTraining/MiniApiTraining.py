import requests
"""
API - Application Programming Interface 
"""

r = requests.get("https://api.chess.com/pub/player/marsjanix/games/2022/10")
data = r.json()

counter = 0

for a in data["games"]:
    for each in a:
        if each == "pgn":
            with open("partia.txt", "w") as file:
                file.write(a[each])
            with open("partia.txt", "r") as file:
                    readfile = file.readlines()
            SeparatedElementsT = []
            for line in readfile:
                temp = line.replace("\n", "")
                SeparatedElementsT.append(temp.split(" "))
            SeparatedElementsT = SeparatedElementsT[5]
            SeparatedElementsT = SeparatedElementsT[1]
            SeparatedElementsT = list(SeparatedElementsT)
            SeparatedElementsT = SeparatedElementsT[1:-2]
            nick = ""
            for letter in SeparatedElementsT:
                nick = nick + letter
            if nick == "marsjanix":
                counter += 1

print("Do tej pory w pazdzierniku na chess.com zagrałem czarnymi",counter, "razy")