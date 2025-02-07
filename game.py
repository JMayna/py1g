import random



def new_Game():
      character_Creation()
 
def character_Creation():
    playername = input("What is your name? ")
    print("Welcome " + playername + ",")
    
    while True:
        classchoice = input("Which class do you choose\n [1] Fighter\n [2] Mage \n [3] Thief \n")
        if classchoice == "1":
            print("You have chosen a Fighter")
            playerclass= "Fighter"
            break
            
        elif  classchoice == "2":
            print("You have chosen a Mage")
            playerclass= "Mage"
            break
        
        elif classchoice == "3":
            print("You have chosen a Thief")
            playerclass= "Thief"
            break
        
        else:
            print ("Invalid choice: Plase choose 1, 2, or 3")
     
 
 
    
def quit_Game():
    print("Exiting game!")
    exit()


#Menu Choices
while True:
    menuChoice = input("Please choose and option \n [1] New Game\n [2] Exit Game\n")

    if menuChoice == "1":
        new_Game()
        break

    elif menuChoice == "2":
        quit_Game
        break
    else: print("Invalid choice: Please Choose 1 or 2")
    
