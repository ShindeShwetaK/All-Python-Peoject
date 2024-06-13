from turtle import *
from random import randint

#Pagesetup
setup(800,500)
speed(0)
bgcolor("black")

def star():
    color("yellow")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()

def starB():
    color("gold")
    begin_fill()
    for i in range(5):
        forward(20)
        right(144)
    end_fill()

#Draw random stars at random location
for i in range(50):
    x=randint(-300,300)
    y=randint(-250,250)
    star()
    penup()
    goto(x,y)
    pendown()

for i in range(20):
    x=randint(-400,400)
    y=randint(-200,200)
    starB()
    penup()
    goto(x,y)
    pendown()

#moon1
penup()
goto(-300,100)
pendown()
color("seashell")
begin_fill()
circle(50)
end_fill()

#moon2
penup()
goto(-280,100)
pendown()
color("black")
begin_fill()
circle(50)
end_fill()


