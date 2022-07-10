name=input("enter your name :")
count=0
name=name.lower()
for x in name:
    if x=="a"or x=="e" or x=="i" or x=="o" or x=="u" :
        count=count + 1
        print("vowels are " , count)
