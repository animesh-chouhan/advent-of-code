import pathlib
import re

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    text = f.read()

ret = 0

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, text)
ret += sum((int(x) * int(y) for x, y in matches))

print(ret)


# print(sum(int(x) * int(y) for l in lines for x, y in re.findall(r"mul\((\d+),(\d+)\)", l)))

print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", text)))


# print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", open('input.txt').read())))
print(
    sum(
        int(x) * int(y)
        for x, y in re.findall(r"mul\((\d+),(\d+)\)", open("input.txt").read())
    )
)
