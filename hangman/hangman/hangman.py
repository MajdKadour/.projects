
import random
hangman_shapes=["""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
""" 
  +---+
  |   |
  O   |
  |   |
      |
      |
========='""",
"""
 +---+
  |   |
  O   |
 /|   |
      |
      |
========='""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
tries=6

lis_things=["water","milk","judo"]
computer_choice=random.choice(lis_things)

lis_space=["_"]*len (computer_choice)
print("".join(lis_space))

print(lis_space)
print(hangman_shapes[0])
letter=[]

while "_" in lis_space and tries>0:
    person_gus=input("pleas try to guss the letter\n\n")
    if person_gus in letter:   
        print("aer you ediot prother you gussed before")
        print(f"now you have {tries}time")
        continue
    
    letter.append(person_gus)


    if person_gus not in computer_choice:
        
      
        print(f"now your tries is {tries}\n")
        tries=tries-1
        print(hangman_shapes[6-tries])
    else: 
          for x in range(len(computer_choice)):
              if computer_choice[x]==person_gus:
                  lis_space[x]=person_gus
                  print("okk you are amazing that's correc\n")
                  print(lis_space)
    print(f"now you have {tries} time")
                  
if tries==0:
    print(hangman_shapes[6])
    print("you lose game over....loser")
else:
    print("you win bic congraution")
    


            
        
         
        

        
        
        
        
        
    
      
      
      
      
      
      
      
      
      
     