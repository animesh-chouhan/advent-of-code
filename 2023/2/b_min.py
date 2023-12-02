import re
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n")


bag = {"red": 12, "green": 13, "blue": 14}

games = []
for line in lines:
    game_id = int(line.split(":")[0].split()[1])
    # print(game_id)
    cubes = line.split(":")[1]
    turns = cubes.split(";")

    reds = []
    greens = []
    blues = []
    for turn in turns:
        colors = turn.split(",")
        # print(colors)
        red = [color.split()[0] for color in colors if "red" in color] or [0]
        green = [color.split()[0] for color in colors if "green" in color] or [0]
        blue = [color.split()[0] for color in colors if "blue" in color] or [0]

        reds.append(int(red[0]))
        greens.append(int(green[0]))
        blues.append(int(blue[0]))

    # print(reds, greens, blues)
    games.append(max(reds) * max(greens) * max(blues))


# print(games)
print(sum(games))
