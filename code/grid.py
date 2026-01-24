from pathlib import Path


class Grid:
    """
    Represents a 2D grid loaded from a text file.

    Coordinates are expressed as (row, col).

    Legend:
        # : wall
        S : start
        G : goal
        digit : free cell
    """

    WALL = "#"
    START = "S"
    GOAL = "G"

    def __init__(self, cells, start, goal):
        self.cells = cells            # cells[row][col]
        self.start = start            # (row, col)
        self.goal = goal              # (row, col)

        self.height = len(cells)
        self.width = len(cells[0]) if cells else 0

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    @classmethod
    def from_file(cls, path):
        """
        Load a grid from a text file.

        :param path: Path to grid file
        :return: Grid instance
        """
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f"Grid file not found: {path}")

        lines = path.read_text().splitlines()
        if not lines:
            raise ValueError("Grid file is empty")

        width = len(lines[0])
        cells = []
        start = None
        goal = None

        for row, line in enumerate(lines):
            if len(line) != width:
                raise ValueError("Grid must be rectangular")

            cell_row = []
            for col, char in enumerate(line):
                if char == cls.START:
                    if start is not None:
                        raise ValueError("Multiple start positions found")
                    start = (row, col)
                    cell_row.append("0")
                elif char == cls.GOAL:
                    if goal is not None:
                        raise ValueError("Multiple goal positions found")
                    goal = (row, col)
                    cell_row.append("0")
                else:
                    cell_row.append(char)

            cells.append(cell_row)

        if start is None:
            raise ValueError("No start position found")

        if goal is None:
            raise ValueError("No goal position found")

        return cls(cells=cells, start=start, goal=goal)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def in_bounds(self, row, col):
        """Return True if (row, col) is inside the grid."""
        return 0 <= row < self.height and 0 <= col < self.width

    def is_wall(self, row, col):
        """Return True if the cell at (row, col) is a wall."""
        if not self.in_bounds(row, col):
            return True
        return self.cells[row][col] == self.WALL

    def is_free(self, row, col):
        """Return True if the cell at (row, col) is free."""
        return self.in_bounds(row, col) and not self.is_wall(row, col)
    
    def cost(self, row, col):
        """Return the cost when entering cell (row, col)."""
        if not self.is_free(row, col):
            raise ValueError(f"Cell ({row}, {col}) is not free.")
        return int(self.cells[row][col])

    # ------------------------------------------------------------------
    # Neighbors
    # ------------------------------------------------------------------

    def neighbors(self, row, col):
        """
        Yield free neighboring cells (4-connectivity).
        """
        for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow, ncol = row + drow, col + dcol
            if self.is_free(nrow, ncol):
                yield nrow, ncol

    # ------------------------------------------------------------------
    # Representation
    # ------------------------------------------------------------------

    def __str__(self):
        grid = [row[:] for row in self.cells]

        sr, sc = self.start
        gr, gc = self.goal

        grid[sr][sc] = self.START
        grid[gr][gc] = self.GOAL

        return "\n".join("".join(row) for row in grid)

