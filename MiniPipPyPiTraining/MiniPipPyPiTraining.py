import requests
strona = requests.get("https://blog.home.pl/2020/07/strona-www-mala-firma-co-powinna-zawierac/")
# wynik 404 to error nie ma takiej strony
# wynik 200 to wszystko ok, jest taka strona
# requests.get tak naprawde pobiera zawartosc strony
print(str(strona))
with open("Zawartosc pobranej strony.txt", "w", encoding="UTF-8") as plik:
    plik.write(strona.text)
