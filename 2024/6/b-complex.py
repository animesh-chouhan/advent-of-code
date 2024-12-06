grid = [list(line) for line in open("input.txt").read().split("\n")]
r, c = len(grid), len(grid[0])
start = next(complex(i, j) for i in range(r) for j in range(c) if grid[i][j] == "^")


def visit(pos, direction, path):
    while (pos, direction) not in path:
        path.add((pos, direction))
        new_pos = pos + direction
        x, y = int(new_pos.real), int(new_pos.imag)
        if not (0 <= x < r and 0 <= y < c):
            return path
        if grid[x][y] == "#":
            direction *= -1j
        else:
            pos = new_pos


def valid(x, y):
    if grid[x][y] == "#" or (x, y) == start:
        return False
    grid[x][y], temp = "#", grid[x][y]
    path = visit(start, -1, set())
    grid[x][y] = temp
    return path is None


path = set(pos for pos, d in visit(start, -1, set()))
print(f"Part 1: {len(path)}")
print(f"Part 2: {sum(1 for pos in path if valid(int(pos.real), int(pos.imag)))}")
