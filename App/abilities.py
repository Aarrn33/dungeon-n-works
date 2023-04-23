import App.Utilities.score2modifier as score2modifier
import App.Utilities.dice as dice
from math import floor

# A class that is used to define the abilities of a character


class Ability:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        self.modifier = score2modifier.score_2_modifier(self.value)

    def modify_value(self, factor: int):
        self.value += factor
        self.modifier = score2modifier.score_2_modifier(self.value)

    def modify_modifier(self, factor: int):
        self.modifier += factor
        self.value = floor((self.modifier*2)+10)

# Adds classes for each ability


class Strength(Ability):
    def __init__(self, value: int = dice.d6.roll(3)):
        self.name = "Strength"
        self.value = value
        super().__init__(self.name, self.value)


class Wisdom(Ability):
    def __init__(self, value: int = dice.d6.roll(3)):
        self.name = "Wisdom"
        self.value = value
        super().__init__(self.name, self.value)


class Charisma(Ability):
    def __init__(self, value: int = dice.d6.roll(3)):
        self.name = "Charisma"
        self.value = value
        super().__init__(self.name, self.value)


class Dexterity(Ability):
    def __init__(self, value: int = dice.d6.roll(3)):
        self.name = "Dexterity"
        self.value = value
        super().__init__(self.name, self.value)


class Intelligence(Ability):
    def __init__(self, value: int = dice.d6.roll(3)):
        self.name = "Intelligence"
        self.value = value
        super().__init__(self.name, self.value)


class Constitution(Ability):
    def __init__(self, value: int = dice.d6.roll(3)):
        self.name = "Constitution"
        self.value = value
        super().__init__(self.name, self.value)
