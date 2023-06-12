import App.Utilities.dices as Dices
import App.Utilities.units as Units
import App.Utilities.money as Money
import sqlite3


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

    def __repr__(self):
        return "<Item: " + str((self.name, self.weight.value, self.cp_cost.number)) + ">"

    def save(self):
        # Exemple input : javelin = Items.Item("Javelin", Units.Weight(10, "lb"), Money.CP(250), "Proficiency with a javelin allows you to add your proficiency bonus to the attack roll for any attack you make with it.", ["Weapon", "Javelin"], {}, {"Attack type": "Melee", "Range": "5", "Damage": "1d6+4", "Damage type": "Piercing", "Thrown": "30/120"}, "Common", ["Damage", "Combat", "Javelin", "Simple"])
        categories = str(self.categories)[1:-1]
        categories = categories.replace("'", "")

        requirements = str(self.requirements)[1:-1]
        requirements = requirements.replace("'", "")

        effects = str(self.effects)[1:-1]
        effects = effects.replace("'", "")

        tags = str(self.tags)[1:-1]
        tags = tags.replace("'", "")

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
    data = cursor.fetchall()
    conn.close()

    # Checks that if the search returns multiple hits, it chooses the one with the exact name or sends an error
    item_found = False
    if len(data) != 1:
        for i, item in enumerate(data):
            if item[0] == item_name:
                name, weight, cp_cost, description, categories, reqs, effs, rarity, tags = data[
                    i]
                item_found = True
        if not item_found:
            raise RuntimeError(
                f"""Your query return more than one items or no items at all, it returned {[item[0] for item in data]}, you search for {item_name}""")

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

    if "Weapon" in categories:
        atk_type = effects["Attack type"]
        damage = effects["Damage"]
        dmg_type = effects["Damage type"]

        if atk_type == "Melee":
            range = Units.Distance(int(effects["Range"]), "ft")
            return Melee(name, damage, dmg_type, range, weight, cp_cost, description, categories, requirements, effects, rarity, tags)

        elif atk_type == "Ranged":
            n_distance, l_distance = effects["Range"].split("/")
            n_distance = Units.Distance(int(n_distance), "ft")
            l_distance = Units.Distance(int(l_distance), "ft")
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
        assert n_distance.value <= l_distance.value, f"The normal range distance must shorter then the long distance, short: {n_distance}, long: {l_distance}"
        self.n_distance = n_distance
        self.l_distance = l_distance

        super().__init__(name, damage, dmg_type, weight, cost, description,
                         categories, requirements, effects, rarity, tags)

        if "Bow" in self.categories:
            self.ammunition = "Arrow"
        elif "Crossbow" in self.categories:
            self.ammunition = "Bolt"

# TODO Add system for spells
# TODO Update find method return class (as specific as possible)

# TODO Add the following items
