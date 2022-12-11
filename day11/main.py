# https://adventofcode.com/2022/day/10

import copy
import math
import re

rounds1 = 20
rounds2 = 10_000
monkeys = dict()

data = open("input.txt", "r").read().strip().split("\n\n")

for monkey in data:
    m = dict()  # Store data for each monkey in dictionary.
    lines = monkey.split("\n")

    # Monkey number
    num = re.search(r"\d+", lines[0])
    if num:
        num = int(num[0])
    # Starting items
    starting_items = re.findall(r"\d+", lines[1])
    starting_items = [int(item) for item in starting_items]
    m["items1"] = copy.deepcopy(starting_items)
    m["items2"] = copy.deepcopy(starting_items)
    # Operation
    operation = lines[2].split("= ")[-1]
    # m["operation"] = lambda x: eval(operation.replace("old", str(x)))
    m["operation"] = operation
    # Divisibility test
    divisibility = re.search(r"\d+", lines[3])
    if divisibility:
        m["divisibility"] = int(divisibility[0])
    # Divisibility True
    monkey_true = re.search(r"\d+", lines[4])
    if monkey_true:
        m["monkey_true"] = int(monkey_true[0])
    # Divisibility False
    monkey_false = re.search(r"\d+", lines[5])
    if monkey_false:
        m["monkey_false"] = int(monkey_false[0])

    m["inspections1"] = 0  # For part 1
    m["inspections2"] = 0  # For part 2

    # Append monkey to monkeys dictionary.
    monkeys[num] = m

# For part 2
p2_num = math.lcm(*[monkey["divisibility"] for monkey in monkeys.values()])


# Play all rounds
for round in range(rounds2):
    # Play a single round
    for monkey, stats in monkeys.items():
        # Part 1
        if round < rounds1:
            for item in stats["items1"]:
                worry1 = eval(stats["operation"].replace(
                    "old", str(item))) // 3
                if worry1 % stats["divisibility"] == 0:
                    monkeys[stats["monkey_true"]]["items1"].append(worry1)
                else:
                    monkeys[stats["monkey_false"]]["items1"].append(worry1)
            stats["inspections1"] += len(stats["items1"])
            stats["items1"] = []

        # Part 2
        for item in stats["items2"]:
            worry2 = eval(stats["operation"].replace(
                "old", str(item))) % p2_num
            if worry2 % stats["divisibility"] == 0:
                monkeys[stats["monkey_true"]]["items2"].append(worry2)
            else:
                monkeys[stats["monkey_false"]]["items2"].append(worry2)
        stats["inspections2"] += len(stats["items2"])
        stats["items2"] = []

# Part 1
inspections = [monkey["inspections1"] for monkey in monkeys.values()]
p1 = math.prod(sorted(inspections, reverse=True)[:2])
print("Solution Part 1:", p1)

# Part 2
inspections = [monkey["inspections2"] for monkey in monkeys.values()]
p2 = math.prod(sorted(inspections, reverse=True)[:2])
print("Solution Part 2:", p2)
