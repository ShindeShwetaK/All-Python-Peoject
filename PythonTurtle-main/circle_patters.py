# Write your code here :-)
from turtle import *

speed(20)
bgcolor("black")

colors=["blue","red","orange","green","white","yellow","pink"]

for i in range(200):
    pencolor(colors[i%7])
    width(i/250)
    circle(i)
    left(59)
