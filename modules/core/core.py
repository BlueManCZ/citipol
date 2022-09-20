from modules.core.entities.human import Human
from modules.core.event_manager import EventManager
from modules.core.grid import Grid
from modules.core.types import Coords, Direction


class Core:
    def __init__(self):
        self._event_manager = EventManager()
        self._grid = Grid(16, 4)
        self._grid.set_event_parent(self._event_manager)

        human = Human()
        self._grid.get_tile(Coords(5, 2)).add_entity(human)

        self._grid.print()

        human.move_event(Direction.RIGHT)
        human.move_event(Direction.UP)
        human.move_event(Direction.UP)

        self._grid.print()
