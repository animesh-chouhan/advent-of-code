import pathlib
from collections import defaultdict

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    line = f.read().strip()


nums = list(map(int, line.split()))
print(nums)

steps = 25

for _ in range(steps):
    i = 0
    while i < len(nums):
        l = len(str(nums[i]))
        if nums[i] == 0:
            nums[i] = 1
            i += 1
        elif l % 2 == 0:
            # print(l, nums[i], int(str(nums[i])[: l // 2]), str(nums[i])[l // 2 :])
            nums.insert(i + 1, int(str(nums[i])[l // 2 :]))
            nums[i] = int(str(nums[i])[: l // 2])
            i += 2

        else:
            nums[i] *= 2024
            i += 1

print(len(nums))
