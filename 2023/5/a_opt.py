import re
import time
import pathlib

input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
print(input_path)

with open(input_path) as f:
    # lines = [line.strip() for line in f.readlines()]
    lines = f.read().split("\n\n")

# print(lines)

start_time = time.time()


def process(entries):
    ret = []
    for entry in entries:
        ret.append(list(map(int, entry.split())))

    return ret


seeds = lines[0].split(":")[1].split()
seed_to_soil = process(lines[1].split("\n")[1:])
soil_to_fertilizer = process(lines[2].split("\n")[1:])
fertilizer_to_water = process(lines[3].split("\n")[1:])
water_to_light = process(lines[4].split("\n")[1:])
light_to_temp = process(lines[5].split("\n")[1:])
temp_to_hum = process(lines[6].split("\n")[1:])
hum_to_location = process(lines[7].split("\n")[1:])

# print(seed_to_soil)

seed_dict = {int(seed): {} for seed in seeds}

for seed in seed_dict.keys():
    for entry in seed_to_soil:
        if entry[1] <= seed < entry[1] + entry[2]:
            seed_dict[seed]["soil"] = entry[0] + seed - entry[1]

for k, v in seed_dict.items():
    if v.get("soil") == None:
        v["soil"] = k


def run(mapping, map_from, map_to):
    for seed in seed_dict.keys():
        for entry in mapping:
            if entry[1] <= seed_dict[seed][map_from] < entry[1] + entry[2]:
                seed_dict[seed][map_to] = (
                    entry[0] + seed_dict[seed][map_from] - entry[1]
                )

    for k, v in seed_dict.items():
        if v.get(map_to) == None:
            v[map_to] = v[map_from]


run(soil_to_fertilizer, "soil", "fertilizer")
run(fertilizer_to_water, "fertilizer", "water")
run(water_to_light, "water", "light")
run(light_to_temp, "light", "temp")
run(temp_to_hum, "temp", "hum")
run(hum_to_location, "hum", "location")


locations = []
for k, v in seed_dict.items():
    locations.append(v["location"])

print(min(locations))
# print(seed_dict)
print(f"Time taken: {time.time() - start_time}")
