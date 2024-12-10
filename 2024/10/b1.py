grid = [list(map(int, line)) for line in open("input.txt").read().splitlines()]
r, c = len(grid), len(grid[0])
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ret = [0]


def visit(i, j):
    if grid[i][j] == 9:
        ret[0] += 1
        return

    for dx, dy in dir:
        ni, nj = i + dx, j + dy
        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == grid[i][j] + 1:
            visit(ni, nj)


for i in range(r):
    for j in range(c):
        if grid[i][j] == 0:
            visit(i, j)

print(ret[0])
