
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os 
from blackjack_art import logo, blackjack_rules

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards():
  return random.choice(cards)


def calculate_score(player_cards):
  #Check Blackjack
  if len(player_cards) == 2 and sum(player_cards) == 21:
    return 0

  if 11 in player_cards and sum(player_cards) > 21:
    player_cards.remove(11)
    player_cards.append(1)
  return sum(player_cards)


def check_winner(player_score, computer_score):
  if player_score == computer_score:
    return "It's a Draw."
  elif computer_score == 0:
    return "Computer has BLACKJACK. Computer Wins." + logo + "\n"
  elif player_score == 0:
    return "You WIN with a BLACKJACK.\n" + logo + "\n"
  elif player_score > 21:
    return "You got busted. Computer Wins."
  elif computer_score > 21:
    return "Computer went over. YOU WIN !!! "
  elif player_score > computer_score:
    return "Congratulations!! You Win!! "
  else:
    return "You Lose. :( "


def play_game():
  game_on = True
  player_cards = []
  computer_cards = []
  player_score = 0
  computer_score = 0
  while game_on:
    print(logo)
    print(blackjack_rules)

    start_game = input("\nShall we START THE GAME? Type 'y' to play or 'n' to exit:  ")
    if start_game == 'y':
      # Function to draw cards randomly from the pack of cards
      for _ in range(2):
        player_cards.append(draw_cards())
        computer_cards.append(draw_cards())
      # print(player_cards)
      player_score = calculate_score(player_cards)
      print(f"Your cards: {player_cards}, Current Score: {player_score}")
      print(f"Computer's first card: {computer_cards[0]}")
  
      while game_on:
        deal = input("Type 'y' to get another card or 'n' to pass:  ")
        if deal == 'y':
          player_cards.append(draw_cards())
          player_score = calculate_score(player_cards)
          print(f"Your cards: {player_cards}, Current Score: {player_score}")
          print(f"Computer's first card: {computer_cards[0]}")
        else:
          game_on = False
          computer_cards.append(draw_cards())
          computer_score = calculate_score(computer_cards)
          while computer_score !=0 and computer_score < 17 :
            computer_cards.append(draw_cards())
            computer_score = calculate_score(computer_cards)
          print(f"Computer's final Hand: {computer_cards}, final score: {computer_score}")
  
  
  print("\n\n  ************************************************************************  ")
  print("  RESULTS:-  \n")
  print(f"  User's final Hand: {player_cards}, Final Score: {player_score}")
  print(f"  Computer's final Hand: {computer_cards}, Final Score: {computer_score}")
  print("\n  " +check_winner(player_score, computer_score))
  print("\n  ************************************************************************  \n")

# Start/Restart the game
while input("Do you want to play a game of BLACKJACK ? Type 'y' to play or 'n' to exit: ") == 'y':
  os.system('cls')
  play_game()
