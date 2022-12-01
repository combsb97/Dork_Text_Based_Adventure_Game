import random
import enemies
import lootTable


## base superclass for constructing different map tiles such as enemy tiles, sleep tiles, building tiles, etc...
## each tile has an x and y coordinate linking it to the game map
## a tile can modify a player_components
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass.")

    def modify_player(self, player):
        pass

    def __str__(self):
        return "Tile"


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        you can make out four paths, each equally dark and foreboding...
        """


class LootTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.loot = lootTable.BarrelLoot()
        self.full_text = """
        You find yourself in a small room...
         ... you notice a barrel with some items inside.
         """
        self.empty_text = """
        You find yourself in a small room...
        ... you remember looting this room.
        """

    def print_loot(self):
        print("{} Loot:".format(self.loot.name))
        for item in self.loot.loot_table:
            print('* ' + str(item))

    def take_loot(self, player, i):
        item = self.loot.loot_table[i]
        player.add_item(item)
        self.loot.loot_table.remove(i)

    def intro_text(self):
        text = self.full_text if self.loot.is_empty() else self.empty_text
        return text


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = """
            A giant spider jumps down from its web in front of you!
            """
            self.dead_text = """
            The corpse of a dead spider rots on the ground.
            """
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = """
            An ogre is blocking your path!
            """
            self.dead_text = """
            A dead ogre reminds you of your triumph.
            """
        elif r < 0.95:
            self.enemy = enemies.BatColony()
            self.alive_text = """
            You hear the incoming screech of angry bats in your direction!
            """
            self.dead_text = """
            Dozens of dead bats litter the ground.
            """
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = """
            You've disturbed a rock monster from its slumber!
            """
            self.dead_text = """
            Defeated, the monster has been reduced to gravel.
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Current HP: {}".format(player.hp))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        
        
        Victory is yours!
        """


world_dsl = """
||VT||
||EN||
|EN|ST|LT|
||EN||
"""

world_map = [
    [None, VictoryTile(1, 0), None],
    [None, EnemyTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), LootTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


tile_type_dict = {"VT": VictoryTile, "EN": EnemyTile, "ST": StartTile, " ": None, "LT": LootTile}


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is Invalid")
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)
