from turtle import *

speed(15)
bgcolor("black")
pensize(2)

for i in  range(5):
    for colors in["red","blue","cyan","gold","deeppink","chocolate","white","seagreen"]:
       color(colors)
       circle(100)
       left(10)
