with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")

# Part 1
mapping1 = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
dwl1 = {0: 3, 1: 6, 2: 0}  # 0 is draw, 1 is win, 2 is loss
data1 = [[mapping1[game[0]], mapping1[game[2]]] for game in data]
shape1 = [game[-1] for game in data1]
outcome1 = [dwl1[(game[1] - game[0]) % 3] for game in data1]

# Part 2
mapping2 = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}
mp = {"X": -1, "Y": 0, "Z": 1}
# "+ 2 mod 3 + 1" to map 4 -> 1, 0 -> 3
shape2 = [(mapping2[game[0]] + mp[game[2]] + 2) % 3 + 1 for game in data]
outcome2 = [mapping2[game[2]] for game in data]

print(f"Solution Part 1: {sum(outcome1) + sum(shape1)}")
print(f"Solution Part 2: {sum(outcome2) + sum(shape2)}")
