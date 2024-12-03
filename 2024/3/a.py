import pathlib
import re

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0
for l in lines:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, l)
    ret += sum((int(x) * int(y) for x, y in matches))

print(ret)

# One-liner
# print(sum(int(x) * int(y) for l in lines for x, y in re.findall(r"mul\((\d+),(\d+)\)", l)))

# One-liner un-rolled
print(
    sum(int(x) * int(y) for l in lines for x, y in re.findall(r"mul\((\d+),(\d+)\)", l))
)
