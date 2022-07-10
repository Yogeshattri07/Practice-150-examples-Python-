num=int(input("enter a number between 10 and 20 :"))
while num<10 or num>20:
    if num<10:
        print("too low")
    else:
        print("too high")
    num=int(input("try again"))
print("thank you")    