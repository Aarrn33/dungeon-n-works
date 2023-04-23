import App.Utilities.shapes as Shapes
import App.items as Items

# A class that is used to implement the race system


class Race:
    def __init__(self, name: str, variant: str = "standard"):
        self.name = name
        self.variant = variant
        self.data = [name, variant]

# Classes incorporating races


class Dragonborn(Race):
    def __init__(self, color: str):
        self.name = "Dragonborn"
        super().__init__(self.name)
        self.data = [self.name, self.color]

        # This section is used to determined the caracteristics of the draconic ancestry capa
        # Checks if it is a valid color
        self.color = color.lower()
        assert self.color in ["black", "blue", "brass", "bronze", "copper", "gold", "green",
                              "red", "silver", "white"], "The color entered is not valid for a dragonborn"
        # Definies the damage type of the capa
        if self.color in ["black", "copper"]:
            self.dmg_type = "acid"
        elif self.color in ["blue", "bronze"]:
            self.dmg_type = "lightning"
        elif self.color in ["brass", "gold", "red"]:
            self.dmg_type = "fire"
        elif self.color == "green":
            self.dmg_type = "poison"
        elif self.color in ["silver", "white"]:
            self.dmg_type == "cold"
        else:
            raise RuntimeError(
                "The color entered is not valid for a dragonborn")

        # Defines the size and shape of the breath
        if self.color in ["black", "blue", "brass", "bronze", "copper"]:
            self.shape = Shapes.Rectangle(30, 5)
        elif self.color in ["gold", "green", "red", "silver", "white"]:
            self.shape = Shapes.Cone(15)
        else:
            raise RuntimeError(
                "The color entered is not valid for a dragonborn")

        # Defines the save to perform in order to resist the attack
        if self.color in ["black", "blue", "brass", "bronze", "copper", "gold", "red"]:
            self.save_ability = "Dexterity"
        elif self.color in ["green", "silver", "white"]:
            self.save_abilty = "Constitution"
        else:
            raise RuntimeError(
                "The color entered is not valid for a dragonborn")

        # TODO: Register the breath as an item (requires level correlation)
        # TODO: Add damage resistance
        # TODO: Add language


# TODO create a classes for the races below -> append find_race function
class Dwarf(Race):
    def __init__(self):
        self.name = "Dwarf"
        super().__init__(self.name)


class Elf(Race):
    def __init__(self):
        self.name = "Elf"
        super().__init__(self.name)


class Gnome(Race):
    def __init__(self):
        self.name = "Gnome"
        super().__init__(self.name)


class HalfElf(Race):
    def __init__(self):
        self.name = "Half-Elf"
        super().__init__(self.name)


class Halfin(Race):
    def __init__(self):
        self.name = "Halfin"
        super().__init__(self.name)


class HalfOrc(Race):
    def __init__(self):
        self.name = "Half-Orc"
        super().__init__(self.name)


class Human(Race):
    def __init__(self):
        self.name = "Human"
        super().__init__(self.name)


class Tiefling(Race):
    def __init__(self):
        self.name = "Tiefling"
        super().__init__(self.name)


def find_race(race_data):
    if race_data[0] == "Dragonborn":
        return Dragonborn(race_data[1])
    elif race_data[0] == "Dwarf":
        return Dwarf()
    elif race_data[0] == "Elf":
        return Elf()
    elif race_data[0] == "Gnome":
        return Gnome()
    elif race_data[0] == "Half-Elf":
        return HalfElf()
    elif race_data[0] == "Halfin":
        return Halfin()
    elif race_data[0] == "Half-Orc":
        return HalfOrc()
    elif race_data[0] == "Human":
        return Human()
    elif race_data[0] == "Tiefling":
        return Tiefling()
