liczba = input("Podaj liczbę całkowitą ")
liczba = int(liczba)
if liczba < 10 or liczba > 15:
    print("Liczba nie jest z odpowiedniego przedziału")
# możemy również sprawdzić warunek zawierania się elementu w kolekcji
zbior_dopuszczalny = [1, 3, 5, 7, 9]
if liczba not in zbior_dopuszczalny:
    print("Podana liczba nie znajduje się w zbiorze")