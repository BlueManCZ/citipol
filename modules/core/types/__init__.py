"""Module containing types and aliases"""

from dataclasses import dataclass
from enum import Enum, auto


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


class Event:
    def __init__(self, name, data=None, callback=None):
        self._name = name
        self._data = data if data else {}
        self._callback = callback
        self._stop_propagation = False
        self._object_path = []

    def stop_propagation(self):
        self._stop_propagation = True

    def get_origin(self):
        return self.get_object_path()[0]

    def get_previous_object(self):
        return self.get_object_path()[-1]

    def get_name(self):
        return self._name

    def get_all_data(self):
        return self._data

    def get_data(self, key):
        if key in self._data:
            return self._data[key]
        return None

    def get_callback(self):
        return self._callback

    def get_object_path(self):
        return self._object_path

    def register_object_to_path(self, obj):
        self._object_path.append(obj)

    def should_propagate(self):
        return not self._stop_propagation
