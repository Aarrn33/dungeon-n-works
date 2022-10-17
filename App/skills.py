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
    def __init__(self):
        self.name = "Athletics"
        self.dependancy = Abilities.Strength
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier

# Dexterity dependants
class Acrobatics(Skill):
    def __init__(self):
        self.name = "Acrobatics"
        self.dependancy = Abilities.Dexterity
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Sleight_of_Hand(Skill):
    def __init__(self):
        self.name = "Sleight of Hand"
        self.dependancy = Abilities.Dexterity
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Stealth(Skill):
    def __init__(self):
        self.name = "Stealth"
        self.dependancy = Abilities.Dexterity
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier

# Intelligence dependants
class Arcana(Skill):
    def __init__(self):
        self.name = "Arcana"
        self.dependancy = Abilities.Intelligence
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class History(Skill):
    def __init__(self):
        self.name = "History"
        self.dependancy = Abilities.Intelligence
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Investigation(Skill):
    def __init__(self):
        self.name = "Investigation"
        self.dependancy = Abilities.Intelligence
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Nature(Skill):
    def __init__(self):
        self.name = "Nature"
        self.dependancy = Abilities.Intelligence
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Religion(Skill):
    def __init__(self):
        self.name = "Religion"
        self.dependancy = Abilities.Intelligence
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier

# Wisdom dependants
class Animal_Handling(Skill):
    def __init__(self):
        self.name = "Animal Handling"
        self.dependancy = Abilities.Wisdom
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Insight(Skill):
    def __init__(self):
        self.name = "Insight"
        self.dependancy = Abilities.Wisdom
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Medicine(Skill):
    def __init__(self):
        self.name = "Medicine"
        self.dependancy = Abilities.Wisdom
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Perception(Skill):
    def __init__(self):
        self.name = "Perception"
        self.dependancy = Abilities.Wisdom
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Survival(Skill):
    def __init__(self):
        self.name = "Survival"
        self.dependancy = Abilities.Wisdom
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier

# Charisma dependats
class Deception(Skill):
    def __init__(self):
        self.name = "Deception"
        self.dependancy = Abilities.Charisma
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Intimidation(Skill):
    def __init__(self):
        self.name = "Intimidation"
        self.dependancy = Abilities.Charisma
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Performance(Skill):
    def __init__(self):
        self.name = "Performance"
        self.dependancy = Abilities.Charisma
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier
class Persuasion(Skill):
    def __init__(self):
        self.name = "Persuasion"
        self.dependancy = Abilities.Charisma
        super().__init__(self.name, self.dependancy)
        self.value = super().value
        self.modifier = super().modifier


#Adds classes per ability dependancy
class Strength_dep:
    def __init__(self):
        self.dependants = [Athletics]
class Dexterity_dep:
    def __init__(self):
        self.dependants = [Acrobatics, Sleight_of_Hand, Stealth]
class Intelligence_dep:
    def __init__(self):
        self.dependants = [Arcana, History, Investigation, Nature, Religion]
class Wisdom_dep:
    def __init__(self):
        self.dependants = [Animal_Handling, Insight, Medicine, Perception, Survival]
class Charisma_dep:
    def __init__(self):
        self.dependants = [Deception, Intimidation, Performance, Persuasion]