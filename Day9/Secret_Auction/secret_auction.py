import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

continue_auction = True
bid_details = {}

def add_bidder(name, amount):
    bid_details[name] = amount

def check_winner(bid_details):
    highest_bid = 0
    winner_name = ""
    for bidder in bid_details:
        price = bid_details[bidder]
        if price > highest_bid:
            highest_bid = price
            winner_name = bidder

    print(logo)
    print(f"\n \n The winner is {winner_name} with the highest bid of amount : $ {highest_bid}. ")

while continue_auction:
    print(logo)
    
    choice = input("Do we have a bidder ? Type 'yes' or 'no'. ").lower()
    if choice == 'yes':
        os.system('cls')
        bidder_name = input("Enter your name : ")
        bid_amount = int(input("Enter your bid amount ($): "))
        add_bidder(name=bidder_name, amount=bid_amount)
    elif choice == 'no':
        os.system('cls')
        continue_auction = False
        check_winner(bid_details)
    else:
        choice = input("Kindly enter the correct choice. 'yes' or 'no'").lower()