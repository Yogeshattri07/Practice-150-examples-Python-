name1=input("you want to add 1st name :")
name2=input("you want to add 2nd name :")
name3=input("you want to add 3rd name :")
party=[name1,name2,name3]
add=input("you want to add another name yes or no :")

while add=="y":
    newname=party.append(input("add another name:"))
    add=input("you want to add another name yes or no :")
print("you have",len(party),"coming to the party")    
print(party)
name=input("type one of the name in thr list name  :")
print(name,"is in position",party.index(name),"on the list")
add1=input("you want to invite this  yes or no :")
if add1=="no":
    party.remove(name )
print(party)    

