import Utilities.dice as dice

# This class is used to create and manage a DnD character
class Character:
    def __init__(self, name, race, chr_class):
        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        self.level = 0
        
        #  Calculates the abilities using the standard method
        self.strength = dice.roll(3, 6) # Physical power
        self.wisdow = dice.roll(3, 6) # Perception and Insight
        self.charisma = dice.roll(3, 6) # Personnality strength
        self.dexterity = dice.roll(3, 6) # Agility
        self.intelligence = dice.roll(3, 6) # Reasoning and Memory
        self.constitution = dice.roll(3, 6) # Endurance