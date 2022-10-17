import App.Utilities.score2modifier as score2modifier
import App.Utilities.dice as dice

# A class that is used to define the abilities of a character
class Ability:
    def __init__(self, name: str):
        self.name = name
        self.value = dice.d6.roll(3)
        self.modifier = score2modifier.score_2_modifier(self.value)
        
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
        self.value = self.value
        self.modifier = self.modifier

class Intelligence(Ability):
    def __init__(self):
        self.name = "Intelligence"
        super().__init__(self.name)
        
class Constitution(Ability):
    def __init__(self):
        self.name = "Constitution"
        super().__init__(self.name)
        
class Test_ability(Ability):
    def __init__(self):
        super().__init__("Test_ability")