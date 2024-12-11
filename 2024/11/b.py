import pathlib
from collections import defaultdict
import functools

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    line = f.read().strip()


nums = list(map(int, line.split()))
print(nums)

steps = 75


@functools.cache
def visit(num, step):
    print(num, steps)
    if step == steps:
        return 1
    if num == 0:
        return visit(1, step + 1)
    elif len(str(num)) % 2 == 0:
        s = str(num)
        l = len(s)
        return visit(int(s[: l // 2]), step + 1) + visit(int(s[l // 2 :]), step + 1)
    else:
        return visit(num * 2024, step + 1)


ret = 0
for num in nums:
    ret += visit(num, 0)

print(ret)
