"""Module for the Grid package"""
from modules.core import AbstractObject
from modules.core.tile import Tile
from modules.core.types import Coords, Event

Matrix = list[list[Tile]]


class Grid(AbstractObject):
    """Class representing a 2D grid of Tiles"""

    def __init__(self, size_x: int, size_y: int) -> None:
        super().__init__()

        self._size_x = size_x
        self._size_y = size_y
        self._grid: Matrix = []

        def move_handler(event: Event) -> None:
            direction = event.get_data("direction")
            old_tile = event.get_object_path()[-2]

            old_coords = self.get_coords_by_tile(old_tile)

            new_coords = old_coords.get_next(direction)

            if not self.coords_valid(new_coords):
                raise InvalidCoordsException(
                    "New coordinates are not valid on this grid."
                )

            new_tile = self.get_tile(new_coords)

            new_tile.add_entity(event.get_origin())
            old_tile.remove_entity(event.get_origin())

        self.add_event_listener("move", move_handler)

        for _ in range(self._size_y):
            self._grid.append([])
            for _ in range(self._size_x):
                tile = Tile()
                tile.set_event_parent(self)
                self._grid[-1].append(tile)

    def coords_valid(self, coords: Coords) -> bool:
        """Check validness of Grid coordinates"""
        return 0 <= coords.x < self._size_x and 0 <= coords.y < self._size_y

    def get_tile(self, coords: Coords) -> Tile:
        """Get Tile from Grid coordinates"""
        if self.coords_valid(coords):
            return self._grid[coords.y][coords.x]
        raise InvalidCoordsException("Coordinates are not valid on this grid.")

    def get_coords_by_tile(self, tile: Tile) -> Coords | None:
        """Get coordinates of Tile"""
        # TODO optimalizovat
        for y_coord in range(self._size_y):
            for x_coord in range(self._size_x):
                current_tile = self.get_tile(Coords(x_coord, y_coord))
                if tile == current_tile:
                    return Coords(x_coord, y_coord)
        return None

    def get_matrix(self) -> Matrix:
        """Return raw matrix (list of lists) of Tiles"""
        return self._grid

    def print(self) -> None:
        """Print text representation of Grid"""
        for y_coord in self.get_matrix():
            print("".join(map(str, y_coord)))


class InvalidCoordsException(Exception):
    """Raised when working with invalid coordinates"""
