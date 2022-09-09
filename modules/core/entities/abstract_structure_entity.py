from modules.core.entities.entity_settings import EntitySettings
from .abstract_entity import AbstractEntity


class AbstractStructureEntity(AbstractEntity):
    type = "structure"

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__(settings)
