from modules.core.entities.entity_settings import EntitySettings
from .abstract_entity import AbstractEntity


class AbstractTerrainEntity(AbstractEntity):
    type = "terrain"

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__(settings)
