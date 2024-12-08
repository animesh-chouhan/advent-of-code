import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])

symbols = defaultdict(list)
for i in range(r):
    for j in range(c):
        if grid[i][j] != ".":
            symbols[grid[i][j]].append((i, j))


def check(x, y):
    return 0 <= x < r and 0 <= y < c


ant = set()
for symbol in symbols.values():
    for i in range(len(symbol)):
        for j in range(i + 1, len(symbol)):

            x1, y1 = symbol[i]
            x2, y2 = symbol[j]

            c1 = (x2 + (x2 - x1), y2 + (y2 - y1))
            if check(*c1):
                ant.add(c1)

            c2 = (x1 - (x2 - x1), y1 - (y2 - y1))
            if check(*c2):
                ant.add(c2)

print(len(ant))
