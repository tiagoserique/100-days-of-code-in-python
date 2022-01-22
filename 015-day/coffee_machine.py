

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


def make_coffee(drink, resources):
	"""
		Deduct the required ingredients from the resources.
	"""
	ingredients = drink["ingredients"]

	for item in ingredients:
		amount_of_resource 		= resources[item]
		amount_of_ingredient 	= ingredients[item]

		resources[item] = amount_of_resource - amount_of_ingredient


def is_transaction_successful(drink, value_inserted):
	"""
		Return True when the payment is accepted, or False if money is 
		insufficient.
	"""
	drink_cost = drink["cost"]

	if ( drink_cost > value_inserted ):
		print("Sorry that's not enough money. Money refunded.")
		return False

	else:
		global money 
		money += drink_cost

		change 	= round(value_inserted - drink_cost, 2)

		if ( change > 0 ):
			print(f"Here is ${change} dollars in change.")
		
		return True



def process_coins():
	"""
		Returns the total calculated from coins inserted.
	"""
	print("Please insert coins.")
	# 0.25
	quarters = int(input("how many quarters?: "))	
	quarters *= 0.25
	
	# 0.10
	dimes = int(input("how many dimes?: "))	
	dimes *= 0.10
	
	# 0.05
	nickles = int(input("how many nickles?: "))	
	nickles *= 0.05
	
	# 0.01
	pennies = int(input("how many pennies?: "))	
	pennies *= 0.01

	return quarters + dimes + nickles + pennies



def is_resources_sufficient(drink, resources):
	"""
		Returns True when order can be made, False if ingredients are insufficient.
	"""
	ingredients = drink["ingredients"]

	for item in ingredients:
		amount_of_resource = resources[item]
		amount_of_ingredient = ingredients[item]

		if ( amount_of_resource < amount_of_ingredient ):
			print(f"Sorry there is not enough {item}")
			return False
	
	return True	


def print_resources(resources, money):
	water 	= resources["water"]
	milk 	= resources["milk"]
	coffee 	= resources["coffee"]
	print(f"Water: {water}ml")
	print(f"Milk: {milk}ml")
	print(f"Coffee: {coffee}g")
	print(f"Money: ${money}")





money 		= 0
turn_off 	= False

while not( turn_off ):
	choice = input("  What would you like? (espresso/latte/cappuccino): ")
	if ( choice == "report" ):
		print_resources(resources, money)	

	elif ( choice == "off"):
		turn_off = True

	elif (( choice == "latte")
	   or ( choice == "espresso")
	   or ( choice == "cappuccino")):
		if ( is_resources_sufficient(MENU[choice], resources) ):
			value_inserted = process_coins()
			if ( is_transaction_successful(MENU[choice], value_inserted) ):
				make_coffee(MENU[choice], resources)
				print(f"Here is your {choice}. Enjoy")
