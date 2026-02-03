import sys
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
# Right-hand wall follow strategy
# -------------------------------

# Define directions in order: UP, RIGHT, DOWN, LEFT
DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

# Robot initially faces "UP"
last_move = 0  # index in DIRECTIONS

step = 0
while not robot.at_goal() and step <= 10**5:
    step += 1
    print(robot)
    for i in [1, 0, 3, 2]:
        if robot.move(DIRECTIONS[(last_move+i)%4]):
            last_move = (last_move+i)%4
            break

if robot.at_goal():
    print(f"Goal reached at {robot.position} with cost {robot.cost}.")
else:
    print("Goal not reached.")

