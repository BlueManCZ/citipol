"""
Module for abstract entity class
"""
from modules.core import AbstractObject
# pylint: disable=too-few-public-methods
from modules.core.entities.entity_settings import EntitySettings


class AbstractEntity(AbstractObject):
    """Abstract class for entity definition"""

    type = ""

    def __init__(self, settings: EntitySettings) -> None:
        super().__init__()
        self._char = settings.char
        self._weight = 0

    def __str__(self) -> str:
        return self._char
