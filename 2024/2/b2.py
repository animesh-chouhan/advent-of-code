import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")


def check(nums):
    return all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))


ret = 0
for l in lines:
    nums = list(map(int, l.split()))

    for i in range(len(nums) - 1):
        if 1 <= nums[i + 1] - nums[i] <= 3:
            continue
        else:
            if check(nums[:i] + nums[i + 1 :]) or check(nums[: i + 1] + nums[i + 2 :]):
                ret += 1
            break
    else:
        ret += 1

    nums = nums[::-1]
    for i in range(len(nums) - 1):
        if 1 <= nums[i + 1] - nums[i] <= 3:
            continue
        else:
            if check(nums[:i] + nums[i + 1 :]) or check(nums[: i + 1] + nums[i + 2 :]):
                ret += 1
            break
    else:
        ret += 1

print(ret)
