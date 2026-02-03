import sys
import random
from grid import Grid
from robot import Robot

# -------------------------------
# Load the grid
# -------------------------------
grid_file = "examples/medium.txt"
if len(sys.argv) == 2:
  grid_file = sys.argv[1]
robot = Robot(Grid.from_file(grid_file))

# -------------------------------
# Random walk
# -------------------------------

# Define directions in order: UP, RIGHT, DOWN, LEFT
DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

step = 0
while not robot.at_goal() and step <= 10**5:
    step += 1
    print(robot, end="")
    i = random.randrange(4)
    if robot.move(DIRECTIONS[i]):
        print(f"Moving {DIRECTIONS[i]} successful.")
    else:
        print(f"Moving {DIRECTIONS[i]} impossible")

if robot.at_goal():
    print(f"Goal reached at {robot.position} with cost {robot.cost}.")
else:
    print("Goal not reached.")
