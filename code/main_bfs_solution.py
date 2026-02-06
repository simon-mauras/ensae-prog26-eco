import sys
from robot import Robot
from grid import Grid
from collections import deque

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

q = deque()
visited = set()
while not robot.at_goal():
    print(robot)
    for d in DIRECTIONS:
        r = robot.copy()
        if r.move(d):
            if r.position not in visited:
                visited.add(r.position)
                q.append(r)
    if len(q) == 0: break
    robot = q.popleft()

if robot.at_goal():
    print(f"Goal reached at {robot.position} with cost {robot.cost}.")
else:
    print("Goal not reachable from start.")

