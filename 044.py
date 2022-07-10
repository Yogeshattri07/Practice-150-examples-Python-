invite=int(input("enter the  number of people you want to invite below 10:  " ))
if invite<10:
    for i in range (0,invite):
     name=input("enter your name :" )
    print(name,"has been invited.")
else:
    print("too many people")    