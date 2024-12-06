import sys

sys.setrecursionlimit(15000)

grid = open("input.txt").read().split("\n")
r, c = len(grid), len(grid[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = next((i, j) for i in range(r) for j in range(c) if grid[i][j] == "^")


def visit(i, j, d, path):
    path.add((i, j))
    dx, dy = directions[d]
    if not (0 <= i + dx < r and 0 <= j + dy < c):
        return path
    elif grid[i + dx][j + dy] == "#":
        return visit(i, j, (d + 1) % 4, path)
    else:
        return visit(i + dx, j + dy, d, path)


def visit_iterative(i, j, d, path):
    while True:
        path.add((i, j))
        dx, dy = directions[d]
        if not (0 <= i + dx < r and 0 <= j + dy < c):
            return path
        if grid[i + dx][j + dy] == "#":
            d = (d + 1) % 4
        else:
            i, j = i + dx, j + dy


path = visit_iterative(*start, 0, set())
print(len(path))
