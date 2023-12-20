import turtle
from turtle import *

width(4)
bgcolor("black")
color("white")

def penrose_triangle():
    up()
    right(90)
    forward(40)
    right(90)
    forward(60)
    right(180)

    for i in range(3):
        if i == 0:
            color("blue")
            fillcolor("blue")
        if i == 1:
            color("pink")
            fillcolor("pink")
        if i == 2:
            color("gold")
            fillcolor("gold")

        begin_fill()
        down()
        forward(120)
        left(60)
        forward(20)
        left(60)
        left(60)
        forward(100)
        right(120)
        forward(55)
        left(60)
        forward(20)
        left(120)
        forward(95)
        end_fill()
#Weg zurücklaufen
        up()
        backward(95)
        right(120)
        back(20)
        right(60)
        backward(55)
        left(120)
        backward(100)
        right(60)

#schwarzer Rand
    for i in range(3):
        color("black")
        pensize(8)

        down()
        forward(120)
        left(60)
        forward(20)
        left(120)
        forward(100)
        right(120)
        forward(60)
        left(60)
        forward(20)
        left(120)
        forward(100)
#Weg zurücklaufen
        backward(100)
        right(120)
        backward(20)
        right(60)
        backward(60)
        left(120)
        backward(100)
        right(60)

    up()
    forward(60)
    left(90)
    forward(50)

    turtle.exitonclick()

penrose_triangle()