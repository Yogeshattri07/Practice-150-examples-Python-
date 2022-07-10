from array import *
import random

num=array("i",[])

for i in range(0,5):

  nums=random.randint(0,100000000)
  num.append(nums)
  print(num)
for i in num:
    print(i)  

