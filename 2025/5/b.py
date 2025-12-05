import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    ranges, items = f.read().split("\n\n")
    ranges = [list(map(int, e.split("-"))) for e in ranges.split("\n")]
    items = [int(e) for e in items.split("\n")]

ranges.sort()
l, r = ranges[0]
ret = r - l + 1
for i in range(1, len(ranges)):
    start, end = ranges[i]
    if r >= end:
        continue

    l = max(r + 1, start)
    r = end
    ret += r - l + 1

print(ret)
