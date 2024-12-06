grid = [list(line) for line in open("input.txt").read().split("\n")]
r, c = len(grid), len(grid[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = next((i, j) for i in range(r) for j in range(c) if grid[i][j] == "^")


def visit(i, j, d, path):
    while (i, j, d) not in path:
        path.add((i, j, d))
        dx, dy = directions[d]
        if not (0 <= i + dx < r and 0 <= j + dy < c):
            return path
        if grid[i + dx][j + dy] == "#":
            d = (d + 1) % 4
        else:
            i, j = i + dx, j + dy


def valid(x, y):
    if grid[x][y] == "#" or (x, y) == start:
        return False
    grid[x][y], temp = "#", grid[x][y]
    path = visit(*start, 0, set())
    grid[x][y] = temp
    return path is None


path = set((x, y) for x, y, _ in visit(*start, 0, set()))
print(f"Part 1: {len(path)}")
print(f"Part 2: {sum(1 for x, y in path if valid(x, y))}")
