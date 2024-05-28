class Item:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:

    def __init__(self):
        self.menu = [
            Item(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            Item(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            Item(name="cappuccino", water=250, milk=50, coffee=24, cost=30)
        ]

    def get_items(self):
        options: str = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def get_item(self, order):

        for item in self.menu:

            if item.name == order:
                return item


class CoffeeMachine():
    led: bool

    def __init__(self, led):
        self.led = led
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def power_off(self):
        self.led = False

    def power_on(self):
        self.led = True

    def check_resources(self, drink):
        resources_ok = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                resources_ok = False
        return resources_ok

    def report(self):
        for item in self.resources:
            print(f"-{item}:{self.resources[item]}")

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")