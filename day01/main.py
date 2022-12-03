# https://adventofcode.com/2022/day/1
with open("day01/input.txt", "r") as f:
    calories = [sum([int(food) for food in elf.split("\n")])
                for elf in f.read().strip().split("\n\n")]
print(f"Solution Part 1: {max(calories)}")
print(f"Solution Part 2: {sum(sorted(calories, reverse=True)[:3])}")
