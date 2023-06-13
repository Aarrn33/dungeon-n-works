import App.items as Items
import App.Utilities.inventory as Inventory


def find_pack(name: str) -> dict[str, tuple[int, Items.Item]]:
    name = name.capitalize()
    # TODO Add other packs (maybe make a db for them)
    if name == "Explorer's pack":
        return Inventory.list2inv([
            ("Backpack", 1),
            ("Bedroll", 1),
            ("Mess Kit", 1),
            ("Tinderbox", 1),
            ("Torch", 1),
            ("Ration", 1),
            ("Waterskin", 1),
            ("Hempen Rope", 1),
        ])
    else:
        return RuntimeError(f"No pack named {name} is yet implemented")
