import pathlib
import re

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"

with open(input_path) as f:
    text = f.read()

ret = 0
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, text)
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x, y = map(int, match[4:-1].split(","))
            ret += x * y

print(ret)


# print(
#     sum(
#         int(x) * int(y)
#         for match in re.findall(
#             r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()
#         )
#         if (
#             flag := (
#                 True
#                 if (match == "do()")
#                 else (
#                     False
#                     if match == "don't()"
#                     else (flag if "flag" in globals() else True)
#                 )
#             )
#         )
#         and match.startswith("mul(")
#         for x, y in [match[4:-1].split(",")]
#     )
# )


# print(
#     sum(
#         int(x) * int(y)
#         for match in re.findall(
#             r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()
#         )
#         if (
#             flag := (match == "do()")
#             or (match != "don't()" and (flag if "flag" in globals() else True))
#         )
#         and match.startswith("mul(")
#         for x, y in [match[4:-1].split(",")]
#     )
# )


# print(sum(int(x) * int(y) for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()) if (flag := (match == "do()") or (match != "don't()" and globals().get("flag", True))) and match.startswith("mul(") for x, y in [match[4:-1].split(",")]))
print(
    sum(
        int(x) * int(y)
        for match in re.findall(
            r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open("input.txt").read()
        )
        if (
            flag := (match == "do()")
            or (match != "don't()" and globals().get("flag", True))
        )
        and match.startswith("mul(")
        for x, y in [match[4:-1].split(",")]
    )
)
