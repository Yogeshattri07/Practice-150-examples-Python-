file=open("names.txt","a")

newname=input("enter a new name :")
file.write(newname +"\n")
file=open("names.txt","r")
print(file.read())


file.close()