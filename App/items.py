import App.Utilities.dices as Dices
import App.Utilities.units as Units
import App.Utilities.money as Money
import sqlite3

# TODO Updates the db to include item categories (stackable, equipment, weapon...)
# A super class for items


class Item:
    def __init__(self,
                 name: str,
                 weight: Units.Weight,
                 cost: Money.Coinage,
                 description: str = "",
                 categories: list[str] = [],
                 requirements: dict[str, str] = {},
                 effects: dict[str, str] = {},
                 rarity: str = "Common",
                 tags: list[str] = []):
        self.name = name
        self.weight = weight
        self.cp_cost = cost.convert(Money.cp)
        self.description = description
        self.categories = categories
        self.requirements = requirements
        self.effects = effects
        self.rarity = rarity
        self.tags = tags

    def save(self):
        # Exemple output : emblem = Items.Item("emblem", Units.Weight(0, "lb"), Money.GP(5), "A holy symbol is a representation of a god or pantheon. A cleric or paladin can use a holy symbol as a spellcasting focus, as described in the Spellcasting section. To use the symbol in this way, the caster must hold it in hand, wear it visibly, or bear it on a shield.", ["Gear", "Holy symbol"], rarity="Common", tags=["Utility"])
        categories = str(self.categories)[1:-1]
        categories = categories.replace("'", "")
        requirements = str(self.requirements)[1:-1].replace("'", "")
        requirements = requirements.replace("'", "")
        effects = str(self.effects)[1:-1].replace("'", "")
        effects = effects.replace("'", "")
        tags = str(self.tags)[1:-1].replace("'", "")
        tags = tags.replace("'", "")
        print(categories, requirements, effects, tags)

        conn = sqlite3.connect(r'App\\Objects\\objects.db')
        cursor = conn.cursor()
        cursor.execute(
            f"""INSERT INTO objects (name, weight, cp_cost, description, categories, requirements, effects, rarity, tags) VALUES (
            "{self.name}", 
            {self.weight.pounds}, 
            {self.cp_cost.number}, 
            "{self.description}", 
            "{categories}", 
            "{requirements}", 
            "{effects}", 
            "{self.rarity}", 
            "{tags}"
            ) """)
        conn.commit()
        conn.close()


def find(item_name):
    # Connects to database framework
    conn = sqlite3.connect(r'App\\Objects\\objects.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT * FROM objects WHERE name LIKE "%{item_name}%" """)
    # TODO Update the find function to return a different item class depending on the item's categories
    data = cursor.fetchall()
    conn.close()
    assert len(data) == 1, f"""Your query return more than one items or no 
    items at all, it returned {[item[0] for item in data]}"""
    name, weight, cp_cost, description, categories, reqs, effs, rarity, tags = data[
        0]
    weight = Units.Weight(weight, "lb")
    cp_cost = Money.CP(cp_cost)
    categories = categories.split(", ") if categories else []

    requirements = {}
    if reqs:
        reqs = reqs.split(", ")
        for data in reqs:
            data = data.split(": ")
            key, value = data
            requirements[key] = value

    effects = {}
    if effs:
        effs = effs.split(", ")
        for data in effs:
            data = data.split(": ")
            key, value = data
            effects[key] = value

    tags = tags.split(", ") if tags else []

    # TODO Add more cases
    if "Weapon" in categories:
        atk_type = effects["Attack type"]
        damage = effects["Damage"]
        dmg_type = effects["Damage type"]
        if atk_type == "Melee":
            range = Units.Distance(effects["Range"], "ft")
            return Melee(name, damage, dmg_type, range, weight, cp_cost, description, categories, requirements, effects, rarity, tags)
        elif atk_type == "Ranged":
            n_distance, l_distance = effects["Range"].split("/")
            n_distance = Units.Distance(n_distance, "ft")
            l_distance = Units.Distance(l_distance, "ft")
            return Range(name, damage, dmg_type, n_distance, l_distance, weight, cp_cost, description, categories, requirements, effects, rarity, tags)
        print("This item looks strange, it is a weapon but it is not ranged or melee")
        return Weapon(name, damage, dmg_type, weight, cp_cost, description, categories, requirements, effects, rarity, tags)
    else:
        return Item(name, weight, cp_cost, description, categories, requirements, effects, rarity, tags)


# Adds a class for weapons (ranged and melee)


class Weapon(Item):
    def __init__(self,
                 name: str,
                 damage: Dices.Dice,
                 dmg_type: str, 
                 weight: Units.Weight,
                 cost: Money.Coinage,
                 description: str = "",
                 categories: list[str] = [],
                 requirements: dict[str, str] = {},
                 effects: dict[str, str] = {},
                 rarity: str = "Common",
                 tags: list[str] = []):
        self.damage = damage
        self.dmg_type = dmg_type
        super().__init__(name, weight, cost, description,
                         categories, requirements, effects, rarity, tags)
        # TODO Add a system to incorporate damage type (ie. piercing)

# Adds a class for melee weapons


class Melee(Weapon):
    # TODO Implement versatile proprieties etc...
    def __init__(self,
                 name: str,
                 damage: Dices.Dice,
                 dmg_type: str, 
                 range: Units.Distance,
                 weight: Units.Weight,
                 cost: Money.Coinage,
                 description: str = "",
                 categories: list[str] = [],
                 requirements: dict[str, str] = {},
                 effects: dict[str, str] = {},
                 rarity: str = "Common",
                 tags: list[str] = []):
        self.range = range
        super().__init__(name, damage, dmg_type, weight, cost, description,
                         categories, requirements, effects, rarity, tags)

# Add a class for ranged weapons


class Range(Weapon):
    def __init__(self,
                 name: str,
                 damage: Dices.Dice,
                 dmg_type: str, 
                 n_distance: Units.Distance,
                 l_distance: Units.Distance,
                 weight: Units.Weight,
                 cost: Money.Coinage,
                 description: str = "",
                 categories: list[str] = [],
                 requirements: dict[str, str] = {},
                 effects: dict[str, str] = {},
                 rarity: str = "Common",
                 tags: list[str] = []):
        assert n_distance <= l_distance, "The normal range distance must shoreter then the long distance"
        self.n_distance = n_distance
        self.l_distance = l_distance
        super().__init__(name, damage, dmg_type, weight, cost, description,
                         categories, requirements, effects, rarity, tags)
        # TODO Add a system to use ammunition

# TODO Add class for measurable items (ie. ropes)
# TODO Add class for ammunition (ie. arrows)
# TODO Add class for special kinds of items (ie. spells)
# TODO Update super load call for objects subclasses
