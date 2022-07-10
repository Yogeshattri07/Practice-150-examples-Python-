import random
score=0
for i in range(1,6):
    num1=random.randint(1,3)
    num2=random.randint(1,3)
    correct=num1+num2
    print(num1,"+",num2,"= ")
    answer=int(input("enter your answer:"))
    print()
    if answer==correct:
        score+=1
print("you scored",score,"out of 5")        
