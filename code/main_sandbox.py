from grid import Grid
from robot import Robot

# -------------------------------
# Load the grid
# -------------------------------
grid_file = "examples/small.txt"
robot = Robot(Grid.from_file(grid_file))

# -------------------------------
# Follow a list of instructions
# -------------------------------
DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]
instructions = [1,2,3,0,1,1]

for i in instructions:
    print(robot, end=" ")
    if robot.move(DIRECTIONS[i]):
        print(f"Moving {DIRECTIONS[i]} successful.")
    else:
        print(f"Moving {DIRECTIONS[i]} impossible")

print(robot, end=" ")
if robot.at_goal():
    print("Goal reached!")
else:
    print("Goal not reached...")
