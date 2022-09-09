"""Module for Wall entity"""

from .abstract_entity import AbstractEntity


# pylint: disable=too-few-public-methods
class Wall(AbstractEntity):
    """Entity representing solid wall"""

    def __init__(self) -> None:
        super().__init__("█")
