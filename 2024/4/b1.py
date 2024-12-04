import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    lines = f.read().split("\n")

ret = 0

grid = [list(line) for line in lines]
r, c = len(grid), len(grid[0])
directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
patterns = ["MSSM", "MMSS", "SSMM", "SMMS"]

for i in range(1, r - 1):
    for j in range(1, c - 1):
        if grid[i][j] == "A":
            if "".join([grid[i + x][j + y] for x, y in directions]) in patterns:
                ret += 1

print(ret)
