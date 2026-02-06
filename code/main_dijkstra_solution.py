import sys
from robot import Robot
from grid import Grid
from heapq import *

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

q = [robot]
visited = set()
while not robot.at_goal():
    print(robot)
    for d in DIRECTIONS:
        r = robot.copy()
        if r.move(d):
            if r.position not in visited:
                visited.add(r.position)
                heappush(q, r)
    if len(q) == 0: break
    robot = heappop(q)

if robot.at_goal():
    print(f"Goal reached at {robot.position} with cost {robot.cost}.")
else:
    print("Goal not reachable from start.")

