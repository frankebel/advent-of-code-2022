# https://adventofcode.com/2022/day/6

def find_distinct(string, length):
    for i, _ in enumerate(string):
        chars = string[i:i+length]
        if len(set(chars)) == len(chars):
            return i+length


data = open("input.txt", "r").read().strip().split("\n")

p1, p2 = -1, -1  # Fallback
for line in data:
    # Part 1
    p1 = find_distinct(line, 4)
    # Part 2
    p2 = find_distinct(line, 14)

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
