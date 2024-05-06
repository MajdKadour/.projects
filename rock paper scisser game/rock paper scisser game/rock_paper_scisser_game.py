import random


shapes=["""             
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________) """,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
random_namber=random.randint(0,2)
random_shap=shapes[random_namber]

print("welcome to the Rock,paper,scissors game:")
ruls=input("press enter to continue or type (help) for the rules help  ").lower()
if ruls=="help":
    print("""
          **********Rules*********
          1) you choose and the computer chooses
          2) Rock smashes scissors->Rock wins
          3)Scissors cut paper ->scissors win
          4)paper covers Rock ->paper wins
          """)
choice=input("enter your choice(rock,paper,scisser): ").lower()
if choice=="rock":
    print("your choice ")
    print(shapes[0])
    print("computer choice:")
    print(random_shap)
    if random_namber==0:
        print("you draw!")
    elif random_namber==1:
        print("you lose!paper beats rock")
    elif random_namber==2:
        print("you win!rock beats scisser")
            
elif choice=="paper":
    print("you choice")
    print(shapes[1])
    print("computer choice:")
    print(random_shap)
    if random_namber==0:
        print("you win!paper beats rock")
    elif random_namber==1:
        print("you draw")
    elif random_namber==2:
        print("you lose!scisser beats paper")
        
elif choice=="scisser":
    print("You coice")
    print(shapes[2])
    print("computer choice")
    print(radnom_shap)
    if random_namber==0:
        print("you lose!rock beats scisser")
    elif random_namber==1:
        print("you win!sciser beats paper")
    elif radnom_namber==2:
        print("you draw")
        
else:
    print("inviled choice")

