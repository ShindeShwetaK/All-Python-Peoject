from turtle import *
bgcolor("Lightyellow")
speed(10)
penup()
#2 Triangle
goto(-330,200)
pensize(5)
color("brown")
fillcolor("blue")
begin_fill()
pendown()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
end_fill()
hideturtle()

penup()
forward(200)
color("salmon")
fillcolor("forestgreen")
begin_fill()
pendown()
for i in range(3):
    left(120)
    forward(100)
end_fill()

#Square
penup()
forward(20)
color("magenta")
pendown()
for i in ['yellow','black','blue','orange']:
    color(i)
    forward(100)
    left(90)

penup()
forward(120)
pendown()
color("red","orange")
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

penup()
forward(120)
pendown()

#Rectangle
for i in ["maroon","green"]:
    color(i)
    forward(200)
    left(90)
    forward(100)
    left(90)



#Kartik<3
penup()
goto(-370,125)
pendown()
color("orangered")
pensize(5)
#K
right(90)
forward(150)
back(75)
left(140)
forward(90)
back(90)
right(90)
forward(110)

color("lime")
penup()
left(30)
forward(20)
left(90)
pendown()
#A
forward(150)
right(150)
forward(160)
back(75)
right(100)
forward(50)

penup()
left(80)
forward(60)
left(90)
forward(100)
left(90)
pendown()
color("yellow")

#R
forward(150)
right(90)
circle(-50,180)
left(130)
forward(70)

penup()
left(50)
forward(60)
pendown()
color("aqua")

#T
left(90)
forward(150)
left(90)
forward(50)
back(90)
left(180)

penup()
forward(30)
pendown()
color("deeppink")

#I
forward(60)
back(30)
right(90)
forward(150)
right(90)
forward(30)
left(180)
forward(60)

penup()
forward(30)
left(90)
forward(150)
pendown()
color("orange")

#K
right(180)
forward(150)
back(75)
left(140)
forward(90)
back(90)
right(90)
forward(110)

#Heart
color("red")
fillcolor("red")
penup()
left(30)
forward(100)
left(150)
pendown()
begin_fill()
forward(120)
circle(-40,230)
circle(40,-220)
left(190)
forward(90)
end_fill()

penup()
goto(-330,-130)
pendown()
color("magenta","cyan")
begin_fill()
circle(90)
end_fill()

penup()
goto(-300,-180)
pendown()
color("cyan","magenta")
begin_fill()
circle(60)
end_fill()

showturtle()
penup()
left(120)
forward(150)
color("gold")
pendown()
begin_fill()
point=1
#Star
while point<5:
    forward(150)
    left(145)
    point=point+1
end_fill()

left(130)
penup()
forward(100)
#left(50)
#forward(50)
color("springgreen")
pendown()

#letter S
circle(-40,-310)
circle(40,-310)

penup()
left(10)
forward(120)
color("firebrick")


#Oval
shape("circle")
fillcolor("Violet")
shapesize(10,5,3)#(length,width,outline)












#letter S
#circle(-30,-170)
#circle(30,-200)# Write your code here :-)
