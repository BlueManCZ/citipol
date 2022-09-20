"""Module for the Tile class"""

from modules.core.entities import AbstractEntity
from modules.core import AbstractObject
from .entities import entity_class_order


class Tile(AbstractObject):
    """Class representing a map tile"""

    def __init__(self, callbacks: dict | bool = False) -> None:
        super().__init__()

        self._entities: set[AbstractEntity] = set()
        self._callbacks = callbacks if callbacks else {}

    def add_entity(self, entity: AbstractEntity) -> None:
        """Add entity to the Tile"""
        entity.set_event_parent(self)
        self.get_entities().add(entity)

    def remove_entity(self, entity: AbstractEntity) -> None:
        self.get_entities().remove(entity)

    def get_entities(self) -> set[AbstractEntity]:
        return self._entities

    def get_entities_by_type(self, entity_type: str) -> set[AbstractEntity]:
        """Get entity from the Tile based on the index"""
        # TODO: Lazy?
        return set(filter(lambda e: e.type == entity_type, self.get_entities()))

    def get_entities_sorted(self):
        def sort_func(entity: AbstractEntity):
            for i, entity_class in enumerate(entity_class_order):
                if issubclass(type(entity), entity_class):
                    return i

            return len(entity_class_order)

        return sorted(self.get_entities(), key=sort_func, reverse=True)

    def has_entity(self, entity: AbstractEntity) -> bool:
        """Check if entity is present in the Tile"""
        return entity in self.get_entities()

    def __str__(self) -> str:
        result = self.get_entities_sorted()

        return str(result[0]) if result else "."
