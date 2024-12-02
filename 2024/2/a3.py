import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0

for l in lines:
    nums = list(map(int, l.split()))
    if nums[1] < nums[0]:
        nums = [-num for num in nums]

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] < 1 or nums[i + 1] - nums[i] > 3:
            break
    else:
        ret += 1


print(ret)
