import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().strip()


nums = list(map(int, lines))

# print(nums)

blocks = []
for i in range(len(nums)):
    if i % 2 == 0:
        blocks.extend([i // 2] * nums[i])
    else:
        blocks.extend(["."] * nums[i])

# print(blocks)


stack = blocks

while True:
    last = stack.pop()
    if last != ".":
        try:
            idx = stack.index(".")
            stack[idx] = last
        except:
            stack.append(last)
            break

# print(stack)


ret = 0
for i, e in enumerate(stack):
    ret += i * e

print(ret)
