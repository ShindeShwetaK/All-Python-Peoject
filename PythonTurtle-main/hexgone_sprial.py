from turtle import *

speed(20)
bgcolor("black")

colors=["lightcoral","mediumvioletred","darkorange","greenyellow","teal","tan","seashell"]

for i in range(360):
    pencolor(colors[i%7])
    width(i/250)
    forword(i)
    left(59)
