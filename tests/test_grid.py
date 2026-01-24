import sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
sys.path.append(str(ROOT / "code"))

import pytest
from grid import Grid

# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

GRID_DIR = ROOT / "examples"


@pytest.fixture
def simple_grid():
    return Grid.from_file(GRID_DIR / "small.txt")


@pytest.fixture
def medium_grid():
    return Grid.from_file(GRID_DIR / "medium.txt")


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------

def test_simple_grid_dimensions(simple_grid):
    assert simple_grid.width > 0
    assert simple_grid.height > 0


def test_simple_grid_start_and_goal(simple_grid):
    sr, sc = simple_grid.start
    gr, gc = simple_grid.goal

    assert simple_grid.is_free(sr, sc)
    assert simple_grid.is_free(gr, gc)


def test_simple_grid_walls(simple_grid):
    # All border cells should be walls
    for col in range(simple_grid.width):
        assert simple_grid.is_wall(0, col)
        assert simple_grid.is_wall(simple_grid.height - 1, col)
    for row in range(simple_grid.height):
        assert simple_grid.is_wall(row, 0)
        assert simple_grid.is_wall(row, simple_grid.width - 1)


def test_neighbors(medium_grid):
    # Pick a free cell and check neighbors
    for row in range(medium_grid.height):
        for col in range(medium_grid.width):
            if medium_grid.is_free(row, col):
                nbs = list(medium_grid.neighbors(row, col))
                # All neighbors must be free
                assert all(medium_grid.is_free(r, c) for r, c in nbs)
                break  # test one free cell


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        Grid.from_file("does_not_exist.txt")


def test_empty_file(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")
    with pytest.raises(ValueError):
        Grid.from_file(file)


def test_multiple_starts(tmp_path):
    file = tmp_path / "multi_start.txt"
    file.write_text(
        "S S\n"
        "   \n"
        "G  "
    )
    with pytest.raises(ValueError):
        Grid.from_file(file)


def test_multiple_goals(tmp_path):
    file = tmp_path / "multi_goal.txt"
    file.write_text(
        "S  \n"
        "G G\n"
        "   "
    )
    with pytest.raises(ValueError):
        Grid.from_file(file)

