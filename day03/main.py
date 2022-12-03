data = open("input.txt", "r").read().strip().split()


def item_to_num(string):
    res = ord(string)
    res = res - ord("A") + 27 if string.isupper() else res - ord("a") + 1
    return res


# Part 1
same_item = []
for rucksack in data:
    split = len(rucksack)//2
    compartment1 = rucksack[:split]
    compartment2 = rucksack[split:]
    item = set.intersection(set(compartment1), set(compartment2)).pop()
    same_item.append(item)
part1 = sum(item_to_num(item) for item in same_item)

# Part 2
same_group = []
for i in range(0, len(data), 3):
    rucksack1 = data[i]
    rucksack2 = data[i+1]
    rucksack3 = data[i+2]
    item = set.intersection(set(rucksack1), set(rucksack2),
                            set(rucksack3)).pop()
    same_group.append(item)
part2 = sum(item_to_num(item) for item in same_group)


print(f"Solution Part 1: {part1}")
print(f"Solution Part 2: {part2}")
