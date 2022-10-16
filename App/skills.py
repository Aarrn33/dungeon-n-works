import App.Abilities as Abilities

# A class that implements the skills deriving from the abilities
class Skill:
    def __init__(self, name: str, dependancy: Abilities.Ability):
        self.name = name
        self.dependancy = dependancy
        self.value = self.dependancy.value
        self.modifier = self.dependancy.modifier
