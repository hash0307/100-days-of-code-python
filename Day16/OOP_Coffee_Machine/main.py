from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''
1. Print report
2. Check resources sufficient
3. Process Coins
4. Check Transaction Successful
5. Make Coffee
'''

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
coffee_machine_is_on = True

# Print the report
# coffee_maker.report()
# money_machine.report()

while coffee_machine_is_on:
    options = menu.get_items()
    choice = input(f"What would you like ? {options} : ")
    if choice == "off":
        coffee_machine_is_on = False
    elif choice == "report":
        # Print the report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



