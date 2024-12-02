import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

z = 0
for l in lines:
    nums = list(map(int, l.split()))
    if all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)):
        z += 1
    if all(1 <= nums[i] - nums[i + 1] <= 3 for i in range(len(nums) - 1)):
        z += 1
print(z)
