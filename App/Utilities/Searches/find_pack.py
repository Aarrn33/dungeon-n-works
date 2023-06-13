import App.items as Items
import App.Utilities.inventory as Inventory


def find_pack(name: str) -> dict[str, tuple[int, Items.Item]]:
    name = name.capitalize()
    # TODO Add other packs (maybe make a db for them)
    if name == "Burglar's pack":
        return Inventory.list2inv([
            ("Backpack", 1),
            ("Bag of Ball Bearings", 1),
            ("String", 1),
            ("Bell", 1),
            ("Candle", 5),
            ("Crowbar", 1),
            ("Hammer", 1),
            ("Pitons", 10),
            ("Hooded Lantern", 1),
            ("Flask of Oil", 2),
            ("Ration", 5),
            ("Tinderbox", 1),
            ("Waterskin", 1),
            ("Hempen Rope", 1),
        ])
    elif name == "Dimplomat's pack":
        return Inventory.list2inv([
            ("Chest", 1),
            ("Case", 2),
            ("Fine Clothes", 1),
            ("Ink Bottle", 1),
            ("Ink Pen", 1),
            ("Lamp", 1),
            ("Flask of Oil", 2),
            ("Paper Sheet", 5),
            ("Vial of Perfume", 1),
            ("Sealing Wax", 1),
            ("Soap", 1),
        ])
    elif name == "Dungeoneer's pack":
        return Inventory.list2inv([
            ("Backpack", 1),
            ("Crowbar", 1),
            ("Hammer", 1),
            ("Piton", 10),
            ("Torch", 10),
            ("Tinderbox", 1),
            ("Ration", 10),
            ("Waterskin", 1),
            ("Hempen Rope", 1),
        ])
    elif name == "Entertainer's pack":
        return Inventory.list2inv([
            ("Backpack", 1),
            ("Bedroll", 1),
            ("Costume", 2),
            ("Candle", 5),
            ("Ration", 5),
            ("Waterskin", 1),
            ("Disguise Kit", 1),
        ])
    elif name == "Explorer's pack":
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
    elif name == "Priest's pack":
        return Inventory.list2inv([
            ("Backpack", 1),
            ("Blanket", 1),
            ("Candle", 10),
            ("Tinderbox", 1),
            ("Alms Box", 1),
            ("Block of Incense", 2),
            ("Censer", 1),
            ("Vestments", 1),
            ("Ration", 2),
            ("Waterskin", 1),
        ])
    elif name == "Scholar's pack":
        return Inventory.list2inv([
            ("Backpack", 1),
            ("Book of Lore", 1),
            ("Ink Bottle", 1),
            ("Ink Pen", 1),
            ("Parchment", 10),
            ("Little bag of Sand", 1),
            ("Small Knife", 1),
        ])
    else:
        return RuntimeError(f"No pack named {name} is yet implemented")
