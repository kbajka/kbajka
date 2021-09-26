from tkinter import *
okno = Tk()
rysunek=Canvas(okno, height=500, width=500)
rysunek.pack()
prostokat1=rysunek.create_rectangle(100,100,300,200)
kwadrat1=rysunek.create_rectangle(30,30,80,80, fill='yellow')
owal1=rysunek.create_oval(100,100,300,200, fill='red')
okrag1=rysunek.create_oval(30,30,80,80, fill='blue')
okno.mainloop()