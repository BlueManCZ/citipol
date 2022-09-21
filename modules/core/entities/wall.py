"""Module for Wall entity"""

from . import AbstractStructureEntity, EntitySettings


# pylint: disable=too-few-public-methods
class Wall(AbstractStructureEntity):
    """Entity representing solid wall"""

    def __init__(self) -> None:
        settings = EntitySettings()
        settings.char = "█"
        super().__init__(settings)

        self.set_solid()
