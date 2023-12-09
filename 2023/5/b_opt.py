import re
import copy
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


seeds_line = lines[0].split(":")[1].split()
seeds = []
for i in range(0, len(seeds_line), 2):
    seeds.append((int(seeds_line[i]), int(seeds_line[i]) + int(seeds_line[i + 1]) - 1))

print(seeds)

seed_to_soil = process(lines[1].split("\n")[1:])
soil_to_fertilizer = process(lines[2].split("\n")[1:])
fertilizer_to_water = process(lines[3].split("\n")[1:])
water_to_light = process(lines[4].split("\n")[1:])
light_to_temp = process(lines[5].split("\n")[1:])
temp_to_hum = process(lines[6].split("\n")[1:])
hum_to_location = process(lines[7].split("\n")[1:])

# print(seed_to_soil)
next_map = {}


def process(seed, mapping):
    # print(seed)

    for entry in mapping:
        # print(entry)
        start = entry[1]
        end = entry[1] + entry[2] - 1
        diff = entry[0] - entry[1]

        if seed[0] > end:
            # print("no match")
            continue

        elif start > seed[1]:
            # print("no match")
            continue

        elif start < seed[0] <= end:
            # print("cond 1")
            next_map[(seed[0], end)] = (seed[0] + diff, end + diff)
            if next_map.get((seed[0], seed[1])) == -1:
                del next_map[(seed[0], seed[1])]
            next_map[(end + 1, seed[1])] = -1
            process((end + 1, seed[1]), mapping)

        elif start <= seed[1] < end:
            # print("cond 2")
            next_map[(start, seed[1])] = (start + diff, seed[1] + diff)
            if next_map.get((seed[0], seed[1])) == -1:
                del next_map[(seed[0], seed[1])]
            next_map[(seed[0], start - 1)] = -1
            process((seed[0], start - 1), mapping)

        elif start >= seed[0] and end <= seed[1]:
            # print("cond 3")
            next_map[(start, end)] = (start + diff, end + diff)
            if next_map.get((seed[0], seed[1])) == -1:
                del next_map[(seed[0], seed[1])]
            next_map[(seed[0], start - 1)] = -1
            process((seed[0], start - 1), mapping)
            next_map[(end + 1, seed[1])] = -1
            process((end + 1, seed[1]), mapping)

        # print(next_map)


next_map = {}
for seed in seeds:
    process(seed, seed_to_soil)
    print(next_map)


# locations = []
# for k, v in seed_dict.items():
#     locations.append(v["location"])

# print(min(locations))
# print(seed_dict)
print(f"Time taken: {time.time() - start_time}")
