import random

def roll_dice():      
    return random.randint(1, 10)


def dice_game(): 
    print("Welcome to my Python dice game!") 

    character1_name = input("Enter character 1's name:") 
    character2_name = input("Enter character 2's name:")

    character1_score = 0 
    character2_score = 0

    rounds = int(input("Enter number of rounds you'd like to play:")) 
    for round_number in range(1, rounds + 1): 
        print(f"\n--- round {round_number} ---") 

        character1_roll = roll_dice() 
        character2_roll = roll_dice()

        print(f"{character1_name} rolled: {character1_roll}") 
        print(f"{character2_name} rolled: {character2_roll}")

        if character1_roll > character2_roll:  
            print(f"{character1_name} has won this round!") 
            character1_score += 1 
        elif character1_roll < character2_roll:
            print(f"{character2_name} has won this round!")
            character2_score += 1
        else:
            print("this round was a tie!") 

    print("\n--- Final Scores ---") 
    print(f"{character1_name}: {character1_score}") 
    print(f"{character2_name}: {character2_score}")

    if character1_score > character2_score:  
        print(f"\n{character1_name} is the champion!!!") 
    elif character1_score < character2_score:
        print(f"\n{character2_name} is the champion!!!")
    else:
        print("\nthe characters have tied!") 


dice_game()

