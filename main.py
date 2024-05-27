from data import Menu, CoffeeMachine, CashBox

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

cash_box = CashBox()



while machine.led == True:
    order = input("Whats is your order?")

    if order == "off":
        machine.power_off()
    elif order =="report":
        machine.report()
        cash_box.report()
    else:
        drink = menu.get_item(order)
        print(drink)
        cash_box.add_coins()


