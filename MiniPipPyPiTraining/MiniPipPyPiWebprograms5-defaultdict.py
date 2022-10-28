from collections import defaultdict
ListExpression = ["word "+str(i) for i in range(10) if i ** 3 < 60]
SomeDefaultDictionary = defaultdict(int)
counter = 0

for EachElement in ListExpression:
    SomeDefaultDictionary[EachElement] += counter
    counter += 1

for i in SomeDefaultDictionary:
    print(i,":",SomeDefaultDictionary[i])

#defaultdict przypisuje kluczowi typu int domyslnie wartosc zero, można potem ją latwo zmienic
#Przydaje sie zeby tworząc slownik nie uzywac konstrukcji try except