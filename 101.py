sales={
    "john" : { "n":3056 ,"s":8463 , " e":8441 , "w":2694 },
    "tom": {"n":4832 ,"s":6786 , " e":4737 ,"w":3612},
    "anne": {"n":5239 ,"s":4802 , " e":8520 , "w":1859},
    "fiona": {"n":3904 ,"s":3445 , " e":8821 , "w":2451} }

name=input("enter your name here :")
region=input("enter your region :")
print(sales[name][region])
new_data=int(input("enter new number you want to change :"))
new_data=sales[name][region]
print(sales[name])
