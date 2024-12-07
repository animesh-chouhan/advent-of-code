ret = 0

for line in open("input.txt").read().splitlines():
    target, nums = line.split(": ")
    target = int(target)
    nums = list(map(int, nums.split()))

    poss = set()
    for ops in range(pow(2, len(nums) - 1)):
        val = nums[0]
        for i, op in enumerate(format(ops, f"0{len(nums) - 1}b")):
            if op == "0":
                val += nums[i + 1]
            elif op == "1":
                val *= nums[i + 1]

        poss.add(val)

    if target in poss:
        ret += target

print(ret)
