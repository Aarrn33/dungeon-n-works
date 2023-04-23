import App.races as Races
import App.classes as Classes
import App.abilities as Abilities
import App.skills as Skills

# This class is used to create and manage a DnD character


class Character:
    def __init__(self, name: str, race: Races.Race, chr_class: Classes.Class):
        # Assigns main identifiers
        self.name = name
        self.race = race
        self.chr_class = chr_class
        self.level = 0
        self.inspiration = False
        self.pb = 2  # Proficiency bonus
        self.inventory = []

        #  Calculates the abilities using the standard method
        self.strength = Abilities.Strength()  # Physical power
        self.wisdom = Abilities.Wisdom()  # Perception and Insight
        self.charisma = Abilities.Charisma()  # Personnality strength
        self.dexterity = Abilities.Dexterity()  # Agility
        self.intelligence = Abilities.Intelligence()  # Reasoning and Memory
        self.constitution = Abilities.Constitution()  # Endurance

        # Calculates default armor class
        # AC = 10 + dexterity
        self.ac = 10 + self.dexterity.modifier

        # Calculates skills
        # Strength dependants
        dependancy = self.strength
        self.athletics = Skills.Athletics(dependancy)
        # Dexterity dependants
        dependancy = self.dexterity
        self.acrobatics = Skills.Acrobatics(dependancy)
        self.sleight_of_hand = Skills.Sleight_of_Hand(dependancy)
        self.stealth = Skills.Stealth(dependancy)
        # Intelligence dependants
        dependancy = self.intelligence
        self.arcana = Skills.Arcana(dependancy)
        self.history = Skills.History(dependancy)
        self.investigation = Skills.Investigation(dependancy)
        self.nature = Skills.Nature(dependancy)
        self.religion = Skills.Religion(dependancy)
        # Wisdom dependants
        dependancy = self.wisdom
        self.animal_handling = Skills.Animal_Handling(dependancy)
        self.insight = Skills.Insight(dependancy)
        self.medicine = Skills.Medicine(dependancy)
        self.perception = Skills.Perception(dependancy)
        self.survival = Skills.Survival(dependancy)
        # Charisma dependants
        dependancy = self.charisma
        self.deception = Skills.Deception(dependancy)
        self.intimidation = Skills.Intimidation(dependancy)
        self.performance = Skills.Performance(dependancy)
        self.persuasion = Skills.Persuasion(dependancy)

        # TODO Incorporate saving throws
        # TODO Incorporates races
        if type(self.race) == Races.Dragonborn:
            self.strength.modify_value(2)
            self.charisma.modify_value(1)
            # TODO Add draconic ancestry mechanic to incorporate fire breath

        # TODO Incorporates classes
        # TODO Add movement speed

        self.data = [self.name, self.race, self.chr_class, self.level, self.inspiration, self.pb, self.inventory, self.strength.value,
                     self.wisdom.value, self.charisma.value, self.dexterity.value, self.intelligence.value, self.constitution.value]

    def save_char(self):
        file_name = self.name+".txt"
        with open(file_name, "w"):
            pass
