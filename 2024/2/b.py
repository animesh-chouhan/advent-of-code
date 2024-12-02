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

    if check(nums) or check(nums[::-1]):
        ret += 1
        continue

    if any(check(nums[:i] + nums[i + 1 :]) for i in range(len(nums))):
        ret += 1
        continue

    nums = nums[::-1]
    if any(check(nums[:i] + nums[i + 1 :]) for i in range(len(nums))):
        ret += 1
        continue

print(ret)

# One-liner
# print(sum(1 for l in lines if (not(check := lambda nums: all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)))) or (check(nums := list(map(int, l.split())))) or (check(nums[::-1])) or any(check(nums[:i] + nums[i + 1 :]) for i in range(len(nums))) or any(check((nums[:i] + nums[i + 1 :])[::-1]) for i in range(len(nums)))))

# One-liner un-rolled
print(
    sum(
        1
        for l in lines
        if (
            not (
                check := lambda nums: all(
                    1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)
                )
            )
        )
        or (check(nums := list(map(int, l.split()))))
        or (check(nums[::-1]))
        or any(check(nums[:i] + nums[i + 1 :]) for i in range(len(nums)))
        or any(check((nums[:i] + nums[i + 1 :])[::-1]) for i in range(len(nums)))
    )
)
