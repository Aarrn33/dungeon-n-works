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
    def __init__(self):
        self.name = "Athletics"
        self.dependancy = Abilities.Strength()
        super().__init__(self.name, self.dependancy)

# Dexterity dependants


class Acrobatics(Skill):
    def __init__(self):
        self.name = "Acrobatics"
        self.dependancy = Abilities.Dexterity()
        super().__init__(self.name, self.dependancy)


class Sleight_of_Hand(Skill):
    def __init__(self):
        self.name = "Sleight of Hand"
        self.dependancy = Abilities.Dexterity()
        super().__init__(self.name, self.dependancy)


class Stealth(Skill):
    def __init__(self):
        self.name = "Stealth"
        self.dependancy = Abilities.Dexterity()
        super().__init__(self.name, self.dependancy)

# Intelligence dependants


class Arcana(Skill):
    def __init__(self):
        self.name = "Arcana"
        self.dependancy = Abilities.Intelligence()
        super().__init__(self.name, self.dependancy)


class History(Skill):
    def __init__(self):
        self.name = "History"
        self.dependancy = Abilities.Intelligence()
        super().__init__(self.name, self.dependancy)


class Investigation(Skill):
    def __init__(self):
        self.name = "Investigation"
        self.dependancy = Abilities.Intelligence()
        super().__init__(self.name, self.dependancy)


class Nature(Skill):
    def __init__(self):
        self.name = "Nature"
        self.dependancy = Abilities.Intelligence()
        super().__init__(self.name, self.dependancy)


class Religion(Skill):
    def __init__(self):
        self.name = "Religion"
        self.dependancy = Abilities.Intelligence()
        super().__init__(self.name, self.dependancy)

# Wisdom dependants


class Animal_Handling(Skill):
    def __init__(self):
        self.name = "Animal Handling"
        self.dependancy = Abilities.Wisdom()
        super().__init__(self.name, self.dependancy)


class Insight(Skill):
    def __init__(self):
        self.name = "Insight"
        self.dependancy = Abilities.Wisdom()
        super().__init__(self.name, self.dependancy)


class Medicine(Skill):
    def __init__(self):
        self.name = "Medicine"
        self.dependancy = Abilities.Wisdom()
        super().__init__(self.name, self.dependancy)


class Perception(Skill):
    def __init__(self):
        self.name = "Perception"
        self.dependancy = Abilities.Wisdom()
        super().__init__(self.name, self.dependancy)


class Survival(Skill):
    def __init__(self):
        self.name = "Survival"
        self.dependancy = Abilities.Wisdom()
        super().__init__(self.name, self.dependancy)

# Charisma dependats


class Deception(Skill):
    def __init__(self):
        self.name = "Deception"
        self.dependancy = Abilities.Charisma()
        super().__init__(self.name, self.dependancy)


class Intimidation(Skill):
    def __init__(self):
        self.name = "Intimidation"
        self.dependancy = Abilities.Charisma()
        super().__init__(self.name, self.dependancy)


class Performance(Skill):
    def __init__(self):
        self.name = "Performance"
        self.dependancy = Abilities.Charisma()
        super().__init__(self.name, self.dependancy)


class Persuasion(Skill):
    def __init__(self):
        self.name = "Persuasion"
        self.dependancy = Abilities.Charisma()
        super().__init__(self.name, self.dependancy)
