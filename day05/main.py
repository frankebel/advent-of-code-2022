# https://adventofcode.com/2022/day/5

import copy

data = open("input.txt", "r").read().strip().split("\n")

# Split at empty line
stack_text, moves_text = data[: data.index("")], data[data.index("") + 1 :]

# Create stacks
stack_text = stack_text[::-1]
stacks = [
    [crate for row in stack_text[1:] if (crate := row[4 * i + 1]) != " "]
    for i in range(int(len(stack_text[0].split())))
]
# Add dummy to set starting index to 1
stacks.insert(0, [""])

# Create moves
moves = [[int(number) for number in row.split()[1::2]] for row in moves_text]

# Operate moves on stacks
stacks1, stacks2 = copy.deepcopy(stacks), copy.deepcopy(stacks)
for move in moves:
    n, src, dest = move
    # Part 1
    stacks1[dest].extend(stacks1[src][-n:][::-1])  # Add crates
    del stacks1[src][-n:]  # Remove crates
    # Part 2
    stacks2[dest].extend(stacks2[src][-n:])  # Add crates
    del stacks2[src][-n:]  # Remove crates

# Combine top crates from each stack
p1 = "".join([stack[-1] for stack in stacks1])
p2 = "".join([stack[-1] for stack in stacks2])

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
