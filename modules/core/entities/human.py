"""Module for Human entity"""

from . import AbstractUnitEntity, EntitySettings


# pylint: disable=too-few-public-methods
class Human(AbstractUnitEntity):
    """Entity representing human"""

    def __init__(self) -> None:
        settings = EntitySettings()
        settings.char = "☺"
        super().__init__(settings)
