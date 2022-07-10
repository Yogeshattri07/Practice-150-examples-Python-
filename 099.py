list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row=int(input("enter the value of raw :"))
print(list[row])
col=int(input("enter the value of col you want to display :"))
print(list[row][col])
ask=input("you want to enter new value y/n")
if ask=="y":
    

 newvalue=int(input("enter a new number :"))
 list[row][col]=newvalue
print([list[row]])