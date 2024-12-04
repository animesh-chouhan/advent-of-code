import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    lines = f.read().split("\n")

# One-liner
# print(sum(1 for i in range(1, len(lines) - 1) for j in range(1, len(lines[0]) - 1) if lines[i][j] == "A" and "".join([lines[i + x][j + y] for x, y in [(-1, -1), (-1, 1), (1, 1), (1, -1)]]) in ["MSSM", "MMSS", "SSMM", "SMMS"]))

# One-liner un-rolled
print(
    sum(
        1
        for i in range(1, len(lines) - 1)
        for j in range(1, len(lines[0]) - 1)
        if lines[i][j] == "A"
        and "".join(
            [lines[i + x][j + y] for x, y in [(-1, -1), (-1, 1), (1, 1), (1, -1)]]
        )
        in ["MSSM", "MMSS", "SSMM", "SMMS"]
    )
)
