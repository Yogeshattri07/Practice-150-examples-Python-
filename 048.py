

again="y"
total_invite=0
while again=="y" :
    name=input("enter the name you want to invite in the party :")
    print(name, "has been invited to the party.")
    total_invite=total_invite + 1
    again=input("do you want to invite something else ? (y/n) :")
print("you have", total_invite , "coming to the party.")    


