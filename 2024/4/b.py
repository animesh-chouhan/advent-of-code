import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    lines = f.read().split("\n")

ret = 0

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])

for i in range(1, r - 1):
    for j in range(1, c - 1):
        if grid[i][j] == "A":
            if (
                grid[i - 1][j - 1] == "M"
                and grid[i - 1][j + 1] == "S"
                and grid[i + 1][j + 1] == "S"
                and grid[i + 1][j - 1] == "M"
            ):
                ret += 1

            if (
                grid[i - 1][j - 1] == "M"
                and grid[i - 1][j + 1] == "M"
                and grid[i + 1][j + 1] == "S"
                and grid[i + 1][j - 1] == "S"
            ):
                ret += 1

            if (
                grid[i - 1][j - 1] == "S"
                and grid[i - 1][j + 1] == "S"
                and grid[i + 1][j + 1] == "M"
                and grid[i + 1][j - 1] == "M"
            ):
                ret += 1

            if (
                grid[i - 1][j - 1] == "S"
                and grid[i - 1][j + 1] == "M"
                and grid[i + 1][j + 1] == "M"
                and grid[i + 1][j - 1] == "S"
            ):
                ret += 1
print(ret)
