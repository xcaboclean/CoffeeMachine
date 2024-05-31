from data import Menu, CoffeeMachine, CashRegister

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3. Print report of all coffee machine resources
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.

menu = Menu()
print(menu.get_items())
machine = CoffeeMachine(True)
cashbox = CashRegister()




while machine.led == True:
    options = menu.get_items()
    order = input(f"Whats would you like({options}): ")
    if order == "off":
        machine.power_off()
    elif order =="report":
        machine.report()
        cashbox.report()
    else:
        drink = menu.get_item(order)
        if machine.check_resources(drink):
            if cashbox.payment(drink.cost):
                machine.make_coffee(drink)




