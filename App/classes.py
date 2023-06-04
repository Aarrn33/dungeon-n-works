import App.Utilities.dices as dices
# A class that is used to create character classes


class Class:
    def __init__(self, name: str, hd: dices.Dice, st: list, skills: list, nbskills: int, chosen_skills=[]):
        self.name = name  # Name of the class
        self.hd = hd  # Hit dice
        self.st = st  # Skills which have saving throws
        self.skills = skills  # Skills that the player can choose to have proficiency in
        self.nbskills = nbskills  # Number of those skills that the player can choose
        self.chosen_skills = chosen_skills  # The skill the user is actually proficient in
        # Checks if the user entered proficient skills are actually valid
        if self.chosen_skills != []:
            if type(self.chosen_skills) != list:
                self.chosen_skills = []
            for skill in self.chosen_skills:
                if skill not in self.skills:
                    self.chosen_skills = []
                    print(
                        "Something went wrong will trying to parse the proficient skills")
                    break
        if self.chosen_skills == []:  # If no chosen skills were provided, or if the previous test failed
            skills_to_choose = self.skills
            num_of_chosen_skills = 0
            while num_of_chosen_skills < nbskills:
                print(self.skills)
                skill_choice = input(
                    "Choose a skill amongst the ones shown to you before: ")
                try:
                    assert skill_choice in skills_to_choose
                    skills_to_choose.remove(skill_choice)
                    num_of_chosen_skills += 1
                    self.chosen_skills.append(skill_choice)
                except AssertionError:
                    print("You must choose a skill in the list provided to you")

        self.data = [name, self.chosen_skills]


class Fighter(Class):
    def __init__(self, chosen_skills: list = []):
        self.name = "Fighter"
        self.hd = dices.d10
        self.st = ["Strength", "Constitution"]
        self.skills = ["Acrobatics", "Animal Handling", "Athletics",
                       "History", "Insight", "Intimidation", "Perception", "Survival"]
        self.nbskills = 2
        self.chosen_skills = chosen_skills
        super().__init__(self.name, self.hd, self.st,
                         self.skills, self.nbskills, self.chosen_skills)


class Wizard(Class):
    def __init__(self, chosen_skills: list = []):
        self.name = "Wizard"
        self.hd = dices.d6
        self.st = ["Intelligence", "Wisdom"]
        self.skills = ["Arcana", "History", "Insight",
                       "Investigation", "Medicine", "Religion"]
        self.nbskills = 2
        self.chosen_skills = chosen_skills
        super().__init__(self.name, self.hd, self.st,
                         self.skills, self.nbskills, self.chosen_skills)

# TODO Add Python classes for other DnD classes -> append find_class function


def find_class(class_data):
    # Changes the string provided to a 1 item list to better treat it
    if isinstance(class_data, str):
        class_data = [class_data]
    # Checks for all classes
    if class_data[0] == "Fighter":
        if len(class_data) > 1:
            return Fighter(class_data[1])
        else:
            return Fighter()
    elif class_data[0] == "Wizard":
        if len(class_data) > 1:
            return Wizard(class_data[1])
        else:
            return Wizard()
    else:
        assert f"One should never reach this point unless the provided class is not valid. You provided this input: {class_data}"
