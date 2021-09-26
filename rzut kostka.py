from tkinter import *
from random import randint
def rzut():
    tekst.delete(1.0, END)
    tekst.insert(END, str(randint(1,6000)))
okno = Tk()
tekst=Text(okno, width=10, height=2)
przyciskA = Button(okno, text="Nacisnij aby rzucic", command=rzut)
tekst.pack()
przyciskA.pack()
okno.mainloop()