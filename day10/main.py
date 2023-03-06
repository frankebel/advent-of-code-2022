# https://adventofcode.com/2022/day/10

import textwrap


def update(cycle, raster, width_CRT, signal_strengths):
    raster += "#" if abs((cycle % width_CRT) - X) <= 1 else "."
    cycle += 1
    signal_strengths.append(cycle * X)
    return cycle, raster


cycle = 0
X = 1  # Register
width_CRT = 40
signal_strengths = []
raster = ""

data = open("input.txt", "r").read().strip().split("\n")

for instruction in data:
    match instruction.split():
        case ["noop"]:
            cycle, raster = update(cycle, raster, width_CRT, signal_strengths)
        case "addx", num:
            # Cycle 1
            cycle, raster = update(cycle, raster, width_CRT, signal_strengths)
            # Cycle 2
            cycle, raster = update(cycle, raster, width_CRT, signal_strengths)
            X += int(num)

# Part 1
p1 = sum(signal_strengths[19::40])
print("Solution Part 1:", p1)

# Part 2
p2 = textwrap.wrap(raster, width_CRT)
print("Solution Part 2:", *p2, sep="\n")
