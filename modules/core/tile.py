"""Module for the Tile class"""

from modules.core.entities.abstract_entity import AbstractEntity


class Tile:
    """Class representing a map tile"""

    def __init__(self, callbacks: dict | bool = False) -> None:
        self._entities: list[AbstractEntity] = []
        self._callbacks = callbacks if callbacks else {}

    def add_entity(self, entity: AbstractEntity) -> None:
        """Add entity to the Tile"""
        self._entities.append(entity)

    def get_entity(self, i: int = 0) -> AbstractEntity:
        """Get entity from the Tile based on the index"""
        return self._entities[i]

    def has_entity(self, entity: AbstractEntity) -> bool:
        """Check if entity is present in the Tile"""
        return entity in self._entities

    def __str__(self) -> str:
        return str(self._entities[0]) if self._entities else "_"
