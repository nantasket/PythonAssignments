import math
import random
import turtle
import time

b = turtle.Turtle()
b.color("blue", "yellow")
b.pensize(5)
b.shape("turtle")
b.speed(5)

def rectangle():
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)


rectangle()
b.color("yellow")
b.circle(20)
b.color("blue")
b.circle(30)

b.forward(100)
b.color("yellow")
b.circle(20)
b.color("blue")
b.circle(30)

b.penup()
b.goto(20, -30)
b.pendown()

b.circle(10)

b.penup()
b.goto(80, -30)
b.pendown()

b.circle(10)

b.penup()
b.goto(45, -50)
b.pendown()

def triangle():
    b.forward(15)
    b.left(120)
    b.forward(15)
    b.left(120)
    b.forward(15)
    b.left(120)

triangle()

b.penup()
b.goto(35, -70)
b.pendown()
b.color("red")
b.right(90)
b.circle(20, 180)

b.penup()
b.goto(-50, 100)

b.done()
