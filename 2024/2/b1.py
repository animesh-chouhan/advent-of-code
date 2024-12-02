import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")


def check(nums):
    return all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))


def check_seq(nums):
    for i in range(len(nums) - 1):
        if 1 <= nums[i + 1] - nums[i] <= 3:
            continue
        else:
            if check(nums[:i] + nums[i + 1 :]) or check(nums[: i + 1] + nums[i + 2 :]):
                return True
            break
    else:
        return True
    return False


ret = 0
for l in lines:
    nums = list(map(int, l.split()))
    if check_seq(nums) or check_seq(nums[::-1]):
        ret += 1
print(ret)
