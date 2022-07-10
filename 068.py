import random 
import turtle
lines=random.randint(0,10)
for x in range(0,lines):
    length=random.randint(25,100)
    rotate=random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)
    