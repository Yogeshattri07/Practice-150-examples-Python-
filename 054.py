import random
dice=random.choice(["h","t"])
turn= input("enter your choice :")
if dice==turn:
    print("you win")
else:
    print("bad luck")    
if dice=="h":
    print("it was head")    
else :
    print("it was tail")    