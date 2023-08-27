from art import logo, vs
from game_data import data
import random
import os

game_on = True
user_score = 0
entityB=random.choice(data)

def print_entity_details(entity):
  """ Return the entity details in a printable format"""
  entity_name = entity["name"]
  entity_desc = entity["description"]
  entity_country = entity["country"]
  return f"{entity_name} , a {entity_desc}, from {entity_country}"

  
def check_winner(entityA, entityB):
  """Returns the winner based on follower count of respective entity"""
  if entityA["follower_count"] > entityB["follower_count"]:
    return "A"
  return "B"


while game_on:
  os.system('cls')

  # Print the game logo
  print(logo)
  
  if user_score > 0:
    print(f"You're right. Current score: {user_score}")
  
  entityA=entityB
  # print(entityA)
  entityB=random.choice(data)
  
  while entityA == entityB:
    entityB = random.choice(data)
  
  # Display the name, description, country of the selected entry. Make sure to not display the follower-count
  # print("Compare A: "+ entityA["name"] + ", a " + entityA["description"] + ", from " + entityA["country"] + ".")
  print(f"Compare A: {print_entity_details(entityA)}.")
   
  # Print the "VS" logo
  print(vs)
  
  # Display the name, description, country of the selected entry. Make sure to not display the follower-count
  # print("Compare B: "+ entityB["name"] + ", a " + entityB["description"] + ", from " + entityB["country"] + ".")
  print(f"Against B: {print_entity_details(entityB)}.")
  
  # Ask the user for input. Pick either Entity A or B.
  user_guess=input("\nWho has more followers? Type 'A' or 'B': ").upper()
  
  # Based on user input compare the follower-count
  # If the user guess is correct. Increment the user_score & Pick another set of entity randomly.
  
  # Else if incorrect, User loses. Display the final user score.
  if check_winner(entityA, entityB) == user_guess:
    user_score += 1
    
  else:
    print(f"\nSorry. That's wrong. Final Score: {user_score}")
    game_on = False