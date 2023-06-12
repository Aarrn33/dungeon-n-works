import App.classes as Classes
import App.Utilities.dices as dices
import App.items as Items


class Barbarian(Classes.Class):
    def __init__(self, chosen_skills: list = [], ask_starting_equipment: bool = True):
        self.name = "Barbarian"
        self.hd = dices.d12
        self.st = ["Strength", "Constitution"]
        self.skills = ["Animal Handling", "Athletics",
                       "Intimidation", "Nature", "Perception", "Survival"]
        self.nbskills = 2
        self.chosen_skills = chosen_skills[:]

        if ask_starting_equipment:
            self.choose_starting_equipment()

        super().__init__(self.name, self.hd, self.st,
                         self.skills, self.nbskills, self.chosen_skills)

        del chosen_skills

    def choose_starting_equipment(self):
        # ["A greataxe", "Any martial melee weapon"], ["Two handaxes", "Any simple weapon"], "An explorer's pack", "Four javelins"]
        choices = []
        # Chooses starting equipment
        print(
            "Choose amongst the following choices by using the number of the item you want:")
        print("Choice 1")
        while True:
            choice = int(
                input("(1) A greataxe or (2) Any martial melee weapon: \n"))
            if choice == 1:
                choices.append(Items.find("Greataxe"))
                break
            elif choice == 2:
                try:
                    choice = Items.find(
                        input("Please enter a martial melee weapon: \n"))
                except RuntimeError:
                    print(
                        "The item you searched for is currently not implemented or your search returned multiple results")
                    continue
                if "Martial" in choice.tags and choice.effects["Attack type"] == "Melee":
                    choices.append(choice)
                    break
                else:
                    print("Please enter a valid martial melee weapon")
            else:
                print("Please choose a valid option")

        print("Choice 2")
        while True:
            choice = int(
                input("(1) Two handaxes or (2) Any simple weapon: \n"))
            if choice == 1:
                choices.extend([Items.find("Handaxe"), Items.find("Handaxe")])
                break
            elif choice == 2:
                try:
                    choice = Items.find(
                        input("Please enter a simple weapon: \n"))
                except RuntimeError:
                    print(
                        "The item you searched for is currently not implemented or your search returned multiple results")
                    continue
                if "Simple" in choice.tags and "Weapon" in choice.categories:
                    choices.append(choice)
                    break
                else:
                    print("Please enter a valid simple weapon")
            else:
                print("Please choose a valid option")
        # TODO Add explorer's pack
        choices.extend([Items.find("Javelin"), Items.find(
            "Javelin"), Items.find("Javelin"), Items.find("Javelin")])

        self.starting_equipment = choices
