# https://adventofcode.com/2022/day/9

data = open("input.txt", "r").read().strip().split("\n")

head = complex(0, 0)
tail = complex(0, 0)
visited = {complex(tail)}
direction = {"R": 1, "L": -1, "U": 1j, "D": -1j}

for motion in data:
    dir, n_steps = motion.split()
    n_steps = int(n_steps)

    for _ in range(n_steps):
        head += direction[dir]
        dist = head - tail
        if abs(dist) >= 2:
            if dist.real > 0:
                tail += 1
            elif dist.real < 0:
                tail -= 1
            if dist.imag > 0:
                tail += 1j
            elif dist.imag < 0:
                tail -= 1j
            visited.add(tail)


p1 = len(visited)
p2 = 0
print("Solution Part 1:", p1)
print("Solution Part 2:", p2)
