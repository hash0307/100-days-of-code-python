import random
import os
from Hangman_Template import welcome_logo, endgame_logo, template, template_0, template_1, template_2, template_3, template_4, template_5, template_6, template_7, words

user_guess = ["_","_","_","_","_","_","_",]
template_list = [template_1, template_2, template_3, template_4, template_5, template_6, template_7]

print(welcome_logo)
print(template.center(100))
# print(template)
print(user_guess)
game_start = input("Do you want to start the Game ? Type \"Y\" or \"N\". ").lower()

game = True
hangman_count = 0
game_word = random.choice(words)

while game:
    
    if game_start == "y":
        # print(template_0)
        count = 0
        
        user_input = input("Enter your guess letter : ")
        os.system('cls')

        if user_input in game_word:
            for letter in game_word:
                if user_input == letter:
                    user_guess[count] = game_word[count]
                count += 1
            print(user_guess)
            print(template_list[hangman_count])
        else:
            hangman_count += 1
            print(f"Incorrect Guess #{hangman_count}. Please Try again.")
            print(user_guess)
            print(template_list[hangman_count-1])

        if "_" not in user_guess:
            print("CONGRATULATIONS!!!! YOU WON !!!")
            break

        if hangman_count >= 7:
            game = False
            print(endgame_logo)
            print(f"Word is: {game_word}")
            break
    else:
        game = False
        print("Thank you. Hope you have a great day.")
        break