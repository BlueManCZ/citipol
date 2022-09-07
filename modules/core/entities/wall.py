from .abstract_entity import AbstractEntity

class Wall(AbstractEntity):
    def __init__(self):
        super().__init__("█")