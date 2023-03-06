# https://adventofcode.com/2022/day/4

with open("input.txt", "r") as f:
    data = [
        [int(element) for element in row.strip().replace("-", ",").split(",")]
        for row in f.readlines()
    ]

p1, p2 = 0, 0
for row in data:
    s1, s2 = set(range(row[0], row[1] + 1)), set(range(row[2], row[3] + 1))
    if s1.issubset(s2) or s2.issubset(s1):
        p1 += 1
    if not s1.isdisjoint(s2):
        p2 += 1

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
