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
        if i == 1:
            color("pink")
        if i == 2:
            color("gold")

        down()
        forward(120)
        left(60)
        forward(20)
        left(60)

        left(60)
        forward(100)
        right(120)
        forward(55)

        up()
        backward(55)
        left(120)
        backward(100)
        right(60)

    forward(60)
    left(90)
    forward(50)

    turtle.exitonclick()

penrose_triangle()







