# Napisz funkcje ktora przyjmuje jeden argument, oblicza wartość bezwzględną liczby i zwraca ją z funkcji.
liczba = int(input("podaj liczbe: "))
def bezwzgledna(liczba):
    if liczba <0:
        liczba = (liczba*(-1))
    return (liczba)
print(bezwzgledna(liczba)) 

