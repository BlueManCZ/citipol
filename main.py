#!/usr/bin/env python3

from modules.core.grid import Grid
from modules.core.entities.wall import Wall
from modules.core.types.coords import Coords

if __name__ == "__main__":
    grid = Grid(8, 16)
    grid.get_tile(Coords(0, 0)).add_entity(Wall())
    grid.print()

    # wall = Wall()
    # print(wall)