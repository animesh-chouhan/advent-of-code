import pathlib
import sys

sys.setrecursionlimit(15000)
input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    # text = f.read()
    lines = f.read().split("\n")

ret = 0

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])

for i in range(r):
    for j in range(c):
        if grid[i][j] == "^":
            start = (i, j)


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
path = set()


def visit(i, j, d):
    path.add((i, j))
    dx, dy = directions[d % 4]
    i, j = i + dx, j + dy

    if i < 0 or i >= r or j < 0 or j >= c:
        return
    elif grid[i][j] == "#":
        visit(i - dx, j - dy, d + 1)
    else:
        visit(i, j, d)


visit(*start, 0)
# print(path)
print(len(path))
