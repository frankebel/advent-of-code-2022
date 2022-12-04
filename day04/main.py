# https://adventofcode.com/2022/day/4
import numpy as np

with open("input.txt", "r") as f:
    data = [[int(element) for element in
             row.strip().replace("-", ",").split(",")]
            for row in f.readlines()]

# Part 1
p1 = 0
for row in data:
    d1, d2 = row[2] - row[0], row[3] - row[1]
    if np.sign(d1) != np.sign(d2):
        p1 += 1
    if d1 == d2 == 0:
        p1 += 1

# Part 2
p2 = 0
for row in data:
    s1, s2 = set(range(row[0], row[1]+1)), set(range(row[2], row[3]+1))
    if len(set(s1) & set(s2)) != 0:
        p2 += 1

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
