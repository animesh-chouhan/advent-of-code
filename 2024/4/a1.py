import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    # text = f.read()
    lines = f.read().split("\n")

# One-liner
# print(sum(1 for i in range(len(lines)) for j in range(len(lines[0])) for mi, mj in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)] if all(0 <= i + mi * k < len(lines) and 0 <= j + mj * k < len(lines[0]) and lines[i + mi * k][j + mj * k] == "XMAS"[k] for k in range(len("XMAS")))))

# One-liner un-rolled
print(
    sum(
        1
        for i in range(len(lines))
        for j in range(len(lines[0]))
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
            0 <= i + mi * k < len(lines)
            and 0 <= j + mj * k < len(lines[0])
            and lines[i + mi * k][j + mj * k] == "XMAS"[k]
            for k in range(len("XMAS"))
        )
    )
)
