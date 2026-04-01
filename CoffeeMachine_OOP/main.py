from CoffeeMachine_OOP.menu import MenuItem
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine  = MoneyMachine()
menu = Menu()



is_on = True
while is_on :
        options = menu.get_items()
        choice = input(f"what would you like? {options} - ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            check_resource = coffee_machine.is_resource_sufficient(drink)
            if check_resource:
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)
