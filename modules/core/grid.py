"""Module for the Grid package"""

from modules.core.tile import Tile
from modules.core.entities.abstract_entity import AbstractEntity
from modules.core.types import Coords, Matrix


class Grid:
    """Class representing a 2D grid of Tiles"""

    def __init__(self, size_x: int, size_y: int) -> None:
        self._size_x = size_x
        self._size_y = size_y
        self._grid: Matrix = []

        def move_callback(entity: AbstractEntity, new_coords: Coords) -> None:
            # TODO optimalizovat
            coords = self.get_entity_coords(entity)

            if not coords:
                raise Exception("Entity not found in grid.")

            if not self.coords_valid(new_coords):
                raise InvalidCoordsException(
                    "New coordinates are not valid on this grid."
                )

        callbacks: dict = {"move_callback": move_callback}

        for _ in range(self._size_y):
            self._grid.append([])
            for _ in range(self._size_x):
                self._grid[-1].append(Tile(callbacks=callbacks))

    def coords_valid(self, coords: Coords) -> bool:
        """Check validness of Grid coordinates"""
        return 0 <= coords.x < self._size_x and 0 <= coords.y < self._size_y

    def get_tile(self, coords: Coords) -> Tile:
        """Get Tile from Grid coordinates"""
        if self.coords_valid(coords):
            return self._grid[coords.y][coords.x]
        raise InvalidCoordsException("Coordinates are not valid on this grid.")

    def get_entity_coords(self, entity: AbstractEntity) -> Coords | bool:
        """Find Entity coordinates"""
        for y_coord in range(self._size_y):
            for x_coord in range(self._size_x):
                if self.get_tile(Coords(x_coord, y_coord)).has_entity(entity):
                    return Coords(x_coord, y_coord)
        return False

    def get_matrix(self) -> Matrix:
        """Return raw matrix (list of lists) of Tiles"""
        return self._grid

    def print(self) -> None:
        """Print text representation of Grid"""
        for y_coord in self.get_matrix():
            print("".join(map(str, y_coord)))


class InvalidCoordsException(Exception):
    """Raised when working with invalid coordinates"""
