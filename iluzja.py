import turtle
turtle.speed(1000)
turtle.bgcolor("black")
turtle.width(10)
def linia():
    color("grey")
    fd(800)
    bk(2000)
    fd(1200)
def linie():
    pu()
    goto(-300,300)
    pd()
    for liczba_linii in range(7):
        linia()
        pu()
        rt(90)
        fd(100)
        lt(90)
        pd()
def kratka():
    linie()
    lt(90)
    linie()

def kropki():
    color("white")
    pu()
    goto(-300,300)
    setheading(0)
    for i in range(7):
         for i in range(7):
             dot(20)
             fd(100)
         rt(90)
         fd(100)
         lt(90)
         bk(700)
kratka()
kropki()
dir(turtle)
