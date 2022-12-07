# https://adventofcode.com/2022/day/7
# Online solution

from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)

curr = [""]
for line in open("input.txt"):
    match line.split():
        case "$", "cd", "/":
            curr = [""]
        case "$", "cd", "..":
            curr.pop()
        case "$", "cd", dir:
            curr.append(dir+"/")
        case "$", "ls":
            pass
        case "dir", _:
            pass
        case size, _:
            for p in accumulate(curr):
                dirs[p] += int(size)

# Parameters
threshold = 100_000
total = 70_000_000
needed = 30_000_000

print(f"Solution Part 1: {sum(s for s in dirs.values() if s <= threshold)}")
print("Solution Part 2:",
      min(s for s in dirs.values() if s >= (dirs[""] + needed - total)))
