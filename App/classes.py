import App.Utilities.dices as dices

# A class that is used to create character classes


class Class:
    def __init__(self, name: str, hd: dices.Dice, st: list, skills: list, nbskills: int, chosen_skills: list = [], ask_starting_equipment: bool = True):
        self.name = name  # Name of the class
        self.hd = hd  # Hit dice
        self.st = st  # Skills which have saving throws
        self.skills = skills  # Skills that the player can choose to have proficiency in
        self.nbskills = nbskills  # Number of those skills that the player can choose
        # The skill the user is actually proficient in
        self.chosen_skills = chosen_skills[:]
        # Flag to know if the starting equipment has been implemented
        self.ask_starting_equipment = ask_starting_equipment

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
            print(self.skills)
            skills_to_choose = self.skills
            num_of_chosen_skills = 0
            while num_of_chosen_skills < nbskills:
                skill_choice = input(
                    "Choose a skill amongst the ones shown to you before that you haven't chosen yet: \n")
                try:
                    assert skill_choice in skills_to_choose
                    skills_to_choose.remove(skill_choice)
                    num_of_chosen_skills += 1
                    self.chosen_skills = self.chosen_skills.append(
                        skill_choice)
                except AssertionError:
                    print(
                        "You must choose a skill in the list provided to you and that you haven't previously chosen")

        self.data = [name, self.chosen_skills, ask_starting_equipment]

# TODO Add starting equipment

# args
# if choice
# [option 1, option 2, ...]
# if forced : use tuple (quantity, "name") or (quantity, "Pack", "name_of_the_pack")
# options
# single item : tuple (quantity, "name") (searchable in item db)
# TODO add pack (ie. explorer's pack)
# packs : tuple (quantity, "Pack", "name_of_the_pack") to take care of in body function
# criteria : list  ["crit 1", "crit 2"]


def get_starting_equipment(*args):
    for line in args:
        # If there is a choice to make
        if isinstance(line, list):
            print(
                "Choose amongst the following choices by using the number of the item you want:")
            for index, value in enumerate(line):
                # If it is a single item
                if isinstance(value, tuple) and len(value) == 2:
                    f_value = value[-1]
                # If it is a pack
                elif isinstance(value, tuple) and len(value) == 3:
                    f_value = value[-1]
                # If it is based on a criteria (ie. a martial melee weapon)
                # TODO implement criterias
                elif isinstance(value, list):
                    pass
                else:
                    raise RuntimeError(
                        f"The provided value: {value} is interpretable for starting equipment")
                print(f"({index+1}) {f_value}")
        # If there is no choice to make
        elif isinstance(line, tuple):
            pass
        else:
            raise RuntimeError(
                f"{line} is not a valid argument for starting equipment")
