# Napisz funkcję która sprawdzi czy liczba jest liczbą pierwszą i zwróci wratość ligiczną True lub false 
liczba = int(input("podaj liczbe: "))
def prime(liczba):
    if liczba == 1:
        return False
    for x in range(2, liczba):
        if liczba % x == 0:
            return False
    return True
    
print(prime(liczba))
            

