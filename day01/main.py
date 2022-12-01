# Read input from file
items = []
with open("day01/input.txt", "r") as f:
    items = [line.rstrip("\n") for line in f]

# Save number of calories per elf.
calories = []
# Calories which one elf has.
cal = 0

# Loop over items.
for element in items:
    if element == "":
        # New elf.
        calories.append(cal)
        cal = 0
    else:
        cal += int(element)

# First half of puzzle.
# Maximum calories one elf has.
max_calories = max(calories)
print(f"Max calories are {max_calories}")

# Second half of puzzle.
# Number of calories the highest 3 elves have.
sum3 = sum(sorted(calories, reverse=True)[:3])
print(f"Three highest are: {sum3}")
