# zad2 Napisz funkcje, która przyjmuje jako argumenty wspolczynniki rownania kwadratowego ax^2 + bx + c = 0 i zwraca liste rzeczywistych rozwiazania rownania. Wykorzystaj funckje, aby sprawdzic jej działania dla trezch przypadków (brak rozwiazań, jedno rozwiązanie, dwa rozwiązania) Podpowiedź: Na początku pliku .py zaimportuj moduł math.
import math

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))

def delzero(a, b, c):
    wynik = (b**2)-(4*a*c)
    if wynik < 0:
        return []
    elif wynik == 0: 
        x1 = (-b)*(2*a)
        return [x1]
    
    elif wynik > 0:
        x1 = ((-b)-(math.sqrt(wynik))/(2*a))
        x2 = ((-b)+(math.sqrt(wynik))/(2*a))
        return [x1, x2]
    


zmienna=delzero(a, b, c)
if len(zmienna) == 0:
    print("Brak rozwiązań")
elif len(zmienna) == 1:
    print("Funkcja ma jedno rozwiązanie", zmienna[0])
elif len(zmienna) == 2:
    print("Funkcja ma dwa rozwiązania", zmienna[1], zmienna[0])