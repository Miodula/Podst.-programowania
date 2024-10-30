import math
x1 = (input("Podaj x1: "))
y1 = (input("Podaj y1: "))
x2 = (input("Podaj x2: "))
y2 = (input("Podaj y2: "))

lista1 = [x1, y1]
lista2 = [x2, y2]

def sprawdz(lista1, lista2):
    if isinstance(lista1, list) and isinstance(lista2, list) and lista1[0].isnumeric() and lista1[1].isnumeric() and lista2[0].isnumeric() and lista2[1].isnumeric():
        return True
    else:
        return False
def pokaz(lista1, lista2):
    if sprawdz(lista1, lista2):
        zmienna = (int(lista2[0])-int(lista1[0])**2)+(int(lista2[1])-int(lista1[1])**2)
        print(zmienna)
        wynik = math.sqrt()
        print(wynik)
    else:
        print("False1")

pokaz(lista1, lista2)
