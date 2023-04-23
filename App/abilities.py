import App.Utilities.score2modifier as score2modifier
import App.Utilities.dice as dice
from math import floor

# A class that is used to define the abilities of a character
class Ability:
    def __init__(self, name: str):
        self.name = name
        self.value = dice.d6.roll(3)
        self.modifier = score2modifier.score_2_modifier(self.value)
        
    def modify_value(self, factor: int):
        self.value += factor
        self.modifier = score2modifier.score_2_modifier(self.value)
    
    def modify_modfier(self, factor: int):
        self.modifier += factor
        self.value = floor((self.modifier*2)+10)
        
#Adds classes for each ability
class Strength(Ability):
    def __init__(self):
        self.name = "Strength"
        super().__init__(self.name)
        
class Wisdom(Ability):
    def __init__(self):
        self.name = "Wisdom"
        super().__init__(self.name)
        
class Charisma(Ability):
    def __init__(self):
        self.name = "Charisma"
        super().__init__(self.name)

class Dexterity(Ability):
    def __init__(self):
        self.name = "Dexterity"
        super().__init__(self.name)

class Intelligence(Ability):
    def __init__(self):
        self.name = "Intelligence"
        super().__init__(self.name)
        
class Constitution(Ability):
    def __init__(self):
        self.name = "Constitution"
        super().__init__(self.name)