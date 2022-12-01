from player import Player
import world
from collections import OrderedDict
import random
import tut
import curses
import time


## This function adds a list of possible actions the player_components can perform on any given tile
def action_adder(action_dic, hotkey, action, name):
    action_dic[hotkey.lower()] = action
    action_dic[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def get_available_actions(room: object, player: object) -> object:
    actions = OrderedDict()
    print("Choose an Action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Inventory")
    if isinstance(room, world.LootTile):
        action_adder(actions, 't', player.add_item, "Take Loot")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
        if player.mana > 0:
            action_adder(actions, 's', player.cast_spell, "Cast Spell")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go North")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go South")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go East")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go West")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")
    if player.mana < 100:
        action_adder(actions, 'm', player.restore_mana, "Restore Mana")

    return actions


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            print()
            action()
        else:
            print("Invalid Action")


def roll_dice():
    roll = random.randint(1, 20)
    return roll


def roll_initiative(room, player):
    player.roll = roll_dice()
    room.roll = roll_dice()
    if player.roll > room.roll:
        print("You act quickly!")
    else:
        print("Enemy strikes!")
        room.modify_player(player)
    return


def battle_loop(room, player):
    roll_initiative(room, player)
    while room.enemy.is_alive() and player.is_alive():
        choose_action(room, player)
        room.modify_player(player)
        if room.enemy.is_alive(): print(room.intro_text())


def play():
    # title screen
    SCREEN = curses.initscr()
    tut.main(SCREEN)

    print("DORK: Escape from Terror Cave")
    world.parse_world_dsl()
    player = Player()
    # main game loop
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        if not isinstance(room, world.EnemyTile):
            room.modify_player(player)

        # if tile is an enemy tile, engage battle loop
        if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
            battle_loop(room, player)

        # if tile has loot
        if isinstance(room, world.LootTile):
            room.print_loot()
            choose_action(room, player)

        # if player is alive and not victorious
        if player.is_alive() and not player.victory:
            choose_action(room, player)

        if not player.is_alive():
            print("Your journey has come to an early end!")

    print("\napplication will close in 5 seconds")
    time.sleep(5)

play()