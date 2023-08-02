print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line ??
choice1 = input('You are at a crossroads, where do you want to go ? Type \"left\" or \"right\". \n').lower()

if choice1 == "left":
  print("Congratulations!!! You managed to survive the first level of the game.")
  print("You have arrived at the Great Grand River !! You need to make another careful decision.")
  choice2 = input("Would you like to swim across the river or wait for the Boat? \n").lower()
  if choice2 == "wait":
    print("Congratulations!!! You've made the right choice. You can now proceed to the next level.")
    print("Patience is the Key To Success.")
    print("You have arrived at the other side of the river. You need to make the final choice.")
    print("There are 3 Magical Doors in front of you. Color - Red, Green, Blue. Only one of them will lead you to Treasure. Make your choices very carefully.")
    choice3 = input("Choose which door would you choose? \n").lower()
    if choice3 == "green":
      print("HURRAYYY!!! YOU HAVE FOUND THE TREASURE !!!")
      print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
      print("""
           _       _ _            
    | |     | | |           
  __| | ___ | | | __ _ _ __ 
 / _` |/ _ \| | |/ _` | '__|
| (_| | (_) | | | (_| | |   
 \__,_|\___/|_|_|\__,_|_| 
      """)
      print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
      
    elif choice3 == "red":
      print("Uh Oh!! You got killed in the Forest Fire. GAME OVER!")
    elif choice3 == "blue":
      print("Bummer! You got eaten by Lions. GAME OVER!")
    else:
      print("Wrong Choice. GAME OVER!")
  else:
    print("You got eaten by Aligators. GAME OVER!")  
else:
  print("You got trapped in QuickSand. GAME OVER!")
  
  
