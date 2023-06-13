import App.Utilities.dices as dices
import App.Utilities.inventory as inventory
from App.Utilities.Searches.find_pack import find_pack

# A class that is used to create character classes


class Class:
    def __init__(
        self,
        name: str,
        hd: dices.Dice,
        st: list[str],
        skills: list[str],
        nbskills: int,
        starting_equipment: inventory.Inventory,
        chosen_skills: list[str] = [],
        ask_starting_equipment: bool = True,
    ):
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
                    self.chosen_skills.append(skill_choice)
                except AssertionError:
                    print(
                        "You must choose a skill in the list provided to you and that you haven't previously chosen")

        if ask_starting_equipment:
            self.chosen_starting_equipment = get_starting_equipment(
                starting_equipment)
            self.ask_starting_equipment = False

        self.data = [name, self.chosen_skills, ask_starting_equipment]

# TODO Update classes to fit the wizard style

# args
# if choice
# [option 1, option 2, ...]
# if forced : use tuple (quantity, "name") or ("name_of_the_pack") or (["crit1", "crit2"])
# options
# single item : tuple (quantity, "name") (searchable in item db)
# packs : str "name_of_the_pack"
# TODO implement criterias
# criteria : list  ["crit 1", "crit 2"]


def get_starting_equipment(args: list[(list | tuple)]):
    equipment = inventory.Inventory()
    for line in args:
        # If there is a choice to make
        if isinstance(line, list):
            print(
                "Choose amongst the following choices by using the number of the item you want:")
            for index, value in enumerate(line):
                # If it is a single item
                if isinstance(value, tuple):
                    f_value = value[-1]
                # If it is a pack
                elif isinstance(value, str):
                    f_value = value
                # If it is based on a criteria (ie. a martial melee weapon)
                elif isinstance(value, list):
                    pass
                else:
                    raise RuntimeError(
                        f"The provided value: {value} is not interpretable for starting equipment")
                print(f"({index+1}) {f_value}")
            choice = int(
                input("Enter the number corresponding to your choice: \n"))
            # To match the index
            choice -= 1
            choice = line[choice]
            # If it is a single item
            if isinstance(choice, tuple) and len(choice) == 2:
                quantity, name = choice
                equipment += inventory.list2inv([(name, quantity)])
            # If it is a pack
            elif isinstance(choice, str):
                equipment += find_pack(choice)
            # If it is based on a criteria
            elif isinstance(choice, list):
                pass
            else:
                raise RuntimeError(
                    f"The provided value: {choice} is not interpretable for starting equipment")
        # If there is no choice to make
        elif isinstance(line, tuple):
            choice = line[0]
            # If it is a single item
            if isinstance(choice, tuple) and len(choice) == 2:
                quantity, name = choice
                equipment += inventory.list2inv([(name, quantity)])
            # If it is a pack
            elif isinstance(choice, str):
                equipment += find_pack(choice)
            # If it is based on a criteria
            elif isinstance(line, list):
                pass
            else:
                raise RuntimeError(
                    f"The provided value: {line} is not interpretable for starting equipment")
        else:
            raise RuntimeError(
                f"{line} is not a valid argument for starting equipment")
    return equipment
