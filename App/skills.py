# A class that implements the skills deriving from the abilities
class Skill:
    def __init__(self, name: str):
        self.name = name

# Strength dependants
athletics = Skill("Athletics")
# Dexterity dependants
acrobatics = Skill("Acrobatics")
sleight_of_hand = Skill("Sleight of Hand")
stealth = Skill("Stealth")
# Intelligence dependants
arcana = Skill("Arcana")
history = Skill("History")
investigation = Skill("Investigation")
nature = Skill("Nature")
religion = Skill("Religion")
# Wisdom dependants
animal_handling = Skill("Animal Handling")
insight = Skill("Insight")
medicine = Skill("Medicine")
perception = Skill("Perception")
survival = Skill("Survival")
# Charisma dependants
deception = Skill("Deception")
intimidation = Skill("Intiimidation")
performance = Skill("Performance")
persuasion = Skill("Persuasion")