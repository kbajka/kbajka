from tkinter import *
def pAdzialanie():
    print("Dziekuje")
def pBdzialanie():
    print("Nie naciskaj")
okno = Tk()
przyciskA=Button(okno, text="Nacisnij mnie", command=pAdzialanie)
przyciskB=Button(okno, text="Nie",           command=pBdzialanie)
przyciskA.pack()
przyciskB.pack()
okno.mainloop()
