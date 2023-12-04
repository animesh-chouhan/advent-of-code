import re
import time
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

symbols = "*"

start_time = time.time()

points = []
for i, line in enumerate(lines):
    card_num = line.split(":")[0].split()[1]
    numbers = line.split(":")[1]
    win_num = numbers.split("|")[0].split()
    our_num = numbers.split("|")[1].split()
    # print(win_num)
    # print(our_num)

    temp = [num for num in our_num if num in win_num]
    # print(len(temp))
    if temp:
        points.append(pow(2, len(temp) - 1))


print(sum(points))
print(f"Time taken: {time.time() - start_time}")
