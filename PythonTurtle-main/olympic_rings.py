from turtle import *

speed(0)
setup(800,500)
pensize(12)

#blaclring
pencolor("black")
circle(80)

#Bluering
penup()
goto(-200,0)
color("blue")
pendown()
circle(80)

#redring
penup()
goto(200,0)
color("red")
pendown()
circle(80)


#yelloring
penup()
goto(-100,-100)
color("yellow")
pendown()
circle(80)

#greenring
penup()
goto(100,-100)
color("green")
pendown()
circle(80)
