import App.Utilities.dice as Dices
import App.Utilities.units as Units
import App.Utilities.money as Money

# TODO Add weight quantity and a description for items
# A super class for items


class Item:
    def __init__(self, name: str, weight: int, cp_cost: int, description: str = ""):
        self.name = name
        self.weight = weight
        self.cost = Money.CP(cp_cost)
        self.description = description

# A class for stackable items (ie. torches)


class Stackable(Item):
    def __init__(self, name: str, weight: int, cp_cost: int, quantity: int = 1, description: str = ""):
        super().__init__(name, weight, cp_cost, description)
        self.quantity = quantity
        # TODO Add something to merge similar items on item creation

# TODO Add class for measurable items (ie. ropes)
# TODO Add class for ammunition (ie. arrows)
# TODO Add class for special kinds of items (ie. spells)

# Adds a class for unique items (not stackables)


class Unique(Item):
    def __init__(self, name: str, weight: int, cp_cost: int, description: str = ""):
        super().__init__(name, weight, cp_cost, description)

# Adds a class for weapons (ranged and melee)


class Weapon(Unique):
    def __init__(self, name: str, damage: Dices.Dice, weight: int, cp_cost: int, description: str = ""):
        self.damage = damage
        super().__init__(name, weight, cp_cost, description)
        # TODO Add a system to incorporate damage type (ie. piercing)

# Adds a class for melee weapons()


class Melee(Weapon):
    def __init__(self, name: str, damage: Dices.Dice, weight: int, cp_cost: int, description: str = ""):
        super().__init__(name, damage, weight, cp_cost, description)

# Add a class for ranged weapons


class Range(Weapon):
    def __init__(self, name: str, damage: Dices.Dice, n_distance: Units.Distance, l_distance: Units.Distance, weight: int, cp_cost: int, description: str = ""):
        super().__init__(name, damage, weight, cp_cost, description)
        assert n_distance <= l_distance, "The normal range distance must shoreter then the long distance"
        self.n_distance = n_distance
        self.l_distance = l_distance
        # TODO Add a system to use ammunition
