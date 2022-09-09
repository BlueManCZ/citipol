"""
Module for abstract entity class
"""


# pylint: disable=too-few-public-methods
class AbstractEntity:
    """Abstract class for entity definition"""

    def __init__(self, char: str = ".") -> None:
        self._char = char

    def __str__(self) -> str:
        return self._char
