import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills

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
        
        # Calculates skills
        # Strength dependants
        self.athletics = Skills.Skill("Athletics")
        # Dexterity dependants
        self.acrobatics = Skills.Skill("Acrobatics")
        self.sleight_of_hand = Skills.Skill("Sleight of Hand")
        self.stealth = Skills.Skill("Stealth")
        # Intelligence dependants
        self.arcana = Skills.Skill("Arcana")
        self.history = Skills.Skill("History")
        self.investigation = Skills.Skill("Investigation")
        self.nature = Skills.Skill("Nature")
        self.religion = Skills.Skill("Religion")
        # Wisdom dependants
        self.animal_handling = Skills.Skill("Animal Handling")
        self.insight = Skills.Skill("Insight")
        self.medicine = Skills.Skill("Medicine")
        self.perception = Skills.Skill("Perception")
        self.survival = Skills.Skill("Survival")
        # Charisma dependants
        self.deception = Skills.Skill("Deception")
        self.intimidation = Skills.Skill("Intiimidation")
        self.performance = Skills.Skill("Performance")
        self.persuasion = Skills.Skill("Persuasion")
        #TODO Incoporate races
        #TODO Incorporate classes
        