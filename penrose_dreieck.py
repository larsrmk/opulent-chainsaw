import turtle
from turtle import *


width(4)
bgcolor("black")
def penrose_triangle():
    for i in range(1):
        color("green")
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

    for i in range(1):
        color ("blue")
        right(120)
        forward(20)
        right(60)
        forward(120)
        right(60)
        forward(20)
        right(60)
        forward(120)
        right(120)
        forward(100)
        right(120)
        forward(20)
        right(60)
        forward(60)

    for i in range(1):
        color ("blue")
        left(120)
        forward(100)
        left(120)
        forward(120)
        left(60)
        forward(20)
        left(120)
        forward(100)
        right(120)
        forward(60)

    turtle.exitonclick()


penrose_triangle()







