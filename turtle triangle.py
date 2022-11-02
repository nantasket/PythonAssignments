import math
import random
import turtle
import time

window = turtle.Screen()

b = turtle.Turtle()
b.shape("turtle")
b.color("black")
b.pensize(5)
b.speed(5)

def triangle(edge=100):
    b.forward(edge)
    b.left(120)
    b.forward(edge)
    b.left(120)
    b.forward(edge)
    b.right(120)

triangle()
triangle()
triangle()
b.right(60)
triangle()
triangle()
triangle()

turtle.exitonclick()

