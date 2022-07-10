file=open("names.txt","r")
print(file.read())
file.close()
file=open("names.txt","r")
selected_name=input("enter a name from the list:")
selected_name=selected_name +"\n"
for row in file:
    if row!=selected_name:
        file=open("names2.txt","a")
        record=row
        file.write(record)
        file.close()
file.close()        