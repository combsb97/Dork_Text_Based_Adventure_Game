class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy object")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2
        self.roll = None


class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10
        self.roll = None


class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of Bats"
        self.hp = 100
        self.damage = 4
        self.roll = None


class RockMonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15
        self.roll = None
