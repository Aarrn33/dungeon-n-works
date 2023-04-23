import App.abilities as Abilities
import App.Utilities.score2modifier as score2modifier
from math import floor

# A class that implements the skills deriving from the abilities


class Skill:
    def __init__(self, name: str, dependancy: Abilities.Ability, value: int):
        self.name = name
        self.dependancy = dependancy
        self.value = value
        if self.value == -1:
            self.value = self.dependancy.value
            self.modifier = self.dependancy.modifier
        else:
            self.modifier = score2modifier.score_2_modifier(self.value)

    def modify_value(self, factor: int):
        self.value += factor
        self.modifier = score2modifier.score_2_modifier(self.value)

    def modify_modifier(self, factor: int):
        self.modifier += factor
        self.value = floor((self.modifier*2)+10)


# Adds classes for each skill
# Strength dependants
class Athletics(Skill):
    def __init__(self, value: int = -1):
        self.name = "Athletics"
        self.dependancy = Abilities.Strength()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Dexterity dependants


class Acrobatics(Skill):
    def __init__(self, value: int = -1):
        self.name = "Acrobatics"
        self.dependancy = Abilities.Dexterity()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Sleight_of_Hand(Skill):
    def __init__(self, value: int = -1):
        self.name = "Sleight of Hand"
        self.dependancy = Abilities.Dexterity()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Stealth(Skill):
    def __init__(self, value: int = -1):
        self.name = "Stealth"
        self.dependancy = Abilities.Dexterity()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Intelligence dependants


class Arcana(Skill):
    def __init__(self, value: int = -1):
        self.name = "Arcana"
        self.dependancy = Abilities.Intelligence()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class History(Skill):
    def __init__(self, value: int = -1):
        self.name = "History"
        self.dependancy = Abilities.Intelligence()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Investigation(Skill):
    def __init__(self, value: int = -1):
        self.name = "Investigation"
        self.dependancy = Abilities.Intelligence()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Nature(Skill):
    def __init__(self, value: int = -1):
        self.name = "Nature"
        self.dependancy = Abilities.Intelligence()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Religion(Skill):
    def __init__(self, value: int = -1):
        self.name = "Religion"
        self.dependancy = Abilities.Intelligence()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Wisdom dependants


class Animal_Handling(Skill):
    def __init__(self, value: int = -1):
        self.name = "Animal Handling"
        self.dependancy = Abilities.Wisdom()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Insight(Skill):
    def __init__(self, value: int = -1):
        self.name = "Insight"
        self.dependancy = Abilities.Wisdom()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Medicine(Skill):
    def __init__(self, value: int = -1):
        self.name = "Medicine"
        self.dependancy = Abilities.Wisdom()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Perception(Skill):
    def __init__(self, value: int = -1):
        self.name = "Perception"
        self.dependancy = Abilities.Wisdom()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Survival(Skill):
    def __init__(self, value: int = -1):
        self.name = "Survival"
        self.dependancy = Abilities.Wisdom()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Charisma dependats


class Deception(Skill):
    def __init__(self, value: int = -1):
        self.name = "Deception"
        self.dependancy = Abilities.Charisma()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Intimidation(Skill):
    def __init__(self, value: int = -1):
        self.name = "Intimidation"
        self.dependancy = Abilities.Charisma()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Performance(Skill):
    def __init__(self, value: int = -1):
        self.name = "Performance"
        self.dependancy = Abilities.Charisma()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Persuasion(Skill):
    def __init__(self, value: int = -1):
        self.name = "Persuasion"
        self.dependancy = Abilities.Charisma()
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)
