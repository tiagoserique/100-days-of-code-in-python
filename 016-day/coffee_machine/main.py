from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_off = False

menu 			= Menu()
coffe_maker 	= CoffeeMaker()
money_machine 	= MoneyMachine()

while not( turn_off ):
	options = menu.get_items()
	choice 	= input(f"​What would you like? ({options}):​")
	
	if ( choice == "off" ):
		turn_off = True
	
	elif ( choice == "report" ):
		coffe_maker.report()
		money_machine.report()

	else:
		drink = menu.find_drink(choice)

		if ( drink ):
			if ( coffe_maker.is_resource_sufficient(drink) ):
				if ( money_machine.make_payment(drink.cost) ):
					coffe_maker.make_coffee(drink)
