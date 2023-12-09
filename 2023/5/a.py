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

seed_dict = {int(seed): {} for seed in seeds}

# print(seed_to_soil)
# for entry in seed_to_soil:
#     for i in range(entry[1], entry[1] + entry[2]):
#         try:
#             seed_dict[i]["soil"] = entry[0] + i - entry[1]
#         except KeyError:
#             continue

# for k, v in seed_dict.items():
#     if v.get("soil") == None:
#         v["soil"] = k

for seed in seed_dict.keys():
    for entry in seed_to_soil:
        if entry[1] <= seed < entry[1] + entry[2]:
            seed_dict[seed]["soil"] = entry[0] + seed - entry[1]

for k, v in seed_dict.items():
    if v.get("soil") == None:
        v["soil"] = k

# # print(soil_to_fertilizer)
# for entry in soil_to_fertilizer:
#     for i in range(entry[1], entry[1] + entry[2]):
#         for k, v in seed_dict.items():
#             if i == v["soil"]:
#                 try:
#                     seed_dict[k]["fertilizer"] = entry[0] + i - entry[1]
#                 except KeyError:
#                     continue

# for k, v in seed_dict.items():
#     if v.get("fertilizer") == None:
#         v["fertilizer"] = v["soil"]

# # print(fertilizer_to_water)
# for entry in fertilizer_to_water:
#     for i in range(entry[1], entry[1] + entry[2]):
#         for k, v in seed_dict.items():
#             if i == v["fertilizer"]:
#                 try:
#                     seed_dict[k]["water"] = entry[0] + i - entry[1]
#                 except KeyError:
#                     continue

# for k, v in seed_dict.items():
#     if v.get("water") == None:
#         v["water"] = v["fertilizer"]

# # print(water_to_light)
# for entry in water_to_light:
#     for i in range(entry[1], entry[1] + entry[2]):
#         for k, v in seed_dict.items():
#             if i == v["water"]:
#                 try:
#                     seed_dict[k]["light"] = entry[0] + i - entry[1]
#                 except KeyError:
#                     continue

# for k, v in seed_dict.items():
#     if v.get("light") == None:
#         v["light"] = v["water"]

# # print(light_to_temp)
# for entry in light_to_temp:
#     for i in range(entry[1], entry[1] + entry[2]):
#         for k, v in seed_dict.items():
#             if i == v["light"]:
#                 try:
#                     seed_dict[k]["temp"] = entry[0] + i - entry[1]
#                 except KeyError:
#                     continue

# for k, v in seed_dict.items():
#     if v.get("temp") == None:
#         v["temp"] = v["light"]

# # print(temp_to_hum)
# for entry in temp_to_hum:
#     for i in range(entry[1], entry[1] + entry[2]):
#         for k, v in seed_dict.items():
#             if i == v["temp"]:
#                 try:
#                     seed_dict[k]["hum"] = entry[0] + i - entry[1]
#                 except KeyError:
#                     continue

# for k, v in seed_dict.items():
#     if v.get("hum") == None:
#         v["hum"] = v["temp"]

# # print(hum_to_location)
# for entry in hum_to_location:
#     for i in range(entry[1], entry[1] + entry[2]):
#         for k, v in seed_dict.items():
#             if i == v["hum"]:
#                 try:
#                     seed_dict[k]["location"] = entry[0] + i - entry[1]
#                 except KeyError:
#                     continue

# for k, v in seed_dict.items():
#     if v.get("location") == None:
#         v["location"] = v["hum"]

# locations = []
# for k, v in seed_dict.items():
#     locations.append(v["location"])

# print(min(locations))
print(seed_dict)
print(f"Time taken: {time.time() - start_time}")
