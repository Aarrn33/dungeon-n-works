import math
import App.items as Items


class Coinage(Items.Stackable):
    def __init__(self, cp_value: int, name: str):
        self.cp_value = cp_value
        self.name = name
        assert self.name in ["Copper piece", "Silver piece", "Electrum piece", "Gold piece",
                             "Platinum piece"], "The chosen coinage is not valid in DnD"
        super().__init__(self.name)

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
        self.name = "Copper piece"
        self.abbreviation = "cp"
        self.cp_value = 1*number
        super().__init__(self.cp_value, self.name)


class SP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.name = "Silver piece"
        self.abbreviation = "sp"
        self.cp_value = 10*number
        super().__init__(self.cp_value, self.name)


class EP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.name = "Electrum piece"
        self.abbreviation = "ep"
        self.cp_value = 50*number
        super().__init__(self.cp_value, self.name)


class GP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.name = "Gold piece"
        self.abbreviation = "gp"
        self.cp_value = 100*number
        super().__init__(self.cp_value, self.name)


class PP(Coinage):
    def __init__(self, number: int = 1):
        self.number = number
        self.name = "Platinum piece"
        self.abbreviation = "pp"
        self.cp_value = 1000*number
        super().__init__(self.cp_value, self.name)


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
