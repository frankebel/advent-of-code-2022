import string

data = open("input.txt", "r").read().strip().split()

# Part 1
p1 = 0
for rucksack in data:
    c1, c2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    p1 += string.ascii_letters.index((set(c1) & set(c2)).pop()) + 1

# Part 2
p2 = 0
for i in range(0, len(data), 3):
    r1, r2, r3 = data[i:i+3]
    p2 += string.ascii_letters.index((set(r1) & set(r2) & set(r3)).pop()) + 1

print(f"Solution Part 1: {p1}")
print(f"Solution Part 2: {p2}")
