# https://adventofcode.com/2022/day/10

cycle = 0
X = 1  # Register
signal_strengths = []

data = open("input.txt", "r").read().strip().split("\n")

for instruction in data:
    match instruction.split():
        case ["noop"]:
            cycle += 1
            signal_strengths.append(cycle*X)
        case "addx", num:
            cycle += 1
            signal_strengths.append(cycle*X)
            cycle += 1
            signal_strengths.append(cycle*X)
            X += int(num)

# Part 1
p1 = sum(signal_strengths[19::40])


p2 = 0
print("Solution Part 1:", p1)
print("Solution Part 2:", p2)
