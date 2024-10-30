# zad1 napisz funkcje oblicz(a, b), która przyjmuje dwa argumenty i wypisuje w kolejnych liniach ich: sume, roznice, iloczyn, iloraz, 

one = int(input("Podaj liczbe a: "))
two = int(input("Podaj liczbe b: "))

def add(a, b):
    wynik = a + b
    return wynik 

def difference(a, b):
    wynik = a - b 
    return wynik

def iloczyn(a, b):
    wynik = a * b
    return wynik

def iloraz(a, b):
    wynik = a / b 
    return wynik

def calculation(a, b): 
    print("Suma:", add(one, two))
    print("Różnica:", difference(one, two))
    print("Iloczyn:", iloczyn(one, two))
    if b == 0:
        print("Nie można dzielić przez 0")
        return False
    print("Iloraz:", iloraz(one, two))
   
       
calculation(one, two)

