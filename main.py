#!/usr/bin/env python3

"""
Main script for starting the application
"""

from modules.core.grid import Grid
from modules.core.entities.wall import Wall
from modules.core.types import Coords

if __name__ == "__main__":
    # grid = Grid(8, 4)
    # grid.get_tile(Coords(0, 0)).add_entity(Wall())
    # running = True
    # while running:
    #     grid.print()
    #     command = input("> ")

    #     match command.split():
    #         case ["exit"]:
    #             running = False
    #         case ["move"]:
    #             pass

    world_file = get_world_file(argv)

    if world_file:
        world = World.from_file(world_file)
    else:
        world = World()

    GUI(world)
