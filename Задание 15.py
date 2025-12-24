#Задание 1
from turtle import *

speed(10)
for x in range(4):
    forward(150)
    left(90)
done()

#Задание 2
from turtle import *

speed(10)
goto(200, 0)
goto(200, 150)
goto(0, 0)
done()

#Задание 3
from turtle import *

speed(10)
color("white")
bgcolor("green")
for x in range(360):
    forward(1)
    left(1)
done()

#Задание 4
from turtle import *

right(310)
speed(10)
right(90)
circle(120, 90)
left(90)
circle(120, 90)
done()
