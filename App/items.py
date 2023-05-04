import App.Utilities.dice as Dices
import App.Utilities.units as Units
import sqlite3

# TODO Updates the db to include item categories (stackable, equipment, weapon...)
# A super class for items


class Item:
    def __init__(self, name: str, weight: Units.Weight, cp_cost: int, description: str = ""):
        self.name = name
        self.weight = weight
        self.cp_cost = cp_cost
        self.description = description


def find(item_name):
    # Connects to database framework
    conn = sqlite3.connect(r'App\\Objects\\objects.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT * FROM objects WHERE name LIKE "%{item_name}%" """)
    # TODO Update the find function to return a different item class depending on the item's categories
    data = cursor.fetchall()
    assert len(data) == 1, f"""Your query return more than one items or no 
    items at all, it returned {data}"""
    name, weight, cp_cost, description = data[0]
    return Item(name, Units.Weight(weight, "lb"), cp_cost, description)

# A class for stackable items (ie. torches)


class Stackable(Item):
    def __init__(self, name: str, weight: Units.Weight, cp_cost: int, quantity: int = 1, description: str = ""):
        super().__init__(name, weight, cp_cost, description)
        self.quantity = quantity
        # TODO Add something to merge similar items on item creation

# TODO Add class for measurable items (ie. ropes)
# TODO Add class for ammunition (ie. arrows)
# TODO Add class for special kinds of items (ie. spells)

# Adds a class for unique items (not stackables)


class Unique(Item):
    def __init__(self, name: str, weight: Units.Weight, cp_cost: int, description: str = ""):
        super().__init__(name, weight, cp_cost, description)

# Adds a class for weapons (ranged and melee)


class Weapon(Unique):
    def __init__(self, name: str, damage: Dices.Dice, weight: Units.Weight, cp_cost: int, description: str = ""):
        self.damage = damage
        super().__init__(name, weight, cp_cost, description)
        # TODO Add a system to incorporate damage type (ie. piercing)

# Adds a class for melee weapons()


class Melee(Weapon):
    def __init__(self, name: str, damage: Dices.Dice, weight: Units.Weight, cp_cost: int, description: str = ""):
        super().__init__(name, damage, weight, cp_cost, description)

# Add a class for ranged weapons


class Range(Weapon):
    def __init__(self, name: str, damage: Dices.Dice, n_distance: Units.Distance, l_distance: Units.Distance, weight: Units.Weight, cp_cost: int, description: str = ""):
        super().__init__(name, damage, weight, cp_cost, description)
        assert n_distance <= l_distance, "The normal range distance must shoreter then the long distance"
        self.n_distance = n_distance
        self.l_distance = l_distance
        # TODO Add a system to use ammunition
