import random
num=random.randint(1,10)

correct=False
while correct==False:
    guess=int(input("enter your number :"))
    if num==guess:
        correct= True
    elif guess>num:
        print("too high")
    elif guess<num:
        print("too low")    
        

    

