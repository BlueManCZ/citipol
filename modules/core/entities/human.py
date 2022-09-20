"""Module for Human entity"""

from modules.core.entities import AbstractUnitEntity
from modules.core.entities.entity_settings import EntitySettings


# pylint: disable=too-few-public-methods
class Human(AbstractUnitEntity):
    """Entity representing human"""

    def __init__(self) -> None:
        settings = EntitySettings()
        settings.char = "☺"
        super().__init__(settings)
