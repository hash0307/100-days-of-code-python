from coffee_menu import MENU, resources
from coffee_machine_art import logo, coffee_mug, coffee_emoji, report
import os

coffee_machine_on = True
resources["money"] = 0


def make_coffee(coffee_type):
    """ Function to adjust the resources in inventory based on the coffee type and serve coffee. """
    for ingredient in MENU[coffee_type]["ingredients"]:
        # print(ingredient)
        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]
    
    return f"Here is your {coffee_type} {coffee_emoji} \nHave a good day!!"
    

def check_stock(coffee_type):
    """ Function returns True, if the selected coffee resources are available in stock
    Else, return the out of stock resource name"""

    if resources["water"] < MENU[coffee_type]["ingredients"]["water"] and \
        "water" in MENU[coffee_type]["ingredients"]:
        return "water"
    elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"] and \
        "coffee" in MENU[coffee_type]["ingredients"]: 
        return "coffee"
    elif "milk" in MENU[coffee_type]["ingredients"] and \
        resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        return "milk"
    else:
        return MENU[coffee_type]["cost"]


def show_report():
    return f"Today's Report:- \nWater: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}"

def refill_stock():
    """ Functions refills the stock to existing stock """
    resources["water"] = 500
    resources["milk"] = 250
    resources["cofee"] = 100

print(logo + coffee_mug)

while coffee_machine_on:
    # print(logo + "      "+coffee_mug)
    print("*************************************************************".center(50))
    user_input=input("What would you like to have today? \nChoose:\n1. Espresso \n2. Latte \n3. Cappuccino.\nEnter your choice: ").lower()
    print("*************************************************************".center(50))

    if user_input == "off":
        coffee_machine_on = False
    elif user_input == "report":
        os.system('cls')
        print(report + show_report())
    elif user_input == "refill":
        os.system('cls')
        print("\nRefilling all the stocks ......")
        refill_stock()
        print("\nStocks Added to Inventory.")
    else:
        item_cost = check_stock(user_input)
        # print(item_cost)

        if type(item_cost) == float:
            print("We are almost ready. \nEnter coins:")
            
            quarters = float(input("No. of quarters: "))
            dimes = float(input("No. of dimes: "))
            nickels = float(input("No. of quarters: "))
            pennies = float(input("No. of pennies: "))
            
            amount_paid = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)
            print(f"Total money inserted: {amount_paid}")
            
            if amount_paid > item_cost:
                resources["money"] += item_cost
                change_amount = round((amount_paid - item_cost),2)
                print(f"\n\nPreparing your {user_input} ... ")
                print(make_coffee(user_input))
                print(f"\nHere's your change. Amount = ${change_amount}")
            else:
                print(f"\nSorry. That's not enough money.")
                print(f"Money refunded: {round(amount_paid,2)}")
        else:
            print(f"\nSorry there's not enough {item_cost}")
