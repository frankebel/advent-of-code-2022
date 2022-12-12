# https://adventofcode.com/2022/day/11

import copy
import math
import re


def run_rounds(monkeys: dict, rounds: int, relief: int) -> int:
    monkeys = copy.deepcopy(monkeys)
    for monkey in monkeys.values():
        monkey["inspections"] = 0
    # Loop over rounds
    for _ in range(rounds):
        for monkey, stats in monkeys.items():
            for item in stats["items"]:
                worry = stats["operation"](item)
                # Hard coded p1, p2.
                worry = worry // relief if relief == 3 else worry % relief
                if worry % stats["divisibility"] == 0:
                    monkeys[stats["monkey_true"]]["items"].append(worry)
                else:
                    monkeys[stats["monkey_false"]]["items"].append(worry)
            stats["inspections"] += len(stats["items"])
            stats["items"] = []

    # Find two highest inspections and return their product.
    inspections = [monkey["inspections"] for monkey in monkeys.values()]
    return math.prod(sorted(inspections, reverse=True)[:2])


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
    m["items"] = starting_items
    # Operation
    operation = lines[2].split("= ")[-1].split()
    match operation:
        case "old", "*", "old":
            m["operation"] = lambda x: x*x
        case "old", "*", n:
            m["operation"] = lambda x, n=int(n): x*n
        case "old", "+", n:
            m["operation"] = lambda x, n=int(n): x+n
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

    # Append monkey to monkeys dictionary.
    monkeys[num] = m


# Part 1
print("Solution Part 1:", run_rounds(monkeys, rounds1, 3))
# Part 2
p2_num = math.lcm(*[monkey["divisibility"] for monkey in monkeys.values()])
print("Solution Part 2:", run_rounds(monkeys, rounds2, p2_num))
