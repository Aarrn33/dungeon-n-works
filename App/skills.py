import App.abilities as Abilities
from math import floor

# A class that implements the skills deriving from the abilities


class Skill:
    def __init__(self, name: str, dependancy: Abilities.Ability, value: int):
        self.name = name
        self.dependancy = dependancy
        self.value = value
        if self.value <= 0:
            self.value = self.dependancy.value
            self.modifier = self.dependancy.modifier
        else:
            self.modifier = floor((self.value-10)/2)

    def modify_value(self, factor: int):
        self.value += factor
        self.modifier = floor((self.value-10)/2)

    def modify_modifier(self, factor: int):
        self.modifier += factor
        self.value = floor((self.modifier*2)+10)


# Adds classes for each skill
# Strength dependants
class Athletics(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Strength = Abilities.Strength()):
        self.name = "Athletics"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Dexterity dependants


class Acrobatics(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Dexterity = Abilities.Dexterity()):
        self.name = "Acrobatics"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Sleight_of_Hand(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Dexterity = Abilities.Dexterity()):
        self.name = "Sleight of Hand"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Stealth(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Dexterity = Abilities.Dexterity()):
        self.name = "Stealth"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Intelligence dependants


class Arcana(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Intelligence = Abilities.Intelligence()):
        self.name = "Arcana"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class History(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Intelligence = Abilities.Intelligence()):
        self.name = "History"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Investigation(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Intelligence = Abilities.Intelligence()):
        self.name = "Investigation"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Nature(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Intelligence = Abilities.Intelligence()):
        self.name = "Nature"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Religion(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Intelligence = Abilities.Intelligence()):
        self.name = "Religion"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Wisdom dependants


class Animal_Handling(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Wisdom = Abilities.Wisdom()):
        self.name = "Animal Handling"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Insight(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Wisdom = Abilities.Wisdom()):
        self.name = "Insight"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Medicine(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Wisdom = Abilities.Wisdom()):
        self.name = "Medicine"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Perception(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Wisdom = Abilities.Wisdom()):
        self.name = "Perception"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Survival(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Wisdom = Abilities.Wisdom()):
        self.name = "Survival"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)

# Charisma dependats


class Deception(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Charisma = Abilities.Charisma()):
        self.name = "Deception"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Intimidation(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Charisma = Abilities.Charisma()):
        self.name = "Intimidation"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Performance(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Charisma = Abilities.Charisma()):
        self.name = "Performance"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)


class Persuasion(Skill):
    def __init__(self, value: int = -1, dependancy: Abilities.Charisma = Abilities.Charisma()):
        self.name = "Persuasion"
        self.dependancy = dependancy
        self.value = value
        super().__init__(self.name, self.dependancy, self.value)
