import App.Utilities.shapes as Shapes
import App.items as Items

# A class that is used to implement the race system
class Race:
    def __init__(self, name: str):
        self.name = name
        
# Classes incorporating races
class Dragonborn(Race):
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        super().__init__(self.name)
        
        # This section is used to determined the caracteristics of the draconic ancestry capa
        # Checks if it is a valid color
        self.color = color.lower()
        assert self.color in ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"], "The color entered is not valid for a dragonborn"
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
            raise RuntimeError("The color entered is not valid for a dragonborn")
        
        # Defines the size and shape of the breath
        if self.color in ["black", "blue", "brass", "bronze", "copper"]:
            self.shape = Shapes.Rectangle(30, 5)
        elif self.color in ["gold", "green", "red", "silver", "white"]:
            self.shape = Shapes.Cone(15)
        else:
            raise RuntimeError("The color entered is not valid for a dragonborn")
        
        # Defines the save to perform in order to resist the attack
        if self.color in ["black", "blue", "brass", "bronze", "copper", "gold", "red"]:
            self.save_ability = "Dexterity"
        elif self.color in ["green", "silver", "white"]:
            self.save_abilty = "Constitution"
        else:
            raise RuntimeError("The color entered is not valid for a dragonborn")
        
        #TODO: Register the breath as an item (requires level correlation)
        #TODO: Add damage resistance
        #TODO: Add language
        

# TODO create a classes for the races below
dwarf = Race("Dwarf")
elf = Race("Elf")
gnome = Race("Gnome")
half_elf = Race("Half-Elf")
halfin = Race("Halfing")
half_orc = Race("Half-Orc")
human = Race("Human")
tiefling = Race("Tiefling")