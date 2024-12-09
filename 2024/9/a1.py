import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().strip()


nums = list(map(int, lines))
disk = []
for i in range(len(nums)):
    if i % 2 == 0:
        disk.extend([i // 2] * nums[i])
    else:
        disk.extend(["."] * nums[i])


i = 0
j = len(disk) - 1
while True:
    while disk[i] != ".":
        i += 1

    while not isinstance(disk[j], int):
        j -= 1

    if i < j:
        disk[i], disk[j] = disk[j], disk[i]
    else:
        break

# print(disk)

ret = 0
for i, e in enumerate(disk):
    if e == ".":
        continue
    ret += i * e

print(ret)
