from random import *
from tkinter import *
rozmiar = 1000
okno = Tk()
plotno = Canvas(okno, width = rozmiar, height = rozmiar)
plotno.pack()
while True:
    kolor = choice(['blue', 'orange', 'red', 'yellow'])
    x0 = randint(0, rozmiar)
    y0 = randint(0, rozmiar)
    d = randint(0, rozmiar/5)
    plotno.create_oval(x0, y0, x0+d, y0+d, fill=kolor)
    okno.update()
okno.mainloop()