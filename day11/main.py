# https://adventofcode.com/2022/day/10

import math
import re

rounds = 20
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
    m["items"] = starting_items
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

    # For part 1
    m["inspections"] = 0

    # Append monkey to monkeys dictionary.
    monkeys[num] = m


for round in range(rounds):
    # Play a round
    for monkey, stats in monkeys.items():
        for item in stats["items"]:
            worry_lvl = eval(stats["operation"].replace("old", str(item))) // 3
            if worry_lvl % stats["divisibility"] == 0:
                monkeys[stats["monkey_true"]]["items"].append(worry_lvl)
            else:
                monkeys[stats["monkey_false"]]["items"].append(worry_lvl)
        stats["inspections"] += len(stats["items"])
        stats["items"] = []

# Part 1
inspections = [monkey["inspections"] for monkey in monkeys.values()]
p1 = math.prod(sorted(inspections, reverse=True)[:2])
print("Solution Part 1:", p1)

# Part 2
p2 = 0
print("Solution Part 2:", p2)
