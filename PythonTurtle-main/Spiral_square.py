from turtle import *

bgcolor("black")
speed(10)
pensize(3)

for i in range(5):
    for colors in["crimson","hotpink","orangered","lawngreen","aqua","azure","peru"]:
       color(colors)
       left(12)
       for i in range(4):
          forward(200)
          left(90)

