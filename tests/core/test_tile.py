"""
Unit tests for Tile class
"""

import pytest

from modules.core.entities import Wall
from modules.core.tile import Tile


@pytest.fixture(name="test_tile")
def fixture_test_tile() -> Tile:
    """Create a Tile for testing purposes"""
    test_tile = Tile()
    return test_tile


def test_add_entity(test_tile: Tile) -> None:
    """Test add_entity method"""
    wall_entity = Wall()
    wall_entity_2 = Wall()
    test_tile.add_entity(wall_entity)
    test_tile.add_entity(wall_entity_2)
    assert (
        # pylint: disable=protected-access
        test_tile._entities[0] == wall_entity
        and test_tile._entities[1] == wall_entity_2
        # pylint: enable=protected-access
    )


def test_get_entity(test_tile: Tile) -> None:
    """Test get_entity method"""
    wall_entity = Wall()
    wall_entity_2 = Wall()
    test_tile.add_entity(wall_entity)
    test_tile.add_entity(wall_entity_2)
    assert (
        test_tile.get_entity(0) == wall_entity
        and test_tile.get_entity(1) == wall_entity_2
    )
