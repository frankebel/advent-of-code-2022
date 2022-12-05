# https://adventofcode.com/2022/day/5

import copy

data = open("input.txt", "r").read().strip().split("\n")

# Split at empty line
stack_text, moves_text = data[:data.index("")], data[data.index("") + 1:]

# Create stacks
stack_text = stack_text[::-1]
num_stacks = int(stack_text[0].split()[-1])
stacks = []
for i in range(num_stacks):
    stack = [row[4*i+1] for row in stack_text[1:]]  # Extract crates
    stack = [item for item in stack if item != " "]  # Remove empty
    stacks.append(stack)

# Create moves
moves = [[int(number) for number in row.split()[1::2]] for row in moves_text]

# Operate moves on stacks
stacks1, stacks2 = copy.deepcopy(stacks), copy.deepcopy(stacks)
for move in moves:
    n, src, dest = move
    # Part 1
    stacks1[dest-1].extend(stacks1[src-1][-1:-n-1:-1])  # Add crates
    stacks1[src-1] = stacks1[src-1][:-n]  # Remove crates
    # Part 2
    stacks2[dest-1].extend(stacks2[src-1][-n:])  # Add crates
    stacks2[src-1] = stacks2[src-1][:-n]  # Remove crates

# Combine top crates from each stack
p1 = "".join([stack[-1] for stack in stacks1])
p2 = "".join([stack[-1] for stack in stacks2])

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
