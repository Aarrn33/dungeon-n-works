import math
import App.Utilities.units as Units


class Coinage():
    def __init__(self, name: str, cp_value: int):
        self.name = name
        self.cp_value = cp_value
        auth_coins = ["Copper piece", "Silver piece",
                      "Electrum piece", "Gold piece", "Platinum piece"]
        assert self.name in auth_coins, f"The chosen coinage is not valid in DnD, the valid values are {auth_coins}"

    def convert(self, end_coinage):
        assert isinstance(
            end_coinage, Coinage), "The end_coinage provided is not valid"
        if isinstance(end_coinage, CP):
            # Adds shortcut if it is a conversion to cp
            return self.cp_value
        else:
            return find_coin([end_coinage.name, math.floor(self.cp_value/end_coinage.cp_value)])


class CP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.abbreviation = "cp"
        super().__init__("Copper piece", 1*number)


class SP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.abbreviation = "sp"
        super().__init__("Silver piece", 10*number)


class EP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.abbreviation = "ep"
        super().__init__("Electrum piece", 50*number)


class GP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.abbreviation = "gp"
        super().__init__("Gold piece", 100*number)


class PP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.abbreviation = "pp"
        super().__init__("Platinum piece", 1000*number)


# Addes easily accessible one coin objects
cp = CP()
sp = SP()
ep = EP()
gp = GP()
pp = PP()


def find_coin(coin_data):
    # coin_data = [coin_name, coin_number -> defaults to 0]
    if type(coin_data) == str:
        coin_data = [coin_data, 1]

    if coin_data[0] == "Copper piece":
        return CP(coin_data[1])
    elif coin_data[0] == "Silver piece":
        return SP(coin_data[1])
    elif coin_data[0] == "Electrum piece":
        return EP(coin_data[1])
    elif coin_data[0] == "Gold piece":
        return GP(coin_data[1])
    elif coin_data[0] == "Platinum piece":
        return PP(coin_data[1])
