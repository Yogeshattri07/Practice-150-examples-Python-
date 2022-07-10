tv=["dna","cartoon", "movies","anime"]
for i in tv:
    print(i)
print()    
add=input("enter another program:")
position=int(input("enter a number between 0 to 3 :"))
tv.insert(position,add)
for i in tv:
    print(i)
