import math
from turtle import *

def heart_a(k):
    return 15*math.sin(k)**3

def heart_b(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

speed(9000)
pensize(50)
bgcolor("black")

for i in range(9000):
    goto(heart_a(i)*20, heart_b(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()   