from grid import Grid

class Robot:
    """
    A robot that moves on a Grid.

    Position is stored as (row, col).
    Movement is 4-connected.
    """

    _MOVES = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1),
    }

    def __init__(self, grid: Grid):
        self.grid = grid
        self.position = grid.start
        self.cost = 0
    
    # ------------------------------------------------------------------
    # Movement
    # ------------------------------------------------------------------

    def move(self, direction):
        """
        Move the robot in the given direction.

        :param direction: One of 'UP', 'DOWN', 'LEFT', 'RIGHT'
        :return: True if the move succeeded, False otherwise
        """
        if direction not in self._MOVES:
            raise ValueError(f"Invalid direction: {direction}")

        drow, dcol = self._MOVES[direction]
        row, col = self.position
        new_row, new_col = row + drow, col + dcol

        if self.grid.is_free(new_row, new_col):
            self.position = (new_row, new_col)
            self.cost += self.grid.cost(new_row, new_col)
            return True

        return False

    # ------------------------------------------------------------------
    # State queries
    # ------------------------------------------------------------------

    def at_goal(self):
        """Return True if the robot has reached the goal."""
        return self.position == self.grid.goal

    def reset(self):
        """Reset the robot to the start position."""
        self.position = self.grid.start
        self.cost = 0

    # ------------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------------

    def __str__(self):
        row, col = self.position
        return f"Robot at ({row}, {col}) with cost {self.cost}."

