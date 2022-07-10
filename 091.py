from array import *
num=array("i",[5,4,3,3,2])
print(num)
for i in num:
    print(i)
ask=int(input("enter one number from the array :"))
num1=num.count(ask)
print(num1)