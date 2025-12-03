import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
# print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

ret = 0

# for l in lines:
#     val = []

#     def visit(i, s):
#         if i >= len(l):
#             return
#         if len(s) == 12:
#             # print(s)
#             # global val
#             val.append(int(s))
#             return

#         visit(i + 1, s)
#         visit(i + 1, s + l[i])

#     visit(0, "")
#     print(max(val))


# print(ret)


from itertools import combinations

for l in lines:
    best = 0
    for comb in combinations(l, 12):
        val = int("".join(comb))
        if val > best:
            best = val
    print(best)
