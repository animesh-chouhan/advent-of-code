import pathlib
import itertools

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().splitlines()

ret = 0

for line in lines:
    target, nums = line.split(": ")
    target = int(target)
    nums = list(map(int, nums.split()))

    poss = set()
    operations = itertools.product("+*", repeat=len(nums) - 1)
    for ops in operations:
        val = nums[0]
        for i, op in enumerate(ops):
            if op == "+":
                val += nums[i + 1]
            elif op == "*":
                val *= nums[i + 1]

        poss.add(val)

    if target in poss:
        ret += target

print(ret)
