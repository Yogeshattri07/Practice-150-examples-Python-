


word=input("enter a word here :")
length=len(word)
print(length)
num=1
for x in word:
    position=length-num
    letter=word[position]
    print(letter)
    num=num+1
