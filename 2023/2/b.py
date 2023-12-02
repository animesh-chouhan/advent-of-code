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
    game_id = int(re.findall(r"\d+", re.findall(r"Game \d+", line)[0])[0])
    # print(game_id)
    cubes = line[7:]
    sets = cubes.split(";")

    reds = []
    greens = []
    blues = []
    for sset in sets:
        colors = sset.split(",")
        # print(colors)
        red = [re.findall(r"\d+", color) for color in colors if "red" in color] or [[0]]
        green = [re.findall(r"\d+", color) for color in colors if "green" in color] or [
            [0]
        ]
        blue = [re.findall(r"\d+", color) for color in colors if "blue" in color] or [
            [0]
        ]

        reds.append(int(red[0][0]))
        greens.append(int(green[0][0]))
        blues.append(int(blue[0][0]))

    # print(reds, greens, blues)
    games.append(max(reds) * max(greens) * max(blues))


# print(games)
print(sum(games))
