import random
import datetime

money = random.randint(1000,10000)
loan = int(0)
while 1>0:
    print("Wyświetl swój stan konta - wpisz 1")
    print("Przelej pieniądze na konto - wpisz 2")
    print("Przelej pieniądze z konta - wpisz 3")
    print("Weź pożyczkę - 4")
    print("Wyjście - 5")
    number = int(input("Co chcesz zrobić?: "))
    
    if number == 1:
        print(f"Twój stan konta to:{money} ZŁ")
    elif number == 2:
        value1 = int(input(f"Podaj wartość przelewu. (Maksymalny przelew na konto to 20000PLN): "))
        if value1 <= 20000 and value1 > 0:
            money = money + value1

    elif number == 3:
        account = int(input(f"Podaj numer konta: "))
        value2 = int(input(f"Podaj wartość przelewu. (Maksymalny przelew z konta to 10000PLN)"))
        if value2 <= 10000 and value2 > 0:
             money = money - value2

    elif number == 4:
        credit = int(input(f"Podaj wartość pożyczki. (Maksymalna wysokość pożyczki to 5000PLN)"))
       
        
        if credit <= 5000 and credit > 0 and loan == 0:
            money = money + credit
            loan = loan + 1 
        elif loan == 1: 
            print("Nie możesz wziąć więcej niż jedną pożyczkę")

    elif number == 5:

        break 

    elif number != range(1,5):
        print("Podaj numer akcji od 1 do 5")

    money != 0 