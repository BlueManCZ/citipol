"""Module containing types and aliases"""

from dataclasses import dataclass
from enum import Enum, auto
from .event import Event


# noinspection PyArgumentList
class Direction(Enum):
    """Enum for representing direction"""

    RIGHT = auto()
    UP = auto()
    LEFT = auto()
    DOWN = auto()


@dataclass
class Coords:
    """Class for storing coordinates"""

    # pylint: disable=invalid-name
    x: int
    y: int
    # pylint: enable=invalid-name

    def get_next(self, direction: Direction):
        """Get next coordinates in given direction"""
        dic = {
            Direction.RIGHT: lambda: Coords(self.x + 1, self.y),
            Direction.UP: lambda: Coords(self.x, self.y - 1),
            Direction.LEFT: lambda: Coords(self.x - 1, self.y),
            Direction.DOWN: lambda: Coords(self.x, self.y + 1),
        }

        return dic[direction]()
