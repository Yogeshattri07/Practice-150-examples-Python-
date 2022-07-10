import random
num=random.randint(1,5)
guess=int(input("enter your number :"))
if num==guess :
    print("well done")
elif guess>num :
    print("too high")    
    guess=int(input("enter a second number:"))
    if guess=="num":
     print("correct")
    else:
     print("you lose")    
elif guess<num :
    print("too low")    
    guess=int(input("enter a second number:"))
    if guess=="num":
     print("correct")
    else:
     print("you lose")    