import Utilities.dice as dice
import App.classes as Classes
import App.abilities as Abilities

# This class is used to create and manage a DnD character
class Character:
    def __init__(self, name: str, race, chr_class: Classes.Classes):
        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        self.level = 0
        
        #  Calculates the abilities using the standard method
        self.strength = Abilities("Strenght") # Physical power
        self.wisdow = Abilities("Wisdom") # Perception and Insight
        self.charisma = Abilities("Charisma") # Personnality strength
        self.dexterity = Abilities("Dexterity") # Agility
        self.intelligence = Abilities("Intelligence") # Reasoning and Memory
        self.constitution = Abilities("Constitution") # Endurance