import items
import world
import spells


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          items.CrustyBread(),
                          items.ColdMushroomSoup(),
                          items.ManaPotion()]

        self.spellbook = [spells.FireSpell()]

        self.x = 1  # world.start_tile_location[0]
        self.y = 2  # world.start_tile_location[1]
        self.hp = 100
        self.mana = 0
        self.gold = 5
        self.roll = None
        self.victory = False

    def add_item(self):
        room = world.tile_at(self.x, self.y)
        found_items = [item for item in room.loot.loot_table]
        print("Choose an item to loot: ")
        for i, item in enumerate(found_items, 1):
            print("{}. {}".format(i, item.name))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_loot = found_items[int(choice) - 1]
                self.inventory.append(to_loot)
                room.loot.loot_table.remove(to_loot)
                print("You put the {} into your pack.\n".format(to_loot.name))
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")


    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you.")
            return

        else:
            print("Choose an item for healing: ")
            for i, item in enumerate(consumables, 1):
                print("{}. {}".format(i, item.name))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def restore_mana(self):
        consumables = [item for item in self.inventory if isinstance(item, items.ManaConsumable)]
        if not consumables:
            print("You don't have any items to restore your mana.")
            return
        else:
            print("Choose an item to restore mana: ")
            for i, item in enumerate(consumables, 1):
                print("{}. {}".format(i, item.name))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.mana = min(100, self.mana + to_eat.mana_value)
                self.inventory.remove(to_eat)
                print("Current MA: {}".format(self.mana))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def print_inventory(self):
        print("\u001B[4mInventory:\u001B[0m")
        for item in self.inventory:
            print('* ' + str(item))
        print("Gold: {}".format(self.gold))
        # best_weapon = self.most_powerful_weapon()
        # print("Your {} may be your best weapon.".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def cast_spell(self):
        known_spells = [spell for spell in self.spellbook if isinstance(spell, spells.Castable)]
        if not known_spells:
            print("You don't know any spells to cast.")
            return

        elif self.mana == 0:
            print("You do not have enough MANA to cast any spells.")
            return

        else:
            print("Choose a spell to cast: ")
            for i, spell in enumerate(known_spells, 1):
                print("{}. {}".format(i, spell.name))

        valid = False
        while not valid:
            choice = input("")
            try:
                spell_cast = known_spells[int(choice) - 1]
                if self.mana < spell_cast.mana_cost:
                    print("You do not have enough MANA to cast this spell.")
                    return

                else:
                    self.mana = min(50, self.mana - spell_cast.mana_cost)

                room = world.tile_at(self.x, self.y)
                enemy = room.enemy
                print("You use {} against {}!".format(spell_cast.name, enemy.name))
                enemy.hp -= spell_cast.damage
                if not enemy.is_alive():
                    print("You killed {}!".format(enemy.name))
                else:
                    print("{} HP is {}.".format(enemy.name, enemy.hp))

                print("Current MANA: {}".format(self.mana))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def is_alive(self):
        return self.hp > 0
