def Treasure_Island():
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure")
    print("You are at a crossroad. Where do you want to go? Type left or right")
    left_or_right = input(str())
    if left_or_right.lower() == "left":
        print("You have come to a lake. There is an island in the middle of the lake, Will you swim or wait")
    elif left_or_right.lower()=="right":
        print("Game Over")
        return "You run into a wall, Game Over"
    Swim_Wait=str(input())
    if Swim_Wait == "wait":
        print("You have reached the island , you find multiple doors which door shall you choose, Type 'red', 'blue' or 'yellow' ")
    elif Swim_Wait=="swim":
        print("You actually don't know how to swim and drown, Game Over")
        return "Game Over"
    Door = str(input())
    if Door == "red" or Door=="blue":
        print('Game Over')
        return "Game Over"
    elif Door.lower() == "yellow":
        print("You Win")
        return "You win"
Treasure_Island()
    
