from array import *
num=array("i",[])
for i in range(0,5):
    nums=int(input("ask the user to enter a number :"))
    num.append(nums)
    print(num)
num=sorted(num)
num.reverse()
print(num)