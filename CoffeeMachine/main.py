MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 4. create a function for checking for sufficiency of recourses
def is_resource_enough(order_ingredients):
    is_enough = True

    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"We can not make you a drink, not enough of {i}")
            is_enough = False
    return is_enough

def process_coins():
    #Returns the total amount inserted
    input("Please insert the coins: ")
    total = int(input(f"How many quarters do you have?")) * 0.25
    total += int(input(f"How many dimes do you have?")) * 0.1
    total += int(input(f"How many nickels do you have?")) * 0.05
    total += int(input(f"How many pennies do you have?")) * 0.01
    return total

profit = 0
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")

def is_payment_successful(payment_received, drink_cost):
    if payment_received < drink_cost:
        print("Sorry, that's not enough money")
        return False
    else:
        change = round(payment_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True







#TODO 1.Prompt user by asking What would you like? (espresso/latte/cappuccino)
ordering = True


while ordering:

    user_choice = input(f"What would you like? ('espresso' / 'latte' / 'cappuccino' ): ").lower()

    # TODO 2.Create an execution button
    if user_choice == "turn off":
        ordering = False
    elif user_choice == "report":
        print(f"Milk: {resources['water']} ml")
        print(f"Coffee: {resources['coffee']}  g")
        print(f"Money: {profit}")
        print(f"Water: {resources['water']} ml")

    # TODO 3. check for sufficiency of recourses
    else:
        drink = MENU[user_choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])



