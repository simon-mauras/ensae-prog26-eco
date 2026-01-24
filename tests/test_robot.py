import sys
from pathlib import Path
ROOT = Path(__file__).parent.parent
sys.path.append(str(ROOT / "code"))

import pytest
from grid import Grid
from robot import Robot

# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------

GRID_DIR = ROOT / "examples"


@pytest.fixture
def simple_grid():
    return Grid.from_file(GRID_DIR / "small.txt")


@pytest.fixture
def robot(simple_grid):
    return Robot(simple_grid)


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------

def test_robot_starts_at_start(robot):
    assert robot.position == robot.grid.start


def test_robot_valid_move(robot):
    row, col = robot.position
    moved = robot.move("RIGHT")
    # If RIGHT is free, position changes
    if robot.grid.is_free(row, col + 1):
        assert moved
        assert robot.position != (row, col)
    else:
        assert not moved
        assert robot.position == (row, col)


def test_robot_invalid_move(robot):
    row, col = robot.position
    # Try moving into a wall
    moved = robot.move("UP")
    assert not moved
    assert robot.position == (row, col)


def test_robot_at_goal(robot, simple_grid):
    robot.position = simple_grid.goal
    assert robot.at_goal()


def test_robot_reset(robot):
    robot.move("RIGHT")
    assert robot.position != robot.grid.start
    robot.reset()
    assert robot.position == robot.grid.start


def test_robot_invalid_direction(robot):
    with pytest.raises(ValueError):
        robot.move("DIAGONAL")


@pytest.mark.parametrize("direction", ["UP", "DOWN", "LEFT", "RIGHT"])
def test_robot_param_moves(robot, direction):
    # Move in each direction if possible
    row, col = robot.position
    new_row, new_col = row + Robot._MOVES[direction][0], col + Robot._MOVES[direction][1]
    moved = robot.move(direction)
    if robot.grid.is_free(new_row, new_col):
        assert moved
        assert robot.position == (new_row, new_col)
    else:
        assert not moved
        assert robot.position == (row, col)

