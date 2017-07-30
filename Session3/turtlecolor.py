from turtle import *

colors = ["red","blue","brown","yellow","grey"]
for p in range (7,1,-1):
    for _ in range (p):
        forward(100)
        left(360/p)
        for i in list (colors):
            color(i)
    
##not yet finished, still in working
