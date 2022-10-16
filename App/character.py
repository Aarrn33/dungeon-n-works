import Utilities.dice as dice

# This class is used to create and manage a DnD character
class Character:
    def __init__(self, name, race, chr_class):
        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        
        #  Calculates the abilities
        self.strength = dice.roll(3, 6)
        self.wisdow = dice.roll(3, 6)
        self.charisma = dice.roll(3, 6)
        self.dexterity = dice.roll(3, 6)
        self.intelligence = dice.roll(3, 6)
        self.constitution = dice.roll(3, 6)