class Item:

    def __init__(self, name, water, milk, coffee, cost):
        self.name  = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffe": coffee
        }

