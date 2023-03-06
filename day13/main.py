# https://adventofcode.com/2022/day/13

from functools import cmp_to_key
from json import loads
from math import prod


def comparison(left: int | list, right: int | list) -> int:
    match left, right:
        case int(left), int(right):
            return left - right
        case int(), list():
            return comparison([left], right)
        case list(), int():
            return comparison(left, [right])
        case list(left), list(right):
            for i, j in zip(left, right):
                if (res := comparison(i, j)) != 0:
                    return res
            return comparison(len(left), len(right))

    raise Exception(f"Could not compare {left} to {right}")


data = [
    loads(packet)
    for packet in open("input.txt", "r").read().strip().split("\n")
    if packet != ""
]

# Part 1
p1 = 0
for i, (left, right) in enumerate(zip(data[::2], data[1::2]), 1):
    if comparison(left, right) < 0:
        p1 += i
print("Solution Part 1:", p1)

# Part 2
divider_packets = [[[2]], [[6]]]
data.extend(divider_packets)
packets_sorted = sorted(data, key=cmp_to_key(comparison))
p2 = prod(i for i, p in enumerate(packets_sorted, 1) if p in divider_packets)
print("Solution Part 2:", p2)
