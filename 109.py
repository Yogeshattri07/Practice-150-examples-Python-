print("1)  create a new file ")
print("2)  display a new file ")
print("3)  add a new item to a new file ")
selection=int(input("enter your choice 1,2 or 3:"))
if selection==1:
    subject=input("enter a school subject:")
    file=open("subject.txt","w")
    file.write(subject )
    file.close()
elif selection==2:
    file=open("subject.txt","r")
    print(file.read())
elif selection==3:
    file=open("subject.txt","a")
    subject=input("enter a new subject")    
    file.write(subject )
    file.close()
    file=open("subject.txt","r")
    print(file.read())
else:
    print("invalid option")    
    
