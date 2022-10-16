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
        self.inspiration = 0
        self.pb = 2 # Proficiency bonus
        
        #  Calculates the abilities using the standard method
        self.strength = Abilities.Ability("Strenght") # Physical power
        self.wisdow = Abilities.Ability("Wisdom") # Perception and Insight
        self.charisma = Abilities.Ability("Charisma") # Personnality strength
        self.dexterity = Abilities.Ability("Dexterity") # Agility
        self.intelligence = Abilities.Ability("Intelligence") # Reasoning and Memory
        self.constitution = Abilities.Ability("Constitution") # Endurance
        
        # Calculates default armor class
        # AC = 10 + dexterity
        self.ac = 10 + self.dexterity.modifier
        
        # Calculates skills
        # Strength dependants
        dependancy = self.strength
        self.athletics = Skills.Skill("Athletics", dependancy)
        # Dexterity dependants
        dependancy = self.dexterity
        self.acrobatics = Skills.Skill("Acrobatics", dependancy)
        self.sleight_of_hand = Skills.Skill("Sleight of Hand", dependancy)
        self.stealth = Skills.Skill("Stealth", dependancy)
        # Intelligence dependants
        dependancy = self.intelligence
        self.arcana = Skills.Skill("Arcana", dependancy)
        self.history = Skills.Skill("History", dependancy)
        self.investigation = Skills.Skill("Investigation", dependancy)
        self.nature = Skills.Skill("Nature", dependancy)
        self.religion = Skills.Skill("Religion", dependancy)
        # Wisdom dependants
        dependancy = self.wisdow
        self.animal_handling = Skills.Skill("Animal Handling", dependancy)
        self.insight = Skills.Skill("Insight", dependancy)
        self.medicine = Skills.Skill("Medicine", dependancy)
        self.perception = Skills.Skill("Perception", dependancy)
        self.survival = Skills.Skill("Survival", dependancy)
        # Charisma dependants
        dependancy = self.charisma
        self.deception = Skills.Skill("Deception", dependancy)
        self.intimidation = Skills.Skill("Intiimidation", dependancy)
        self.performance = Skills.Skill("Performance", dependancy)
        self.persuasion = Skills.Skill("Persuasion", dependancy)
        
        #TODO Incorporate saving throws
        #TODO Incorporates races
        if self.race == Races.human:
            pass
        
        #TODO Incorporates classes
        #TODO Add inventory
