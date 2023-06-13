from App.items import Item as item


class Inventory():
    def __init__(self, content: dict[str, int] = {}) -> None:
        self.inventory = content
        self.names = list(self.inventory.keys())

    def __iter__(self):
        self.current_key_id = 0
        return self

    def __next__(self):
        if self.current_key_id < len(self.inventory.keys()):
            name = list(self.inventory.keys())[self.current_key_id]
            # Returns (name, quantity)
            current_data = (name, self.inventory[name])
            self.current_key_id += 1
            return current_data
        else:
            raise StopIteration

    def __getitem__(self, key: str) -> int:
        return self.inventory[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.inventory[key] = value

    def __add__(self, other):
        assert isinstance(
            other, Inventory), f"{other} must be a valid inventory"
        new_inventory = Inventory()
        for name, quantity in self:
            new_inventory.inventory[name] = quantity
        for name, quantity in other:
            # If the item is not already present in the current dictionnary
            if name not in self.inventory.keys():
                new_inventory.inventory[name] = quantity
            else:
                new_inventory.inventory[name] = self.inventory[name] + quantity
        return new_inventory

    def __repr__(self) -> str:
        return f"<Inventory: {self.inventory}>"


def list2inv(lis: list[tuple[str, int]]) -> Inventory:
    # Basic check to catch basic mistakes
    assert all((isinstance(tup, tuple) and len(tup) == 2)
               for tup in lis), f"The provided argument {lis} cannot be transformed in to an inventory"
    dict_inv = {}
    for name, quantity in lis:
        dict_inv[name] = quantity
    return Inventory(dict_inv)
