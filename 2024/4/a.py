import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    # text = f.read()
    lines = f.read().split("\n")

ret = 0

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
target = "XMAS"


def check(i, j, mi, mj):
    for k in range(len(target)):
        if (
            0 <= i + mi * k < r
            and 0 <= j + mj * k < c
            and grid[i + mi * k][j + mj * k] == target[k]
        ):
            continue
        else:
            return False
    else:
        return True


for i in range(r):
    for j in range(c):
        for mi, mj in directions:
            if check(i, j, mi, mj):
                ret += 1

print(ret)

print(
    sum(
        1
        for i in range(len(grid))
        for j in range(len(grid[0]))
        for mi, mj in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, -1),
            (1, 1),
            (-1, 1),
            (-1, -1),
        ]
        if all(
            0 <= i + mi * k < len(grid)
            and 0 <= j + mj * k < len(grid[0])
            and grid[i + mi * k][j + mj * k] == "XMAS"[k]
            for k in range(len("XMAS"))
        )
    )
)
