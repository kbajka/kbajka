##
##oceny = [1, 2, 3, 4, 5] * 3
##print(oceny)
##
##liczba1 = 1
##liczba2 = 2
##print(liczba1 > liczba2)
##print(liczba1 <= liczba2)
##print(liczba1 == liczba2)
##print(liczba1 != liczba2)
##
### operacje na napisach
##full_name = "Krzysztof" + " " + "Ropiak"
### ale to ?
##spam = "SPAM "
##print(spam)
##
##prawda = True
##falsz = False
##print(prawda and falsz)
##print(prawda or falsz)
##print(not prawda)
##print(not not prawda)
##print(bool(prawda or falsz))
##
##suma = 1 + 2 * 3 / 4
##print(float(suma))
##
##liczba_str = "123"
##liczba = float(liczba_str)
##print(type(liczba))
##print(liczba)

##imie = "Krzysztof"
##nazwisko = "Ropiak"
##### string to tablica znaków więc możemy odwołać się do jej elementów
####print(imie[0])
##### indeks elementu możemy również określać jako pozycja od końca ciągu
####print(imie[-1])
####print(imie[0] + imie[-2] + imie[4:5])
####print(imie + nazwisko[3:])
####print(imie + " " + nazwisko)
##print(imie.count("a"))
##print(imie.lower())
##print(imie)
##print(len(nazwisko))

##print("Używamy wersji Python %i" % 3)
##print("A dokładniej Python %f" % 3.5)
##print("Lubię język {1} oraz {0}".format("Java", "Python"))

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

kr = Osoba("Krzysztof", "Ropiak")
print("Tą osobą jest {0.imie} {0.nazwisko}".format(kr))
