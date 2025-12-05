import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    range, items = f.read().split("\n\n")
    range = [list(map(int, e.split("-"))) for e in range.split("\n")]
    items = [int(e) for e in items.split("\n")]

ret = 0
for i in items:
    for r in range:
        if r[0] <= i <= r[1]:
            ret += 1
            break


print(ret)
