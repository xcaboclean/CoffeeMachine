class Item:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffe": coffee
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

    def report(self):
        for item in self.resources:
            print(f"-{item}:{self.resources[item]}")


class CashBox():
    CURRENCY = {"$"}
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.10
    NICKEL_VALUE = 0.05
    PENNY_VALUE = 0.01

    def __init__(self, quarters=0, dimes=0, nickels=0, pennies=0):
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies

    def add_coins(self):
        self.quarters += int(input("Enter the number of quarters: "))
        self.dimes += int(input("Enter the number of dimes: "))
        self.nickels += int(input("Enter the number of nickles: "))
        self.pennies += int(input("inputEnter the number of pennes:"))

    def report(self, quarters=0, dimes=0, nickels=0, pennies=0):
        total = (self.quarters * self.QUARTER_VALUE +
                 self.dimes * self.DIME_VALUE +
                 self.nickels * self.NICKEL_VALUE +
                 self.pennies * self.PENNY_VALUE
                 )
        print(f"{self.CURRENCY}:{total}")
