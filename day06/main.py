# https://adventofcode.com/2022/day/6

import more_itertools


def find_distinct(string, length):
    for i, window in enumerate(more_itertools.sliding_window(string, length)):
        if len(set(window)) == length:
            return i + length


data = open("input.txt", "r").readline().strip()
p1 = find_distinct(data, 4)
p2 = find_distinct(data, 14)

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
