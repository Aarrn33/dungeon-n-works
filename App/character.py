import Utilities.dice as dice
import App.classes as Classes

# This class is used to create and manage a DnD character
class Character:
    def __init__(self, name: str, race, chr_class: Classes.Classes):
        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        self.level = 0
        
        #  Calculates the abilities using the standard method
        self.strength = dice.d6.roll(3) # Physical power
        self.wisdow = dice.d6.roll(3) # Perception and Insight
        self.charisma = dice.d6.roll(3) # Personnality strength
        self.dexterity = dice.d6.roll(3) # Agility
        self.intelligence = dice.d6.roll(3) # Reasoning and Memory
        self.constitution = dice.d6.roll(3) # Endurance