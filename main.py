from dataclasses import dataclass
from resource import data


# TODO 1.  Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3. Print report of all coffee machine resources
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.
@dataclass
class CoffeeMachine:
    def __init__(self, resources, coins):
        self.resources = []
        self.coins = []


class Resource:
    description: str
    volume: float
    unit: str


class Coins:
    type: str
    quantity: int
    value: float
