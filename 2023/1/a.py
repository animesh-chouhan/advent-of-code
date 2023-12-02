import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

nums = []
for line in lines:
    temp = [char for char in line if char.isdigit()]
    num = int(temp[0] + temp[-1])
    nums.append(num)

print(sum(nums))
