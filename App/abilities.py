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
        self.value = super().value
        self.modifier = super().modifier
        
class Wisdom(Ability):
    def __init__(self):
        self.name = "Wisdom"
        super().__init__(self.name)
        self.value = super().value
        self.modifier = super().modifier
        
class Charisma(Ability):
    def __init__(self):
        self.name = "Charisma"
        super().__init__(self.name)
        self.value = super().value
        self.modifier = super().modifier

class Dexterity(Ability):
    def __init__(self):
        self.name = "Dexterity"
        super().__init__(self.name)
        self.value = super().self.value
        self.modifier = super().self.modifier
        print(self.modifier)

class Intelligence(Ability):
    def __init__(self):
        self.name = "Intelligence"
        super().__init__(self.name)
        self.value = super().value
        self.modifier = super().modifier
        
class Constitution(Ability):
    def __init__(self):
        self.name = "Constitution"
        super().__init__(self.name)
        self.value = super().value
        self.modifier = super().modifier