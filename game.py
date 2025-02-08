import random

def new_Game():
     playername, playerclass, HP, AC, Mana, Stealth = character_Creation()
     if playerclass:
         print(f"Welcome {playername}, you have chosen to play as a {playerclass}")
         game_menu(playername, playerclass, HP,AC, Mana, Stealth)

def character_Creation():
   
    playername = input("What is your name? ")
    print(f"Welcome {playername}!")
    
    playerclass = ""
    HP = 0
    AC = 0
    Mana = 0
    Stealth = 0 

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
    return  playername, playerclass, HP, AC, Mana, Stealth

    print(f"Welcome {playername}, you have chosen to play as a {playerclass}")  


def game_menu (playername, playerclass, HP, AC, Mana, Stealth):
    while True:
        playerChoice =  input("What would you like to do: \n [1] Go to next encounter \n [2] View your stats \n [3] Save Game \n [4] Return to Main Menu: \n")
        
        if playerChoice == "1":
            next_encounter()
            break
        elif playerChoice == "2":
            view_stats(playername, playerclass,HP,AC,Mana, Stealth)
            
        elif playerChoice == "3":
            save_game()
            break
        elif playerChoice == "4":
            return_to_main_menu()
            break
        else:
            print("Invalid Choice. Please Choose 1, 2, 3, or 4")
       
def next_encounter():
    pass

def view_stats(playername, playerclass, HP, AC, Mana, Stealth ):
    
    print(f"Name:{playername}\nClass: {playerclass}\nHP: {HP}\nAC: {AC}", end="")
    if Mana > 0:
        print(f"\nMana: {Mana}")
    elif Stealth > 0:
        print(f"\nStealth: {Stealth}")
    else:
        print() #newline

def save_game():
    pass

def return_to_main_menu():
    pass



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