# zad2 Napisz funkcje, która przyjmuje jako argumenty wspolczynniki rownania kwadratowego ax^2 + bx + c = 0 i zwraca liste rzeczywistych rozwiazania rownania. Wykorzystaj funckje, aby sprawdzic jej działania dla trezch przypadków (brak rozwiazań, jedno rozwiązanie, dwa rozwiązania) Podpowiedź: Na początku pliku .py zaimportuj moduł math.
import math
value = math.sqrt(121)

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))

def delzero(a, b, c):
    wynik = b**2-4*a*c
    if wynik < 0:
        return 0
    if wynik == 0:
        return 1
    
    if wynik > 0:
        return 2
    


zmienna=delzero(a, b, c)
if zmienna == 0:
    print("Brak rozwiązań")
if zmienna == 1:
    print("Funkcja ma jedno rozwiązanie")
if zmienna == 2:
    print("Funkcja ma dwa rozwiązania")