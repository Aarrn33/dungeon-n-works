# A class that is used to create classes
class Classes:
    def __init__(self, name: str, hd: int, st: list, skills: list, nbskills: int):
        self.name = name #N Name of the class
        self.hd = hd # Hit dice
        self.st = st # Skills which have saving throws
        self.skills = skills # Skills that the player can choose to have proficiency in
        self.nbskills = nbskills # Number of those skills that the plyer can choose