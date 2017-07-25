from turtle import *

penup()
goto(120,30)
pendown()
color(0.9,0.3,0.7)
pensize(2)

for i in range(5):
    penup()
    right(144)
    forward(350)
    pendown()
    for _ in range(5):
        right(144)
        forward(100)
    
    
