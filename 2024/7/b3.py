ret = 0

for line in open("input.txt").read().splitlines():
    target, nums = line.split(": ")
    target = int(target)
    nums = list(map(int, nums.split()))

    def visit(i, val):
        if i >= len(nums):
            return val == target
        return (
            visit(i + 1, val + nums[i])
            or visit(i + 1, val * nums[i])
            or visit(i + 1, int(f"{str(val)}{str(nums[i])}"))
        )

    if visit(1, nums[0]):
        ret += target

print(ret)
