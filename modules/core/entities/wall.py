"""Module for Wall entity"""

from modules.core.entities.entity_settings import EntitySettings
from .abstract_structure_entity import AbstractStructureEntity


# pylint: disable=too-few-public-methods
class Wall(AbstractStructureEntity):
    """Entity representing solid wall"""

    def __init__(self) -> None:
        settings = EntitySettings()
        settings.char = "█"

        super().__init__(settings)
