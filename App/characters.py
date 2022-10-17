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
        self.strength = Abilities.Strength() # Physical power
        self.wisdow = Abilities.Wisdom() # Perception and Insight
        self.charisma = Abilities.Charisma() # Personnality strength
        self.dexterity = Abilities.Dexterity() # Agility
        self.dexterity.__init__()
        print(self.dexterity)
        import inspect
        print(inspect.getmembers(self.dexterity, lambda a : not(inspect.isroutine(a))))
        self.intelligence = Abilities.Intelligence # Reasoning and Memory
        self.constitution = Abilities.Constitution # Endurance
        
        # Calculates default armor class
        # AC = 10 + dexterity
        self.ac = 10 + self.dexterity.modifier
        print(self.ac)
        
        # Calculates skills
        # Strength dependants
        self.athletics = Skills.Athletics
        # Dexterity dependants
        self.acrobatics = Skills.Acrobatics
        self.sleight_of_hand = Skills.Sleight_of_Hand
        self.stealth = Skills.Stealth
        # Intelligence dependants
        self.arcana = Skills.Arcana
        self.history = Skills.History
        self.investigation = Skills.Investigation
        self.nature = Skills.Nature
        self.religion = Skills.Religion
        # Wisdom dependants
        self.animal_handling = Skills.Animal_Handling
        self.insight = Skills.Insight
        self.medicine = Skills.Medicine
        self.perception = Skills.Perception
        self.survival = Skills.Survival
        # Charisma dependants
        self.deception = Skills.Deception
        self.intimidation = Skills.Intimidation
        self.performance = Skills.Performance
        self.persuasion = Skills.Persuasion
        
        #TODO Incorporate saving throws
        #TODO Incorporates races
        if self.race == Races.human:
            pass
        
        #TODO Incorporates classes
        #TODO Add inventory
