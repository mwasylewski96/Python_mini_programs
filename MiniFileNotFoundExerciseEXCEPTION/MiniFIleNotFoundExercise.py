otwieranie = True
while otwieranie == True:
    print("Podaj nazwe pliku do otwarcia")
    print("Przykładowe pliki do otwarcia:")
    print("plik1.txt")
    print("plik2.txt")
    print("Zakoncz dzialanie programu -> exit")
    openfile = input()
    if openfile == "exit":
        break
    try:
        with open(openfile, "r", encoding="UTF_8") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("Nie ma takiego pliku")
