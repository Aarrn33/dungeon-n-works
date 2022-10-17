import App.abilities as Abilities

# A class that implements the skills deriving from the abilities
class Skill:
    def __init__(self, name: str, dependancy: Abilities.Ability):
        self.name = name
        self.dependancy = dependancy
        self.value = self.dependancy.value
        self.modifier = self.dependancy.modifier


# Adds classes for each skill
# Strength dependants
class Athletics(Skill):
    def __init__(self, dependancy: Abilities.Strength()):
        self.name = "Athletics"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier

# Dexterity dependants
class Acrobatics(Skill):
    def __init__(self, dependancy: Abilities.Dexterity()):
        self.name = "Acrobatics"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Sleight_of_Hand(Skill):
    def __init__(self, dependancy: Abilities.Dexterity()):
        self.name = "Sleight of Hand"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Stealth(Skill):
    def __init__(self, dependancy: Abilities.Dexterity()):
        self.name = "Stealth"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier

# Intelligence dependants
class Arcana(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Arcana"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class History(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "History"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Investigation(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Investigation"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Nature(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Nature"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Religion(Skill):
    def __init__(self, dependancy: Abilities.Intelligence()):
        self.name = "Religion"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier

# Wisdom dependants
class Animal_Handling(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Animal Handling"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Insight(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Insight"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Medicine(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Medicine"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Perception(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Perception"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Survival(Skill):
    def __init__(self, dependancy: Abilities.Wisdom()):
        self.name = "Survival"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier

# Charisma dependats
class Deception(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Deception"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Intimidation(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Intimidation"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Performance(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Performance"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier
class Persuasion(Skill):
    def __init__(self, dependancy: Abilities.Charisma()):
        self.name = "Persuasion"
        self.dependancy = dependancy
        super().__init__(self.name, self.dependancy)
        self.value = self.value
        self.modifier = self.modifier


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