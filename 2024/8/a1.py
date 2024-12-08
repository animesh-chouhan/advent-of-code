import collections

grid = [list(line) for line in open("input.txt").read().splitlines()]
r, c = len(grid), len(grid[0])
coordinates = collections.defaultdict(list)
antennas = set()

for i in range(r):
    for j in range(c):
        if grid[i][j] != ".":
            coordinates[grid[i][j]].append((i, j))


def check(x, y):
    if 0 <= x < r and 0 <= y < c:
        antennas.add((x, y))


for coordinate in coordinates.values():
    for i in range(len(coordinate)):
        for j in range(i + 1, len(coordinate)):
            x1, y1 = coordinate[i]
            x2, y2 = coordinate[j]
            check(x2 + (x2 - x1), y2 + (y2 - y1))
            check(x1 - (x2 - x1), y1 - (y2 - y1))

print(len(antennas))
