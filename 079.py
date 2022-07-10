nums=[]
count=0
while count<3:
    num=int(input("enter a number"))
    nums.append(num)
    count=count+1
    print(nums)
last=input("yes or no do you want last number saved")   
if last=="n":
    nums.remove(num)
print(nums)    
