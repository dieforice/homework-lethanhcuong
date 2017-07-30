from turtle import *

colors=["blue","red","grey","red","blue","brown","yellow","grey"]
for p in range(7,1,-1):
    for i in range(p):
        color(colors[p])
        forward(100)
        left(360/p)
        
        
        
    

