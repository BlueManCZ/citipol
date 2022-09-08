from .tile import Tile
from .entities.abstract_entity import AbstractEntity
from .types import Coords, Direction, Matrix


class Grid:
    def __init__(self, size_x: int, size_y):
        self._size_x = size_x
        self._size_y = size_y
        self._grid: Matrix = []

        def move_callback(entity, new_coords: Coords):
            # TODO optimalizovat
            coords = self.get_entity_coords(entity)

            if not coords:
                raise Exception("Entity not found in grid.")

            if not self.coords_valid(new_coords):
                raise InvalidCoordsException(
                    "New coordinates are not valid on this grid."
                )

        callbacks: dict = {"move_callback": move_callback}

        for y in range(self._size_y):
            self._grid.append([])
            for x in range(self._size_x):
                self._grid[-1].append(Tile(callbacks=callbacks))

    def coords_valid(self, coords: Coords) -> bool:
        return 0 <= coords.x < self._size_x and 0 <= coords.y < self._size_y

    def get_tile(self, coords: Coords) -> Tile:
        if self.coords_valid(coords):
            return self._grid[coords.y][coords.x]
        else:
            raise InvalidCoordsException("Coordinates are not valid on this grid.")

    def get_entity_coords(self, entity: AbstractEntity) -> Coords | bool:
        for y in range(self._size_y):
            for x in range(self._size_x):
                if self.get_tile(Coords(x, y)).has_entity(entity):
                    return Coords(x, y)
        return False

    def get_matrix(self) -> Matrix:
        return self._grid

    def print(self):
        for y in self.get_matrix():
            print("".join(map(lambda x: str(x), y)))


class InvalidCoordsException(Exception):
    """Raised when working with invalid coordinates"""

    pass
