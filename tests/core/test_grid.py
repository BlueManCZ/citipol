"""
Unit tests for Grid class
"""

import pytest

from modules.core.entities import Wall
from modules.core.grid import Grid, InvalidCoordsException
from modules.core.types import Coords

SIZE_X = 15
SIZE_Y = 10


@pytest.fixture(name="test_grid")
def fixture_test_grid() -> Grid:
    """Create an empty grid for testing purposes"""
    test_grid = Grid(SIZE_X, SIZE_Y)
    return test_grid


def test_real_size(test_grid: Grid) -> None:
    """Test if the Grid contains correct number of items"""
    count = 0
    for line in test_grid.get_matrix():
        count += len(line)

    assert count == SIZE_X * SIZE_Y


def test_real_size_y(test_grid: Grid) -> None:
    """Test if the Grid contains correct number of lines"""
    size_y = len(test_grid.get_matrix())
    assert size_y == SIZE_Y


@pytest.mark.parametrize(
    "coords, valid",
    [
        (Coords(0, 0), True),
        (Coords(SIZE_X - 1, SIZE_Y - 1), True),
        (Coords(0, SIZE_Y - 1), True),
        (Coords(SIZE_X - 1, 0), True),
        (Coords(SIZE_X, SIZE_Y), False),
        (Coords(-5, -5), False),
        (Coords(-5, 0), False),
        (Coords(0, -5), False),
        (Coords(SIZE_X, -5), False),
        (Coords(-5, SIZE_Y), False),
    ],
)
def test_coords_valid(test_grid: Grid, coords: Coords, valid: bool) -> None:
    """Test coords_valid method"""
    status = test_grid.coords_valid(coords)
    assert status == valid


@pytest.mark.parametrize(
    "coords",
    [
        (Coords(0, 0)),
        (Coords(SIZE_X, SIZE_X)),
    ],
)
def test_get_tile(test_grid: Grid, coords: Coords) -> None:
    """Test get_tile method"""

    def testcase() -> None:
        tile = test_grid.get_tile(coords)
        assert tile == test_grid.get_matrix()[coords.y][coords.x]

    if test_grid.coords_valid(coords):
        testcase()
    else:
        with pytest.raises(InvalidCoordsException):
            testcase()


@pytest.mark.parametrize(
    "coords",
    [
        (Coords(0, 0)),
        (Coords(SIZE_X, SIZE_X)),
    ],
)
def test_get_entity_coords(test_grid: Grid, coords: Coords) -> None:
    """Test get_entity_coords method"""
    wall_entity = Wall()

    def testcase() -> None:
        test_grid.get_tile(coords).add_entity(wall_entity)
        entity_coords = test_grid.get_entity_coords(wall_entity)
        assert entity_coords == coords

    if test_grid.coords_valid(coords):
        testcase()
    else:
        with pytest.raises(InvalidCoordsException):
            testcase()
