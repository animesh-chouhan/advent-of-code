import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

digits = mapping.keys()

nums = []
for line in lines:
    temp = []
    for i, char in enumerate(line):
        if char.isdigit():
            temp.append(char)

        for digit in digits:
            if char == digit[0]:
                if digit == line[i : i + len(digit)]:
                    temp.append(mapping[digit])
                    # print(digit)

    # print(temp)
    num = int(temp[0] + temp[-1])
    # print(num)
    nums.append(num)

print(sum(nums))
