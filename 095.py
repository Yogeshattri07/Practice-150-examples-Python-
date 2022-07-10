from array import *
import math
nums=array('f',[34.75,52.25,69.46,87.74,96.45])
try_again=True
while try_again==True:
    num=int(input("enter a number between 2 and 5 :"))
    if num<2 or num>5 :
        print("incorrect value try again.")
    else:
        try_again=False
for i in range (0,5):
    ans=nums[i]/num
    print(round(ans,2))        


