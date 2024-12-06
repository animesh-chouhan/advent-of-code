import pathlib
import sys

sys.setrecursionlimit(10000)

grid = [list(line) for line in open("input.txt").read().split("\n")]
r, c = len(grid), len(grid[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = next((i, j) for i in range(r) for j in range(c) if grid[i][j] == "^")


def visit(i, j, d, path):
    if (i, j, d) in path:
        return None
    path.add((i, j, d))
    dx, dy = directions[d]
    if not (0 <= i + dx < r and 0 <= j + dy < c):
        return path
    elif grid[i + dx][j + dy] == "#":
        return visit(i, j, (d + 1) % 4, path)
    else:
        return visit(i + dx, j + dy, d, path)


def valid(x, y):
    if grid[x][y] == "#" or (x, y) == start:
        return False
    store = grid[x][y]
    grid[x][y] = "#"
    path = visit(*start, 0, set())
    grid[x][y] = store
    return path is None


path = set((x, y) for x, y, _ in visit(*start, 0, set()))
print(len(path))
print(sum(1 for x, y in path if valid(x, y)))
