from array import *
nums=array("i",[ ])
for i in range(0,5):
    num=int(input("enter a number :"))
    nums.append(num)
nums=sorted(nums)
for i in nums:
    print(i)

num=int(input("enter a number from array you want to remove  :"))    
if num in nums:
  nums.remove(num)
  
  num2=array("i",[])
  num2.append(num)
  print(nums)
  print(num2)
else:
    print("not an array ")  