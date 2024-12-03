import pathlib
import re

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0
flag = True
for l in lines:
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, l)

    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x, y = map(int, match[4:-1].split(","))
                ret += x * y

print(ret)

# One-liner
# print(sum(int(x) * int(y) for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()) if (flag := (match == "do()") or (match != "don't()" and globals().get("flag", True))) and match.startswith("mul(") for x, y in [match[4:-1].split(",")]))

# One-liner un-rolled
print(
    sum(
        int(x) * int(y)
        for match in re.findall(
            r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()
        )
        if (
            flag := (match == "do()")
            or (match != "don't()" and globals().get("flag", True))
        )
        and match.startswith("mul(")
        for x, y in [match[4:-1].split(",")]
    )
)
