from tkinter.messagebox import YES


answer=input("please enter is it raining today :")
answer=str.lower(answer)
if answer=="yes" :
    ask=input("is it windy today :")
    ask=str.lower(ask)
    if ask=="yes":
        print("it is too windy for umbrella")
    else:
        print("take an umbrella")
else:
    print("enjoy your day")        

    