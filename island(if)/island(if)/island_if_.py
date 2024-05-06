print("""
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)

       """)


print("welcome to my island")
print("there are two doors in front of you 🚪a red door and 🚪a blue door")
door_choice=input("which door do ou want to open?(write red or blue)").lower()


if door_choice=="blue":
    print("oops! you choe the crocodile door\ngame over!🐊🐊")
    

elif door_choice=="red":
    print("Graet! now you entered a room")
    print("you found three boxes:🎁 white ,🎁 black,🎁green")
    box_choice=input("which one do you want to open??").lower()
    

    if box_choice=="white":
        print("Oops! you opened a box filled with snakes🐍🐍🐍")
    elif box_choice=="black":
        print("Oops! you opened a box filled with spiders🕷️🕷️🕷️ ")
    elif box_choice=="green":
        print("congratulations! you found the treasure!🪙🪙🪙🪙 ")
    else:
        print("Invalid choice!")
        

else:
    print("Invalid choice!")
    
       
