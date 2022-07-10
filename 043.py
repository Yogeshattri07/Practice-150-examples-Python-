direction=input("enter your direction up or down ? (u/d)")
if direction== "u"  :
    num=int(input("enter the top number  " ))
    for i in range(1,num+1):
        print(i)
elif direction=="d":       
    num= int(input("enter the  number below 20 :  " ))
    for i in range( 20, num -1 ,-1):
        print(i)
else:
    print("i don't understand")        



    

