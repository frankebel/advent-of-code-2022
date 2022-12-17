# https://adventofcode.com/2022/day/15

import re

data = [tuple(map(int, re.findall(r"-?\d+", observation)))
        for observation in
        open("input.txt", "r").read().strip().split("\n")]

# Part 1
row = 2_000_000
p1 = set()
beacons = set()
for sx, sy, bx, by in data:
    beacons.add((bx, by))
    d = abs(sx - bx) + abs(sy - by)  # Manhatten distance
    # Check if area overlaps given row.
    if (row_dist := abs(sy - row)) <= d:
        # Add all x coordinates to p1.
        x = set(range(sx-(d-row_dist), sx+(d-row_dist)+1))
        p1 = p1.union(x)

# Remove beacons in row.
for bx, by in beacons:
    if by == row:
        p1.remove(bx)

print("Solution Part 1:", len(p1))


# Part 2
p2 = 0
print("Solution Part 2:", p2)
