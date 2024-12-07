import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")

ret = 0

for line in lines:
    target, nums = line.split(": ")
    target = int(target)
    nums = list(map(int, nums.split()))
    flag = False

    def visit(i, val):
        if i >= len(nums):
            if val == target:
                global flag
                flag = True
            return
        visit(i + 1, val + nums[i])
        visit(i + 1, val * nums[i])

    visit(1, nums[0])
    if flag:
        ret += target

print(ret)
