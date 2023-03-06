# https://adventofcode.com/2022/day/12

from collections import deque
import copy
import numpy as np
import string


def alpha_to_int(
    grid: np.ndarray, start: tuple, end: tuple, reverse: bool = False
) -> np.ndarray:
    """Create grid with numeric representation."""

    # Map ("S", "E") to ("a", "z")
    temp = copy.deepcopy(grid)
    temp[start] = "a"
    temp[end] = "z"
    # Map ASCII characters to number
    s = string.ascii_lowercase
    s = s[::-1] if reverse else s
    res = [[s.index(element) for element in row] for row in temp]
    res = np.array(res, dtype=np.int32)
    return res


def BFS(grid: np.ndarray, start: tuple, end: int | tuple) -> int:
    """Breadth first_search on grid from start to end."""

    # Deque holds nodes in the form (y, x, steps)
    Q = deque()
    Q.append((*start, 0))
    # Explored holds all explored nodes
    explored = set([start])

    while len(Q) > 0:
        y, x, steps = Q.popleft()

        # Return steps if "end" is visited
        if isinstance(end, tuple):
            if (y, x) == end:
                return steps
        else:
            if grid[y, x] == end:
                return steps

        # Else raise steps by 1
        steps += 1
        # Create list of neighbouring nodes.
        next_node = []
        # Left
        if x > 0:
            if grid[y, x - 1] - grid[y, x] <= 1:
                next_node.append((y, x - 1))
        # Right
        try:
            if grid[y, x + 1] - grid[y, x] <= 1:
                next_node.append((y, x + 1))
        except IndexError:
            pass
        # Up
        if y > 0:
            if grid[y - 1, x] - grid[y, x] <= 1:
                next_node.append((y - 1, x))
        # Down
        try:
            if grid[y + 1, x] - grid[y, x] <= 1:
                next_node.append((y + 1, x))
        except IndexError:
            pass

        # Check if neighbor is already visited and update if not.
        for neighbor in next_node:
            if neighbor not in explored:
                explored.add(neighbor)
                Q.append((*neighbor, steps))

    raise Exception("No path found")


data = [list(row) for row in open("input.txt", "r").read().strip().split("\n")]
data = np.array(data, dtype=np.dtype("U1"))

# Get coordinates for start, end
for i, row in enumerate(data):
    for j, element in enumerate(row):
        match element:
            case "S":
                start = (i, j)
            case "E":
                end = (i, j)
assert start
assert end

# Part 1
grid1 = alpha_to_int(data, start, end)
p1 = BFS(grid1, start, end)
print("Solution Part 1:", p1)

# Part 2
goal = string.ascii_lowercase[::-1].index("a")
grid2 = alpha_to_int(data, start, end, reverse=True)
p2 = BFS(grid2, end, goal)
print("Solution Part 2:", p2)
