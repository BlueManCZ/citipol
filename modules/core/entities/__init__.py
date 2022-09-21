"""Module containing all entities"""

from typing import Type

from .entity_settings import EntitySettings

from .abstract_entity import AbstractEntity
from .abstract_terrain_entity import AbstractTerrainEntity
from .abstract_structure_entity import AbstractStructureEntity
from .abstract_unit_entity import AbstractUnitEntity

from .wall import Wall

entity_class_order: list[Type[AbstractEntity]] = [
    AbstractTerrainEntity,
    AbstractStructureEntity,
    AbstractUnitEntity,
]


def get_entity_class(entity_type: str) -> Type[AbstractEntity] | None:
    """Return entity class by type"""
    for entity in entity_class_order:
        if entity.type == entity_type:
            return entity
    return None
