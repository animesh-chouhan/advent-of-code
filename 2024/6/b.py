import pathlib
import sys

sys.setrecursionlimit(10000)
input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    lines = f.read().split("\n")

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = next((i, j) for i in range(r) for j in range(c) if grid[i][j] == "^")


def valid(x, y):
    # if grid[x][y] == "#" or (x, y) == start:
    #     return False

    path = set()
    store = grid[x][y]
    grid[x][y] = "#"

    def visit(i, j, d):
        if (i, j, d) in path:
            return True
        path.add((i, j, d))
        dx, dy = directions[d]
        ni, nj = i + dx, j + dy
        if ni < 0 or ni >= r or nj < 0 or nj >= c:
            return False
        elif grid[ni][nj] == "#":
            return visit(i, j, (d + 1) % 4)
        else:
            return visit(ni, nj, d)

    res = visit(*start, 0)
    grid[x][y] = store
    return res


print(sum(1 for i in range(r) for j in range(c) if valid(i, j)))
