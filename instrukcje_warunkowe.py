liczba1 = 2.01
liczba2 = 2
if liczba1 > liczba2:
    print("Pierwsza liczba jest większa")
elif liczba1 == liczba2:
    print("Liczby są równe")
else:
    print("Druga liczba jest większa")

print("--------")
liczba = (input("Podaj liczbę całkowitą"))
print(type(liczba))

#if type(liczba) != class(int)
#    print("To jest liczba rzeczywista")

liczba = int(liczba)
print(type(liczba))

if liczba < 10:
    print("To dość mała liczba")
elif 9 < liczba < 100: # to jest wersja skrócona warunku
    print("To już całkiem duża liczba")
else:
    print("To musi być wielka liczba")
