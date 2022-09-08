import pytest

from modules.core.entities import Wall
from modules.core.tile import Tile


@pytest.fixture
def test_tile() -> Tile:
    test_tile = Tile()
    return test_tile


def test_add_entity(test_tile):
    wall_entity = Wall()
    wall_entity_2 = Wall()
    test_tile.add_entity(wall_entity)
    test_tile.add_entity(wall_entity_2)
    assert (
        test_tile._entities[0] == wall_entity
        and test_tile._entities[1] == wall_entity_2
    )


def test_get_entity(test_tile):
    wall_entity = Wall()
    wall_entity_2 = Wall()
    test_tile.add_entity(wall_entity)
    test_tile.add_entity(wall_entity_2)
    assert (
        test_tile.get_entity(0) == wall_entity
        and test_tile.get_entity(1) == wall_entity_2
    )
