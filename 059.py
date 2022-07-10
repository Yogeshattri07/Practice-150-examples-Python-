import random
color=random.choice(["red","blue","green","black","white"])
print(" color:")
guess=True
while guess==True:
    choice=input("enter the color:")
    choice=choice.lower()
    if color==choice:
        print("well done")
        guess=False
    else:
        if color=="red":
            print("red")    
        elif color=="blue":
            print("blue")    
        elif color=="green":
            print("green")    
        elif color=="black":
            print("black")    
        elif color=="white":
            print("white")    


