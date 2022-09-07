from .entities.abstract_entity import AbstractEntity

class Tile:
    def __init__(self, callbacks):
        self._entities = []

    def add_entity(self, entity: AbstractEntity):
        self._entities.append(entity)

    def get_entity(self, i: int = 0):
        return self._entities[i]
    
    def has_entity(self, entity: AbstractEntity):
        return entity in self._entities

    def __str__(self):
        return str(self._entities[0]) if self._entities else "_"