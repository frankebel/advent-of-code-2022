import numpy as np


def insert_array(value: int, array: np.ndarray):
    """Insert value in decreasing array."""
    for i, element in enumerate(array):
        if value > element:
            array[i] = value
            value = element


# Save top 3 calories of elves.
top3 = np.zeros(3, dtype=np.int32)

# Read input from file
items = []
f = open("day01/input.txt", "r")
line = ""
while (line := f.readline()) != "":
    if line != "\n":
        # Append to current elf.
        items.append(line.removesuffix("\n"))
    else:
        # Calculate calories of elf and reset for next.
        calories = np.asarray(items).astype(np.int32).sum(dtype=np.int32)
        insert_array(calories, top3)
        items = []
f.close()

# First half of puzzle.
# Maximum calories one elf has.
max_calories = top3[0]
print(f"Max calories are {max_calories}")

# Second half of puzzle.
# Number of calories the highest 3 elves have.
sum3 = np.sum(top3)
print(f"Three highest are: {sum3}")
