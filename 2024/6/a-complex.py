grid = [list(line) for line in open("input.txt").read().split("\n")]
r, c = len(grid), len(grid[0])
start = next(complex(i, j) for i in range(r) for j in range(c) if grid[i][j] == "^")


def visit_complex(point, direction, path):
    while path.add(point) is None:
        new_point = point + direction
        x, y = int(new_point.real), int(new_point.imag)
        if not (0 <= x < r and 0 <= y < c):
            return path
        if grid[x][y] == "#":
            direction *= -1j
        else:
            point = new_point


path = visit_complex(start, -1, set())
print(len(path))
