list=[]
for i in range(0,4):
    name=input("enter your name :")
    age=int(input("enter your age :"))
    size=int(input("enter your shoe size :"))
    list[name] = { 
        "AGE":age ,"SHOE SIZE" :  size  }
ask=input("enter a name :")
print(list[ask])

