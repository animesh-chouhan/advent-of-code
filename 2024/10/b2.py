grid = [list(map(int, line)) for line in open("input.txt").read().splitlines()]
r, c = len(grid), len(grid[0])
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def visit(i, j):
    if grid[i][j] == 9:
        return 1
    return sum(
        visit(i + dx, j + dy)
        for dx, dy in dir
        if 0 <= i + dx < r
        and 0 <= j + dy < c
        and grid[i + dx][j + dy] == grid[i][j] + 1
    )


print(sum(visit(i, j) for i in range(r) for j in range(c) if grid[i][j] == 0))
