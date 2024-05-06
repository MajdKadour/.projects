import random

print("welcome to the coin Guessing Game!")
print("choisse a method to toss the coin:")
print("1. using random.random()\n2. using random.randint()")


choice=int(input("please enter your choice 1 or 2"))
guess=input("plase enter your guess (heads or tails)").lower()


if choice==1:
    
    computer_choice=random.random()
    if computer_choice<0.5:
        computer_choice="talis"
     
    else:
        computer_choice="heads"
    
elif choice==2:
    computer_choice=random.randint(1,10)
    if computer_choice<5:
        computer_choice="talis"
        
    else:
        computer_choice="heads"
        
else:
    print("inviled choice")
    
if guess==computer_choice:
    print(f"amazing! you win\ncomputer choice is {computer_choice}")
else:
    print(f"sorry you lost \ncomputer choice is {computer_choice}")
    
    



