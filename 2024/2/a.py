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
        nums = nums[::-1]

    if all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)):
        ret += 1


print(ret)

# One-liner
# print(sum(1 for l in lines if ((((nums := list(map(int, l.split())))[1] > nums[0]) or (nums := nums[::-1])) and all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1)))))

# One-liner un-rolled
print(
    sum(
        1
        for l in lines
        if (
            (((nums := list(map(int, l.split())))[1] > nums[0]) or (nums := nums[::-1]))
            and all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(len(nums) - 1))
        )
    )
)
