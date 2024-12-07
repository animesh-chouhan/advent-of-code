import pathlib
import itertools

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")

ret = 0

for l in lines:
    o = int(l.split(": ")[0])
    nums = list(map(int, l.split(": ")[1].split()))

    poss = set()
    ops = itertools.product("+*|", repeat=len(nums) - 1)
    for op in ops:
        val = nums[0]
        for i, p in enumerate(op):
            if p == "+":
                val += nums[i + 1]
            elif p == "*":
                val *= nums[i + 1]
            elif p == "|":
                val = int(str(val) + str(nums[i + 1]))

        poss.add(val)

    if o in poss:
        ret += o

print(ret)
