from collections import defaultdict

with open("input.txt") as f:
    steps = [l.strip() for l in f]

grid  = defaultdict(lambda: defaultdict(int))
grid2 = defaultdict(lambda: defaultdict(int))

dists = []
times = []

for symbol, wire in enumerate(steps):
    x, y = 0, 0
    counter = 1
    for d, n in [(w[0], int(w[1:])) for w in wire.split(",")]:
        for _ in range(n):
            if   d == "R": x += 1
            elif d == "L": x -= 1
            elif d == "U": y += 1
            elif d == "D": y -= 1
            else: raise Exception()

            grid2[x][y] += counter

            if grid[x][y] != 0 and grid[x][y] != symbol+1:
                dists.append(abs(x)+abs(y))
                times.append(grid2[x][y])

            grid[x][y] = symbol+1
            counter += 1

print(min(dists))
print(min(times))
