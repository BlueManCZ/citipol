"""Module for AbstractStructureEntity"""

from modules.core.entities.entity_settings import EntitySettings
from modules.core.entities.abstract_entity import AbstractEntity


class AbstractStructureEntity(AbstractEntity):
    """Abstraction for entities representing structure"""

    type = "structure"

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__(settings)
        self._solid = False

    def is_solid(self):
        """Return if structure is solid e.g. unit can or can't move there"""
        return self._solid

    def set_solid(self, state=True):
        """Set solidness of the """
        self._solid = state
