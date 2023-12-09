next_map = {}


def process(seed, mapping):
    print(seed)

    for entry in mapping:
        print(entry)
        start = entry[1]
        end = entry[1] + entry[2]
        diff = entry[0] - entry[1]

        if seed[0] >= end:
            print("cond 1")
            print("no match")
            next_map[(seed[0], seed[1])] = -1

        elif start <= seed[0] < end:
            if seed[0] < end < seed[1]:
                print("cond 2")
                next_map[(seed[0], end)] = (seed[0] + diff, end + diff)
                if next_map.get((seed[0], seed[1])) == -1:
                    del next_map[(seed[0], seed[1])]
                next_map[(end, seed[1])] = -1
                process((end, seed[1]), mapping)

            elif end >= seed[1]:
                print("cond 3")
                next_map[(seed[0], seed[1])] = (seed[0] + diff, seed[1] + diff)
                if next_map.get((seed[0], seed[1])) == -1:
                    del next_map[(seed[0], seed[1])]

        elif seed[0] < start < seed[1]:
            if seed[0] < end < seed[1]:
                print("cond 4")
                next_map[(start, end)] = (start + diff, end + diff)
                if next_map.get((seed[0], seed[1])) == -1:
                    del next_map[(seed[0], seed[1])]
                next_map[(seed[0], start - 1)] = -1
                process((seed[0], start - 1), mapping)
                next_map[(end, seed[1])] = -1
                process((end, seed[1]), mapping)

            if end >= seed[1]:
                print("cond 5")
                next_map[(start, seed[1])] = (start + diff, seed[1] + diff)
                if next_map.get((seed[0], seed[1])) == -1:
                    del next_map[(seed[0], seed[1])]
                next_map[(seed[0], start)] = -1
                process((seed[0], start), mapping)

        elif start >= seed[1]:
            print("cond 6")
            print("no match")
            next_map[(seed[0], seed[1])] = -1

        print(next_map)


# seed = (79, 79 + 14)

# seed_to_soil = [(50, 98, 2), (52, 50, 48)]
# seed_to_soil = [(55, 50, 36), (95, 90, 6)]

# # only left
# seed_to_soil = [(55, 50, 29)]
# # left full cover and 1 overlap
# seed_to_soil = [(55, 50, 30)]
# # left full cover and some overlap
# seed_to_soil = [(55, 50, 34)]
# # left full cover and -1 overlap
# seed_to_soil = [(55, 50, 42)]
# # left full cover and full overlap
# seed_to_soil = [(55, 50, 43)]
# # full cover
# seed_to_soil = [(55, 50, 45)]
# # full cover
# seed_to_soil = [(55, 78, 45)]
# # full cover
# seed_to_soil = [(55, 79, 45)]
# # right full cover -1 overlap
# seed_to_soil = [(55, 80, 45)]
# # right full cover some overlap
# seed_to_soil = [(55, 82, 45)]
# # right full cover 1 overlap
# seed_to_soil = [(55, 92, 45)]
# # no overlap
# seed_to_soil = [(55, 93, 45)]
# # no overlap
# seed_to_soil = [(55, 99, 45)]

# process(seed, seed_to_soil)

next_map = {}
seeds = [(79, 79 + 14), (55, 55 + 13), (95, 95 + 10)]
seed_to_soil = [(50, 98, 2), (52, 50, 48)]

for seed in seeds:
    process(seed, seed_to_soil)
    print(next_map)
