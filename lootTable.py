import items


class LootTable:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy object")

    def __str__(self):
        return self.name

    def remove (self):
        pass


class BarrelLoot(LootTable):
    def __init__(self):
        self.name = "Barrel"
        self.loot_table = [items.RustySword(), items.HealingPotion()]

    def is_empty(self):
        return len(self.loot_table) > 0

