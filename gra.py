from random import *

do_wyboru = ["A","B","C"]
print("Witam w grze A, B, C")
wybór_gracza =  " "
while wybór_gracza not in do_wyboru:
    wybór_gracza = input("Wybierz A, B, C ").upper()
print("wybrałeś",wybór_gracza)
wybór_kom = choice(do_wyboru)
print("Wybralem",wybór_kom)

      
##if != "A","B","c":
##else:
##    print("Nie wybrałes A, B lub C")
    

####if imię == "Ala":
####    print(odpowiedz, imię)
####    or imię == "ala":
####        print("Miło Cię poznać")
##else:
##    print("czesc")
