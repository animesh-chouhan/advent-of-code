import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")

ret = 0

symbols = defaultdict(list)

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])

for i in range(r):
    for j in range(c):
        if grid[i][j] != ".":
            symbols[grid[i][j]].append((i, j))

ant = set()


def check(i, j):
    return 0 <= i < r and 0 <= j < c


for symbol in symbols.values():
    for i in range(len(symbol)):
        for j in range(i + 1, len(symbol)):

            x1, y1 = symbol[i]
            x2, y2 = symbol[j]

            for j in range(60):
                c1 = (x2 + j * (x2 - x1), y2 + j * (y2 - y1))
                if check(*c1):
                    ant.add(c1)

            for j in range(60):
                c2 = (x1 - j * (x2 - x1), y1 - j * (y2 - y1))
                if check(*c2):
                    ant.add(c2)

print(len(ant))
