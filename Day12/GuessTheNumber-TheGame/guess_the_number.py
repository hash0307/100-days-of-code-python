#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo, congrats, thanks
import random
import os

def set_attempts(difficulty_level):
    if difficulty_level == "hard":
        return 5
    elif difficulty_level == "medium":
        return 7
    else:
        return 10


def set_game_number():
    return random.randint(1, 100)


def check_result(user_guess, game_number):
    if user_guess == game_number:
        print(congrats)  
        print(f"\nWinning Number is: {game_number}")
        print("You guessed the correct number.")
        # attempts_left = 0
        return -1
    elif user_guess < game_number:
        print("Too Low.")
        print("Guess again.")
        # attempts_left -= 1
        return attempts_left - 1
    elif user_guess > game_number:
        print("Too high.")
        print("Guess again.")
        # attempts_left -= 1
        return attempts_left - 1

  
game_on = True
while game_on:

    print(logo)
    print("\n WELCOME TO THE NUMBER GUESSING GAME!")
    print("\n I'm thinking of a number between 1 & 100.")
    
    attempts_left = set_attempts(input("Choose a difficulty. Type 'easy' or 'medium' or 'hard': ").lower())
    print(f"Total attempts: {attempts_left}")
    game_number = set_game_number()

    while attempts_left > 0:
        print(f" You have {attempts_left} attempts remaining to guess the number.")

        user_guess = int(input(" Make a guess: "))

        attempts_left = check_result(user_guess, game_number)

        if attempts_left == 0:
            print(" UH-OHH !! YOU LOST.")

    replay = input("\nDo you want to play again? Type 'y' to play or 'n' to exit: ")
    if replay == 'y':
        os.system('cls')
    else:
        game_on = False
        print("\n" + thanks)
