import json
import pesel

dictionary = {}

try:
    with open("dane-studentow.txt") as file:
        dictionary = json.load(file)
except FileNotFoundError:
        print("Nie ma takiego pliku :(")



while 1>0:
    print(f"\n1 - Dodaj nowego studenta ")
    print(f"2 - Edytuj dane studenta")
    print(f"3 - Usuń studenta")
    print(f"4 - Wyświetl studenta")
    print(f"5 - Wyjście")
    choice = int(input("Your choice: "))
    
    if choice == 1:
        pesel = input("Podaj numer pesel: ")
        name = input("Podaj imie: ")
        surname = input("Podaj nazwisko: ")
        location = input("Podaj lokalizacje: ")
        indeks = input("Podaj indeks studenta: ")
        student1 = {
            "pesel": pesel,
            "name": name,
            "surname": surname,
            "location": location
        }
        dictionary[indeks] = student1
    elif choice == 2:
        indeks = input("Podaj numer indeksu studenta: ")
        if indeks in dictionary:
            print("1 - Edytuj pesel studenta")
            print("2 - Edytuj imie studenta")
            print("3 - Edytuj nazwisko studenta")
            print("4 - Edytuj lokalizacje studenta")
            choice = int(input("Your choice: "))
            
            if choice == 1: 
                dictionary[indeks]["pesel"] = input("Nowy pesel: ")
            
            if choice == 2: 
                dictionary[indeks]["name"] = input("Nowe imie: ")

            if choice == 3:
                dictionary[indeks]["surname"] = input("Nowe nazwisko: ")
            
            if choice == 4:
                dictionary[indeks]["location"] = input("Nowa lokalizacja: ")
        else:
            print("Podaj prawidłowy numer indeksu!!!")
    
    elif choice == 3:
        indeks = input("Podaj numer indeksu studenta, którego chcesz usunąć: ")
        if indeks in dictionary:
            del dictionary[indeks]
            print(f"Student o indeksie {indeks} został usunięty ;)")
        else:
            print("Podaj prawidłowy numer indeksu!!!")

    elif choice == 4:
        indeks = input("Podaj numer indeksu studenta, którego chcesz wyświetlić: ")
        if indeks in dictionary:
            print("Pesel:", dictionary[indeks]["pesel"])
            print("Imie:", dictionary[indeks]["name"])
            print("Nazwisko:", dictionary[indeks]["surname"])
            print("Lokalizacja:", dictionary[indeks]["location"])
            print("Indeks studenta:", indeks)
        else:
            print("Podaj prawidłowy numer indeksu!!!")
    
    elif choice == 5:
        print("Zamknąłeś program :)")
        try:
            with open("dane-studentow.txt", "w") as file:
                json.dump(dictionary, file, indent=4)
        except Exception as e:
            print(f"Wystąpił błąd:{e}")

        break