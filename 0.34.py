print("1) square")
print("2) Triangle")
print()
num=int(input("enter a number :"))
if num==1:
    side=int(input("enter the side :"))
    area=side*side
    print("area of circle is :" , area)
elif num==2:
    base=int(input("enter the base of a triangle:"))
    height=int(input("enter the height of a triangle:"))
    area=base*height//2
    print("print area of a triangle :", area)
else:
    print("error occur")    

    
        