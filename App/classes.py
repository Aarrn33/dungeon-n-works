import App.Utilities.dice as dice
# A class that is used to create character classes


class Class:
    def __init__(self, name: str, hd: dice.Dice, st: list, skills: list, nbskills: int, chosen_skills: list = []):
        self.name = name  # Name of the class
        self.hd = hd  # Hit dice
        self.st = st  # Skills which have saving throws
        self.skills = skills  # Skills that the player can choose to have proficiency in
        self.nbskills = nbskills  # Number of those skills that the plyer can choose
        self.chosen_skills = chosen_skills
        if self.chosen_skills != []:
            for skill in self.chosen_skills:
                if skill not in self.skills:
                    self.chosen_skills = []
                    print(
                        "Something went wrong will trying to parse the proficient skills")
        if self.chosen_skills == []:  # If no chosen skills were provided, or if the previous test failed
            skills_to_choose = self.skills
            num_of_chosen_skills = 0

            while num_of_chosen_skills < nbskills:
                print(skills_to_choose)
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
    def __init__(self):
        self.name = "Fighter"
        self.hd = dice.d10
        self.st = ["Strength", "Constitution"]
        self.skills = ["Acrobatics", "Animal Handling", "Athletics",
                       "History", "Insight", "Intimidation", "Perception"]
        self.nbskills = 2
        super().__init__(self.name, self.hd, self.st, self.skills, self.nbskills)

# TODO Add Python classes for other DnD classes -> append find_class function


def find_class(class_data):
    # Changes the string provided to a 1 item list to better treat it
    if isinstance(class_data, str):
        class_data = [class_data]
    # Checks for all classes
    # TODO Check for other classes and subclasses
    if class_data[0] == "Fighter":
        return Fighter()
