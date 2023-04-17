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
    "money": 0
}

def machineLogic(drink):
    if checkEnoughIngredients(drink):
        transactionSuccessful = transaction(drink)
        if not transactionSuccessful:
            print("Sorry that's not enough money. Money refunded.")
            return
        else:
            makeDrink(drink)
            print("Here is your",drink ,"your change is ", transactionSuccessful)
            return
    else:
        print("sorry, not enough resources")

def checkEnoughIngredients(drink):
    drinkIngredients = MENU[drink]["ingredients"]
    for ingredient in drinkIngredients.keys():
        if resources[ingredient] < drinkIngredients[ingredient]:
            return False
    resources["money"] = resources["money"] + MENU[drink]["cost"]
    return True

def transaction(drink):
    quarters = int(input("insert quarters:"))
    nickels = int(input("insert nickels:"))
    dimes = int(input("insert dimes:"))
    pennies = int(input("insert pennies:"))
    balance = .25*quarters + .10*dimes + .05*nickels + .01*pennies
    if MENU[drink]["cost"] > balance:
        return False
    else:
        return balance - MENU[drink]["cost"]


def makeDrink(drink):
    drinkIngredients = MENU[drink]["ingredients"]
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] = resources[ingredient] - drinkIngredients[ingredient]

    return


off = False

while not off:
    response = input("What would you like? (espresso/latte/cappuccino)")
    if response == "done":
        off = True
    if response == "report":
        print("water:", resources.get("water"),
              "milk: ", resources.get("milk"),
              "coffee: ", resources.get("coffee"),
              "money: ", resources.get("money"))
        continue
    if response == "espresso" or response == "latte" or response == "cappuccino":
        machineLogic(response)
    else:
        print("Do not understand command")


print("done")
