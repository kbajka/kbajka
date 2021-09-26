from turtle import *
shape("turtle")
color("blue","purple")
def kwadrat():
    begin_fill()
    for bok in range(4):
        fd(100)
        rt(90)
    end_fill()
for liczba_kwadratow in range(5):
    kwadrat()
    rt(72)

