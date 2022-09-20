from modules.core.entities.entity_settings import EntitySettings
from .abstract_entity import AbstractEntity


class AbstractStructureEntity(AbstractEntity):
    type = "structure"

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__(settings)
        self._solid = False

    def is_solid(self):
        return self._solid

    def set_solid(self, state=True):
        self._solid = state
