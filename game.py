import random
import pickle




monster_names=  [
    "Trugle the Goblin",
    "Gnar the Fierce Orc",
    "Snarl the Gruesome Skeleton",
    "Crush the Swift Spider",
    "Bite the Unseen Rat",
    "Whisper the Silent Zombie",
    "Creep the Mighty Slime",
    "Fang the Wicked Bat",
    "Shadow the Brutal Kobold",
    "Howl the Agile Ghoul",
    "Zorgon the Destroyer",
    "Xylar the Sorcerer",
    "Kraken the Deep",
    "Medusa the Gorgon",
    "Cerberus the Guardian",
    "Chimera the Hybrid",
    "Hydra the Many-Headed",
    "Phoenix the Reborn",
    "Griffin the Majestic",
    "Minotaur the Labyrinth",
    "Cyclops the One-Eyed",
    "Harpy the Winged",
    "Siren the Enchanting",
    "Dragon the Ancient",
    "Wraith the Spectral"
]

def generate_monster(player_level):
    name = random.choice(monster_names)
    
    #Monster Stats scale with player level 
    
    hp = random.randint(5 * player_level, 10 * player_level)
    ac = random.randint(10 + player_level, 15 + player_level)
    attack = random.randint(2+ player_level, 5 + player_level)
    damage = random.randint(1 * player_level, 4 * player_level)
    return {"name": name, "hp": hp, "ac": ac, "attack": attack, "damage": damage}  # Return as a dictionary


def new_Game():
     playername, playerclass, HP, AC, Mana, Stealth, player_level, exp = character_Creation()
     if playerclass:
         print(f"Welcome {playername}, you have chosen to play as a {playerclass}")
         game_menu(playername, playerclass, HP,AC, Mana, Stealth, player_level, exp)

def character_Creation():
   
    playername = input("What is your name? ")
    print(f"Welcome {playername}!")
    
    playerclass = ""
    HP = 0
    AC = 0
    Mana = 0
    Stealth = 0 
    player_level = 1
    exp = 0

    while True:
        classchoice = input("Which class do you choose?\n [1] Fighter\n [2] Mage \n [3] Thief \n")
        if classchoice == "1":
            playerclass = "Fighter"
            HP = 20
            AC = 18
            player_level= 1
            exp = 0
            break  
        elif classchoice == "2":
            playerclass = "Mage"
            HP = 20
            AC = 18
            Mana = 20
            player_level= 1
            exp = 0
            break
        elif classchoice == "3":
            playerclass = "Thief"
            HP = 20
            AC = 18
            Stealth = 20
            player_level= 1
            exp = 0
            break
        else:
            print("Invalid choice: Please choose 1, 2, or 3")
    return  playername, playerclass, HP, AC, Mana, Stealth, player_level, exp

    print(f"Welcome {playername}, you have chosen to play as a {playerclass}")  


def game_menu (playername, playerclass, HP, AC, Mana, Stealth, player_level, exp):
    while True:
        playerChoice =  input("What would you like to do: \n [1] Go to next encounter \n [2] View your stats \n [3] Save Game \n [4] Return to Main Menu: \n")
        
        if playerChoice == "1":
            next_encounter(playername, playerclass, player_level, HP, AC, Mana, Stealth, exp)  # Pass player_level)
            break
        elif playerChoice == "2":
            view_stats(playername, playerclass,HP,AC,Mana, Stealth, player_level, exp)
            
        elif playerChoice == "3":
            save_game(playername, playerclass, HP, AC, Mana, Stealth, player_level, exp)
            
        elif playerChoice == "4":
            return_to_main_menu()
            break
        else:
            print("Invalid Choice. Please Choose 1, 2, 3, or 4")
       


#Dice system

def roll_dice(num_dice, sides):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, sides)
        total += roll
    return total 

def attack_roll(attack_bonus): 
    return roll_dice(1, 20) + attack_bonus  # 1d20 + attack bonus

def damage_roll(num_dice, sides): 
    return roll_dice(num_dice, sides)










def next_encounter(playername, playerclass, player_level, HP, AC, Mana, Stealth, exp):  # Add exp here
    monster = generate_monster(player_level)
    print(f"You encounter a {monster['name']}!")

    while True:  # Encounter loop
        # Player's turn
        attack_roll_player = attack_roll(0)  # No attack bonus for now
        print(f"{playername} attacks! Roll: {attack_roll_player}")
        if attack_roll_player >= monster["ac"]:
            damage_roll_player = damage_roll(1, monster["damage"])
            monster["hp"] -= damage_roll_player
            print(f"{monster['name']} takes {damage_roll_player} damage. HP: {monster['hp']}")
            if monster["hp"] <= 0:
                print(f"You defeated the {monster['name']}!")
                exp += 100 #example exp reward
                print(f"You gained 100 experience points! You now have {exp} experience points.")
                game_menu(playername, playerclass, HP, AC, Mana, Stealth, player_level, exp)
        else:
            print("Attack misses!")
        input("Press space to continue...")  # Pause here, wait for spacebar

        # Monster's turn (if still alive)
        if monster["hp"] > 0:
            attack_roll_monster = attack_roll(monster["attack"])
            print(f"Monster attacks! Roll: {attack_roll_monster}")
            if attack_roll_monster >= AC:
                damage_roll_monster = damage_roll(1, monster["damage"])
                HP -= damage_roll_monster
                print(f"{playername} takes {damage_roll_monster} damage. HP: {HP}")
                if HP <= 0:
                    print("You have been defeated!\n Game over!")
                    while True:
                        play_again = input("Would you like to play again?\n [1] Yes\n[2] No \n :")
                        if play_again == "1":
                            new_Game()
                            break
                        elif play_again == "2":
                            quit_Game()
                            break
                        else:
                            print("Invlaid Choice please choose [1] or [2]\n")
                    
            else:
                print("Monster attack misses!")
        input("Press space to continue...")  # Pause here, wait for spacebar
        if HP <= 0:
            game_menu()
    
    
    
    
    
    
    
    
    
    

def view_stats(playername, playerclass, HP, AC, Mana, Stealth, player_level, exp ):
    
    print(f"Name:{playername}\nClass: {playerclass}\nHP: {HP}\nAC: {AC}\n Experience: {exp}", end="")
    if Mana > 0:
        print(f"\nMana: {Mana}")
    elif Stealth > 0:
        print(f"\nStealth: {Stealth}")
    else:
        print() #newline

def save_game(playername, playerclass, HP, AC, Mana, Stealth, player_level, exp):
     game_data = {  # Create a dictionary to store game data
        "playername": playername,
        "playerclass": playerclass,
        "HP": HP,
        "AC": AC,
        "Mana": Mana,
        "Stealth": Stealth,
        "player_level": player_level,
        "exp": exp
    }
     
     try:
         with open("save_game.pkl", "wb") as file:
             pickle.dump(game_data, file)
         print("Game Saved Sucessfully")
     except Exception as e:
         print(f"Erorr saving game {e}")
     
def load_game():
    try:
        with open("save_game.pkl", "rb") as file:  # Open file in binary read mode
            game_data = pickle.load(file)  # Load game data
        print("Game loaded successfully!")
        return game_data  # Return the loaded game data
    except FileNotFoundError:
        print("No saved game found.")
        return None  # Return None if no save file exists
    except Exception as e:
        print(f"Error loading game: {e}")
        return None
     
     
     
     

def return_to_main_menu():
    main_menu()



def quit_Game():
    print("Exiting game!")
    exit()


def main_menu():
    while True:
        menuChoice = input("Please choose an option \n [1] New Game\n [2] Load Game\n [3] Exit Game\n")  # Added Load Game option

        if menuChoice == "1":
            new_Game()
            break
        elif menuChoice == "2":
            loaded_game = load_game()
            if loaded_game:
                playername = loaded_game["playername"]
                playerclass = loaded_game["playerclass"]
                HP = loaded_game["HP"]
                AC = loaded_game["AC"]
                Mana = loaded_game["Mana"]
                Stealth = loaded_game["Stealth"]
                player_level = loaded_game["player_level"]
                exp = loaded_game["exp"]
                print("Game loaded. Continuing from where you left off.")
                game_menu(playername, playerclass, HP, AC, Mana, Stealth, player_level, exp)
                break  # Exit main menu after loading
            else:
                print("No saved game found. Starting a new game.") #inform user that no save was found
                new_Game()
                break #exit loop after new game
        elif menuChoice == "3":  # Changed to 3
            quit_Game()
            break
        else:
            print("Invalid choice: Please choose 1, 2, or 3")  # Updated message

main_menu()