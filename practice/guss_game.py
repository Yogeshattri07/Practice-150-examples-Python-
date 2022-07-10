secret_word= "lion"
guess=" "
chance=0
chance_limit=3
out_of_chance= False
while guess!=secret_word and not(out_of_chance):
    if out_of_chance< chance_limit :
      guess=input("enter the word:")
      chance +=1
    else:

      out_of_chance = True 
if out_of_chance:
    print(("you lose"))      
else:
 print("you win!" )

