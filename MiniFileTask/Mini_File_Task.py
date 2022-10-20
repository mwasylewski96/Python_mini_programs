with open("names_and_surnames.txt", "r", encoding="UTF-8") as file:
    readfile = file.readlines()
SeparatedElements = []
for line in readfile:
    temp = line.replace("\n", "")
    SeparatedElements.append(temp.split(" "))
print(SeparatedElements)
SeparatedNames = [i[0] for i in SeparatedElements]
SeparatedSurnames = [i[1] for i in SeparatedElements]
with open("Names.txt", "w", encoding="UTF-8") as file:
    for name in SeparatedNames:
        file.write(name)
        file.write("\n")
with open("Surnames.txt", "w", encoding="UTF-8") as file:
    for surname in SeparatedSurnames:
        file.write(surname)
        file.write("\n")
