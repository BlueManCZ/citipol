"""
Module for abstract entity class
"""


# pylint: disable=too-few-public-methods
from modules.core.entities.entity_settings import EntitySettings


class AbstractEntity:
    """Abstract class for entity definition"""

    type = ""

    def __init__(self, settings: EntitySettings) -> None:
        self._char = settings.char
        self._weight = 0

    def __str__(self) -> str:
        return self._char
