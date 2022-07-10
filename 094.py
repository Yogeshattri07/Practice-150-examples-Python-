from array import *
nums=array("i",[1,2,3,4,5])
for i in nums:
    print(i)
num=int(input("select an array from nums :"))
try_again=True
while try_again==True:
    if num in nums:
        print("this is in position", nums.index(num))
        try_again=False
else:
    print("not in array")        
    num=int(input("select an array from nums :"))



