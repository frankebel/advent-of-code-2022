# https://adventofcode.com/2022/day/15

import re
import z3

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
        p1 |= x

# Remove beacons in row.
for bx, by in beacons:
    if by == row:
        p1.discard(bx)

print("Solution Part 1:", len(p1))


# Part 2
p2_constant = 4_000_000

s = z3.Solver()
x, y = z3.Ints("x y")
s.add(x >= 0, x <= 4_000_000)
s.add(y >= 0, y <= 4_000_000)


def z3_abs(x):
    return z3.If(x >= 0, x, -x)


for sx, sy, bx, by in data:
    d = abs(sx - bx) + abs(sy - by)  # Manhatten distance
    # Add constraint that point (x, y) must have bigger distance.
    s.add(z3_abs(x - sx) + z3_abs(y - sy) > d)

assert s.check() == z3.sat
model = s.model()
p2 = model[x].as_long()*p2_constant + model[y].as_long()
print("Solution Part 2:", p2)
