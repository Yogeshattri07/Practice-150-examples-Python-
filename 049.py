comp_num=50
guess=int(input("enter a number here :"))
count=1
while guess!=50:
    if guess<comp_num:
        print("too low")
    else:
        print("too high")
    count=count+1
    guess=int(input("enter a another number here :"))
print("well done", "you took",count,"attempts")    


