import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
with open(input_path) as f:
    lines = f.read().split("\n")

ret = 0

for l in lines:
    o = int(l.split(": ")[0])
    nums = list(map(int, l.split(": ")[1].split()))
    poss = set()

    def visit(i, val):
        if i >= len(nums):
            poss.add(val)
            return
        visit(i + 1, val + nums[i])
        visit(i + 1, val * nums[i])

    visit(1, nums[0])
    if o in poss:
        ret += o

print(ret)
