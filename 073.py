from re import A


dictionary={ }
food1=input("enter your 1st fav food :")
dictionary[1]=food1
food2=input("enter your 2nd fav food :")
dictionary[2]=food2
food3=input("enter your 3rd fav food :")
dictionary[3]=food3
food4=input("enter your 4th fav food :")
dictionary[4]=food4

print(dictionary)

dislike=int(input("not fav food:"))
del dictionary[dislike]

print(sorted(dictionary.values()))
