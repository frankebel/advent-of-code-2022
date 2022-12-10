# https://adventofcode.com/2022/day/10

cycle = 0
X = 1  # Register
signal_strengths = []
raster = ''

data = open("input.txt", "r").read().strip().split("\n")

for instruction in data:
    match instruction.split():
        case ["noop"]:
            raster += "#" if abs((cycle % 40)-X) <= 1 else "."
            cycle += 1
            signal_strengths.append(cycle*X)
        case "addx", num:
            # Cycle 1
            raster += "#" if abs((cycle % 40)-X) <= 1 else "."
            cycle += 1
            signal_strengths.append(cycle*X)
            # Cycle 2
            raster += "#" if abs((cycle % 40)-X) <= 1 else "."
            cycle += 1
            signal_strengths.append(cycle*X)
            X += int(num)

# Part 1
p1 = sum(signal_strengths[19::40])
print("Solution Part 1:", p1)

# Part 2
p2 = [raster[i:i+40] for i in range(0, len(raster), 40)]
print("Solution Part 2:", *p2, sep="\n")
