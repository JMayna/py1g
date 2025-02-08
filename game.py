import random

def new_Game():
     playername, playerclass = character_Creation()
     if playerclass:
         print(f"Welcome {playername}, you have chosen to play as a {playerclass}")

def character_Creation():
   
    playername = input("What is your name? ")
    print(f"Welcome {playername}!") 

    while True:
        classchoice = input("Which class do you choose?\n [1] Fighter\n [2] Mage \n [3] Thief \n")
        if classchoice == "1":
            playerclass = "Fighter"
            HP = 20
            AC = 18
            break  
        elif classchoice == "2":
            playerclass = "Mage"
            HP = 20
            AC = 18
            Mana = 20
            break
        elif classchoice == "3":
            playerclass = "Thief"
            HP = 20
            AC = 18
            Stealth = 20
            break
        else:
            print("Invalid choice: Please choose 1, 2, or 3")
    return  playername, playerclass

    print(f"Welcome {playername}, you have chosen to play as a {playerclass}")  


def quit_Game():
    print("Exiting game!")
    exit()

# Main Menu
while True:
    menuChoice = input("Please choose an option \n [1] New Game\n [2] Exit Game\n")

    if menuChoice == "1":
        new_Game()
        break  
    elif menuChoice == "2":
        quit_Game()  
        break  
    else:
        print("Invalid choice: Please choose 1 or 2")