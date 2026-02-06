import sys
from robot import Robot
from grid import Grid

# -------------------------------
# Load the grid
# -------------------------------
grid_file = "examples/medium.txt"
if len(sys.argv) == 2:
  grid_file = sys.argv[1]
robot = Robot(Grid.from_file(grid_file))

# -------------------------------
# Recursive DFS
# -------------------------------

# Define directions in order: UP, RIGHT, DOWN, LEFT
DIRECTIONS = ["UP", "RIGHT", "DOWN", "LEFT"]

def dfs(robot, visited):
    if robot.position in visited:
        return False # already visited here
    visited.add(robot.position)
    
    if robot.at_goal():
        return True  # goal reached
    
    for d in range(4):
        print(robot)
        if robot.move(DIRECTIONS[d]):
            if dfs(robot, visited):
                return True # goal found in recursion
            robot.move(DIRECTIONS[(d+2)%4])
    return False  # no path found from this branch

if dfs(robot, set()):
    print(f"Goal reached at {robot.position} with cost {robot.cost}.")
else:
    print("Goal not reachable from start.")

