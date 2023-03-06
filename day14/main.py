# https://adventofcode.com/2022/day/14

from collections import defaultdict
from copy import deepcopy


def grid_edges(grid):
    # Get min, max of x, y coordinates.
    x = [a[0] for a in grid.keys()]
    y = [a[1] for a in grid.keys()]
    return min(x), max(x), min(y), max(y)


def print_grid(grid):
    x_min, x_max, _, y_max = grid_edges(grid)
    for y in range(0, y_max + 1):
        print(f"{y:3}", end="")
        for x in range(x_min, x_max + 1):
            print(grid[(x, y)], end="")
        print()


def fill_sand(grid):
    x_min, x_max, _, _ = grid_edges(grid)

    units = 0  # Number of sand units.
    while True:
        # Create sand particle.
        s = source
        while True:
            # Calculate possible locations.
            below = s[1] + 1
            left = s[0] - 1
            right = s[0] + 1
            sb = (s[0], below)  # Below
            sbl = (left, below)  # Bottom left
            sbr = (right, below)  # Bottom right
            # Return sand units if outside of grid.
            if left < x_min:
                return units
            if left > x_max:
                return units
            # Check if possible locations are empty.
            if grid[sb] == ".":
                s = sb
            elif grid[sbl] == ".":
                s = sbl
            elif grid[sbr] == ".":
                s = sbr
            else:
                break
        # Fill location with sand particle.
        grid[s] = "o"
        units += 1
        # Return if source is blocked.
        if s == source:
            return units


source = (500, 0)
data = [
    [tuple(map(int, coordinate.split(","))) for coordinate in wall.split(" -> ")]
    for wall in open("input.txt", "r").readlines()
]


# Create grid.
grid = defaultdict(lambda: ".")
grid[source] = "+"
# Fill grid with walls.
for wall in data:
    for (ax, ay), (bx, by) in zip(wall, wall[1:]):
        if ax == bx:
            if by > ay:
                for y in range(ay, by + 1):
                    grid[(ax, y)] = "#"
            else:
                for y in range(ay, by - 1, -1):
                    grid[(ax, y)] = "#"
        elif ay == by:
            if bx > ax:
                for x in range(ax, bx + 1):
                    grid[(x, ay)] = "#"
            else:
                for x in range(ax, bx - 1, -1):
                    grid[(x, ay)] = "#"
        else:
            Exception("Wall not grid alined")


# Part 1
grid1 = deepcopy(grid)
p1 = fill_sand(grid1)
print("Solution Part 1:", p1)


# Part 2
grid2 = deepcopy(grid)
# Create "inifinite" floor two levels below.
_, _, _, y_max = grid_edges(grid2)
for x in range(500 - y_max - 10, 500 + y_max + 10):  # Margin of 10 units.
    grid2[(x, y_max + 2)] = "#"
p2 = fill_sand(grid2)
print("Solution Part 2:", p2)
