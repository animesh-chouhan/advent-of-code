import re
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")

bag = {"red": 12, "green": 13, "blue": 14}

ids = []
for line in lines:
    game_id = int(line.split(":")[0].split()[1])
    # print(game_id)
    cubes = line.split(":")[1]
    turns = cubes.split(";")

    flag = False
    for turn in turns:
        colors = turn.split(",")
        # print(colors)
        red = [color.split()[0] for color in colors if "red" in color] or [0]
        green = [color.split()[0] for color in colors if "green" in color] or [0]
        blue = [color.split()[0] for color in colors if "blue" in color] or [0]

        # print(red, green, blue)
        if (
            int(red[0]) > bag["red"]
            or int(green[0]) > bag["green"]
            or int(blue[0]) > bag["blue"]
        ):
            flag = True
        # print(flag)

    if flag == False:
        ids.append(int(game_id))

# print(ids)
print(sum(ids))
