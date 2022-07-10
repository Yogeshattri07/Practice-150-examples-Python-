num1=int(input("enter a first number :"))
total=num1
again="y"

while again== "y" :
  num2=int(input("enter a second number :"))
  total=total + num2
  again=input("do you want the add another number ? (y/n) :")
print("enter the total : " , total )    