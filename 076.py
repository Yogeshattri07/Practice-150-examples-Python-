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


