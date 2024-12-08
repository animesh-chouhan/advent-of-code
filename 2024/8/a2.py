import collections

grid = [list(line) for line in open("input.txt").read().splitlines()]
r, c = len(grid), len(grid[0])

symbols = collections.defaultdict(list)
for i in range(r):
    for j in range(c):
        if grid[i][j] != ".":
            symbols[grid[i][j]].append((i, j))


def check(x, y):
    return 0 <= x < r and 0 <= y < c


ant = set()
for symbol in symbols.values():
    for i in range(len(symbol)):
        for j in range(i + 1, len(symbol)):
            x1, y1 = symbol[i]
            x2, y2 = symbol[j]
            for p in [(x2 + x2 - x1, y2 + y2 - y1), (x1 - (x2 - x1), y1 - (y2 - y1))]:
                if 0 <= p[0] < r and 0 <= p[1] < c:
                    ant.add(p)


print(len(ant))
