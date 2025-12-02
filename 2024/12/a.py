import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")


grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()


def calc(i, j):
    stack = [(i, j)]
    visited.add((i, j))
    area, per = 0, 0

    while stack:
        x, y = stack.pop()
        area += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if (nx, ny) not in visited and grid[nx][ny] == grid[x][y]:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                elif grid[nx][ny] != grid[x][y]:
                    per += 1
            else:
                per += 1

    return area, per


ret = 0
for i in range(r):
    for j in range(c):
        if (i, j) not in visited:
            area, per = calc(i, j)
            ret += area * per

print(ret)
