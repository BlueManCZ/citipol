from modules.core.entities.entity_settings import EntitySettings
from .abstract_entity import AbstractEntity


class AbstractUnitEntity(AbstractEntity):
    type = "unit"

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__(settings)
    
    def move_event(self, direction):
        
