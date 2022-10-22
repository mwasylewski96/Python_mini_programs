import time
"""Mierzenie wydajnosci skryptu - 5 pomiarów różnych sposobów"""
print("Podaj liczbe do ktorej mam sumowac:")
a = int(input())
def sumowanie_do_petla(a):
    suma = 0
    for i in range(a+1):
        suma = i + suma
    return suma
def sumowanie_do_znany_wzor(a):
    return int((1+a)*a/2)
def sumowanie_do_wyrazenie_zbioru(a):
    return sum({i for i in range(a+1)})
def sumowanie_do_wyrazenie_listowego(a):
    return sum([i for i in range(a+1)])
def sumowanie_do_wyrazenia_generujacego(a):
    return sum((i for i in range(a+1)))
def finish_timer(start):
    end = time.perf_counter()
    return end - start
def function_performance(a):
    start = time.perf_counter()
    print("Suma wynosi:", a)
    print("Czas sposobu wynosi:", finish_timer(start))
lista_sposobow = [sumowanie_do_petla(a),sumowanie_do_znany_wzor(a),sumowanie_do_wyrazenie_zbioru(a), sumowanie_do_wyrazenie_listowego(a),sumowanie_do_wyrazenia_generujacego(a)]
for sposob in lista_sposobow:
    function_performance(sposob)
"""    
print("Suma wynosi:",sumowanie_do_znany_wzor(a))
print("Suma wynosi:",sumowanie_do_wyrazenie_zbioru(a))
print("Suma wynosi:",sumowanie_do_wyrazenie_listowego(a))
print("Suma wynosi:",sumowanie_do_wyrazenia_generujacego(a))
"""