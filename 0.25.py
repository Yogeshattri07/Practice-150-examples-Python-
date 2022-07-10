name=input("enter your first name :")
length=len(name)
if length<=5:
    surname=input("enter your surname :")
    name=name.upper()
    print(name + surname)
elif length>=5 :
    name=name.lower()
    print(name)
    