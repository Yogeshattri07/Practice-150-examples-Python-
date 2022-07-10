from array import *
num=array("i",[ ])

while len(num)<5:
    nums=int(input("enter a number between 10 and 20 :"))
    if nums >=10 and nums <=20 :
        num.append(nums)
        print(num)
    else:
        print("outside the range")    
for i in num:
    print(i)        
