# https://adventofcode.com/2022/day/8

import numpy as np

data = np.genfromtxt("input.txt", dtype=np.int32, delimiter=1)
m, n = data.shape

# Part 1
p1 = 0
for i, row in enumerate(data):
    for j, element in enumerate(row):
        # Check if edge row.
        if i == 0 or i == m - 1:
            p1 += 1
            continue
        # Check if edge column.
        if j == 0 or j == n - 1:
            p1 += 1
            continue
        # Compare to left, right, up, down.
        if element > max(row[:j]) \
                or element > max(row[j+1:]) \
                or element > max(data[:i, j]) \
                or element > max(data[i+1:, j]):
            p1 += 1

# Part 2
p2 = 0
for i, row in enumerate(data):
    for j, element in enumerate(row):
        # Check if edge row.
        if i == 0 or i == m - 1:
            continue
        # Check if edge column.
        if j == 0 or j == n - 1:
            continue
        # Look left.
        left = 0
        for tree in row[:j][::-1]:
            if tree < element:
                left += 1
            else:
                left += 1
                break
        # Look right.
        right = 0
        for tree in row[j+1:]:
            if tree < element:
                right += 1
            else:
                right += 1
                break
        # Look up.
        up = 0
        for tree in data[:i, j][::-1]:
            if tree < element:
                up += 1
            else:
                up += 1
                break
        # Look down.
        down = 0
        for tree in data[i+1:, j]:
            if tree < element:
                down += 1
            else:
                down += 1
                break
        # Update score.
        scenic_score = left*right*up*down
        p2 = max(p2, scenic_score)

print("Solution Part 1:", p1)
print("Solution Part 2:", p2)
