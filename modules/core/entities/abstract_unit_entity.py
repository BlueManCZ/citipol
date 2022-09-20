from modules.core.entities.entity_settings import EntitySettings
from .abstract_entity import AbstractEntity
from ..types import Event, Direction


class AbstractUnitEntity(AbstractEntity):
    type = "unit"

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__(settings)
        self._health = 100

    def get_health(self) -> int:
        return self._health

    def set_health(self, health) -> None:
        self._health = health

    def move_event(self, direction: Direction) -> None:
        def moving_callback():
            # Pro renderování
            print("MOVING MOVING")

        event = Event("move", {"direction": direction}, moving_callback)

        self.emit(event)
