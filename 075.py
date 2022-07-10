num=[101,102,103,104]
for i in num:
     print(i)
selection=int(input("input the number :"))
if selection in num:
    print(selection , "is present in the position of ", num.index(selection))
else:
   print("that is not present in the list")    