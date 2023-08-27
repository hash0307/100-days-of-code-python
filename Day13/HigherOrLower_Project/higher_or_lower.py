from art import logo, vs
from game_data import data
import random
import os


game_on = True
user_score = 0

def check_winner(entityA, entityB):
  if entityA["follower_count"] > entityB["follower_count"]:
    return "A"
  return "B"


while game_on:
  os.system('cls')
  # Print the game logo
  print(logo)
  if user_score > 0:
    print(f"You're right. Current score: {user_score}")
  # Randomly pick an entry from the list of dictionary for Entity-A
  entityA=random.choice(data)
  # print(entityA)
  
  # Display the name, description, country of the selected entry. Make sure to not display the follower-count
  print("Compare A: "+ entityA["name"] + ", a " + entityA["description"] + ", from " + entityA["country"] + ".")
  
  # Print the "VS" logo
  print("\n" + vs)
  
  # Similarly pick an entry from the list of dicitonary for Entity-B
  entityB=random.choice(data)
  # print(entityB)
  
  # Display the name, description, country of the selected entry. Make sure to not display the follower-count
  print("Compare B: "+ entityB["name"] + ", a " + entityB["description"] + ", from " + entityB["country"] + ".")
  
  # Ask the user for input. Pick either Entity A or B.
  user_guess=input("Who has more followers? Type 'A' or 'B': ").upper()
  
  # Based on user input compare the follower-count
  if check_winner(entityA, entityB) == user_guess:
    user_score += 1
    
  else:
    print(f"Sorry. That's wrong. Final Score: {user_score}")
    game_on = False
    
  # If the user guess is correct. Increment the user_score & Pick another set of entity randomly.
  
  # Else if incorrect, User loses. Display the final user score.