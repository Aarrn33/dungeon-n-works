import App.races as Races
import App.classes as Classes
import App.abilities as Abilities

# This class is used to create and manage a DnD character
class Character:
    def __init__(self, name: str, race: Races.Race, chr_class: Classes.Classes):
        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        self.level = 0
        
        #  Calculates the abilities using the standard method
        self.strength = Abilities.Ability("Strenght") # Physical power
        self.wisdow = Abilities.Ability("Wisdom") # Perception and Insight
        self.charisma = Abilities.Ability("Charisma") # Personnality strength
        self.dexterity = Abilities.Ability("Dexterity") # Agility
        self.intelligence = Abilities.Ability("Intelligence") # Reasoning and Memory
        self.constitution = Abilities.Ability("Constitution") # Endurance
        
        #TODO Incoporate races
        #TODO Incorporate classes
        #TODO Calculates skills