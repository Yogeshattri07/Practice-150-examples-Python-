word=input("enter a pig latin word :")
first=word[0]
length=len(word)
rest=word[1:length]
if first != "a" and first !="e" and first != "i" and first !="o" or first !="u" :
    new_word=rest + first +"ay"
    print(new_word)

else:
    new=word + "way" 
    print(word.lower())


