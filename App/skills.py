import App.abilities as Abilities
import App.Utilities.score2modifier as score2modifier
from math import floor

# A class that implements the skills deriving from the abilities
class Skill:
    def __init__(self, name: str, dependancy: Abilities.Ability):
        self.name = name
        self.dependancy = dependancy
        self.value = self.dependancy.value
        self.modifier = self.dependancy.modifier
        
    def modify_value(self, factor: int):
        self.value += factor
        self.modifier = score2modifier.score_2_modifier(self.value)
    
    def modify_modifier(self, factor: int):
        self.modifier += factor
        self.value = floor((self.modifier*2)+10)


# Adds classes for each skill
# Strength dependants
class Athletics(Skill):
    def __init__(self, dependancy: Abilities.Strength()):
        self.name = "Athletics"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)

# Dexterity dependants
class Acrobatics(Skill):
    def __init__(self, dependancy: Abilities.Dexterity()):
        self.name = "Acrobatics"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Sleight_of_Hand(Skill):
    def __init__(self, dependancy: Abilities.Dexterity()):
        self.name = "Sleight of Hand"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Stealth(Skill):
    def __init__(self, dependancy: Abilities.Dexterity()):
        self.name = "Stealth"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)

# Intelligence dependants
class Arcana(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Arcana"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class History(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "History"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Investigation(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Investigation"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Nature(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Nature"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Religion(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Religion"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)

# Wisdom dependants
class Animal_Handling(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Animal Handling"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Insight(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Insight"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Medicine(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Medicine"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Perception(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Perception"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Survival(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Survival"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)

# Charisma dependats
class Deception(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Deception"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Intimidation(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Intimidation"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Performance(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Performance"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
class Persuasion(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Persuasion"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)


#Adds classes per ability dependancy
class Strength_dep:
    def __init__(self):
        self.dependants = [Athletics()]
class Dexterity_dep:
    def __init__(self):
        self.dependants = [Acrobatics(), Sleight_of_Hand(), Stealth()]
class Intelligence_dep:
    def __init__(self):
        self.dependants = [Arcana(), History(), Investigation(), Nature(), Religion()]
class Wisdom_dep:
    def __init__(self):
        self.dependants = [Animal_Handling(), Insight(), Medicine(), Perception(), Survival()]
class Charisma_dep:
    def __init__(self):
        self.dependants = [Deception(), Intimidation(), Performance(), Persuasion()]