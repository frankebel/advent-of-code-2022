# https://adventofcode.com/2022/day/9

data = open("input.txt", "r").read().strip().split("\n")

n_knots = 10
rope = [complex(0, 0) for _ in range(n_knots)]
visited = [set([knot]) for knot in rope]
direction = {"R": 1, "L": -1, "U": 1j, "D": -1j}

for motion in data:
    dir, n_steps = motion.split()
    for _ in range(int(n_steps)):
        for i, knot in enumerate(rope):
            if i == 0:
                # Update head knot.
                rope[0] += direction[dir]
            else:
                # Update all other knots.
                dist = rope[i - 1] - knot  # Distance to previous knot.
                if abs(dist) >= 2:
                    rope[i] += complex(
                        (dist.real > 0) - (dist.real < 0),
                        (dist.imag > 0) - (dist.imag < 0),
                    )
                    visited[i].add(rope[i])

p1 = len(visited[1])
p2 = len(visited[-1])
print("Solution Part 1:", p1)
print("Solution Part 2:", p2)
