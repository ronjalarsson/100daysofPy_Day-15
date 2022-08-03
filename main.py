from data import MENU
from data import resources

profit = 0
turn_off = False


# TODO: 4. Check resources sufficient?
def is_resource_sufficient(drink_ingredients):
    """Returns True when resources are sufficient to make the chosen drink
    and False when there is not enough ingredients to make the chosen drink."""
    # When the user chooses a drink,
    # the program checks if there are enough resources to make that drink.
    resources_sufficient = True  # Start by assuming that there is enough resources.
    for ingredient in drink_ingredients:  # Check through each ingredient.
        # If what it takes to make the chosen drink is less than ingredients in the resources,
        if drink_ingredients[ingredient] > resources[ingredient]:
            #  Let the user know that there is not enough ingredients to make the chosen drink,
            print(f"Sorry, there is not enough {ingredient}.")
            #  And return False (resources are not sufficient).
            resources_sufficient = False
    # If after above lines are run and the function did not return False,
    # it means we still have enough resources to make the chosen drink (resources are sufficient).
    return resources_sufficient


# TODO: 5. Process coins.
def process_coins():
    """Asks the user to enter coins and returns the total value of the inserted coins."""
    print("Please insert coins.")
    q_amount = int(input("How many quarters?: "))
    d_amount = int(input("How many dimes?: "))
    n_amount = int(input("How many nickles?: "))
    p_amount = int(input("How many pennies?: "))
    # Calculate the monetary value of the coins inserted.
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total = (q_amount * 0.25) + (d_amount * 0.1) + (n_amount * 0.05) + (p_amount * 0.01)
    return total


# TODO: 6. Check transaction successful?
def check_transaction(paid_amount, drink_cost):
    """Returns True when the payment is accepted, or False if the funds are inefficient.
    The amount of the change will be displayed as well."""
    # Check that the user has inserted enough money to purchase the drink they selected.
    if paid_amount < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        # If the user has inserted enough money,
        # the cost of the drink gets added to the machine as the profit and this will be
        # reflected the next time “report” is triggered.
        global profit  # Getting the global variable by adding "global" before the variable name.
        change = round(paid_amount - drink_cost, 2)
        profit = round(profit + drink_cost, 2)
        # If the user has inserted too much money, the machine should offer change.
        print(f"Here is ${change} dollars in change.")
        return True


# TODO: 7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients of the chosen drink from the resources."""
    # If the transaction is successful and there are enough resources to make the drink the user
    # selected, then the ingredients to make the drink is deducted from the coffee machine resources.
    for ingredient in order_ingredients:
        resources[ingredient] = resources[ingredient] - order_ingredients[ingredient]
    # Once all resources have been deducted, tell the user to enjoy his/her chosen drink.
    print(f"Here is your {drink_name}, enjoy! ☕️")


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
while not turn_off:
    # Check the user input to decide what to do next.
    option = input(" What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if option == "off":
        # For maintainers of the coffee machine,
        # they can use “off” as the secret word to turn off the machine.
        # Your code should end execution when this happens.
        turn_off = True
    # TODO: 3. Print report.
    elif option == "report":
        # When the user enters “report” to the prompt,
        # a report should be generated that shows the current resource values.
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # Put the user input "option" from "MENU" into variable "drink".
        # variable "drink" contains both the values under "ingredients" and "cost"
        # of the chosen key, e. g. espresso/latte/cappuccino.
        drink = MENU[option]
        # Check if the resources are enough to make the order.
        if is_resource_sufficient(drink['ingredients']):  # Pulling the data from the chosen drink's ingredients.
            # If resources are sufficient, process with pyment by using process_coins()
            # and put the returned value into variable "payment".
            payment = process_coins()
            # Check if the transaction is successful by
            # comparing the paid amount in variable "payment" with the cost of the drink listed in "MENU".
            if check_transaction(payment, drink['cost']):  # Pulling the data from the chosen drink's cost.
                # If the transaction is successful, make coffee.
                # Variable "option" stores the original user input which is the name of the drink,
                # the ingredients of the user's ordered drink is accessed by using "drink['ingredients']".
                make_coffee(option, drink['ingredients'])  # Pulling the data from the chosen drink's ingredients.
