"""Module containing types and aliases"""

from dataclasses import dataclass
from enum import Enum, auto

from modules.core.tile import Tile


@dataclass
class Coords:
    """Class for storing coordinates"""

    # pylint: disable=invalid-name
    x: int
    y: int
    # pylint: enable=invalid-name


# noinspection PyArgumentList
class Direction(Enum):
    """Enum for representing direction"""

    RIGHT = auto()
    UP = auto()
    LEFT = auto()
    DOWN = auto()


Matrix = list[list[Tile]]
