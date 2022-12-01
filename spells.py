class Castable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Castable Spell object")

    def __str__(self):
        return self.name


class FireSpell(Castable):
    def __init__(self):
        self.name = "Fire Spell"
        self.mana_cost = 10
        self.damage = 10

