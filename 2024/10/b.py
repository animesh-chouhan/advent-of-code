import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")

grid = [list(map(int, line)) for line in lines]
r, c = len(grid), len(grid[0])
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def visit(i, j):
    if i < 0 or i >= r or j < 0 or j >= c:
        return
    if grid[i][j] == 9:
        global ret
        ret += 1
        return

    curri, currj = i, j
    for dx, dy in dir:
        i = curri + dx
        j = currj + dy
        if i < 0 or i >= r or j < 0 or j >= c:
            continue
        else:
            if grid[i][j] == grid[curri][currj] + 1:
                visit(i, j)


ret = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 0:
            visit(i, j)

print(ret)
