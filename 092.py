from array import *
import random
num1=array("i",[ ])
for i in range(0,3):
    num2=int(input("enter a number :"))
    num1.append(num2)

num3=array("i",[ ])    
for i in range(0,5):
    num4=random.randint(1,100)
    num3.append(num4)
number=num1+ num3    
number=sorted(number)
for i in number:
    print(i)

