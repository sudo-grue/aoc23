#!/usr/bin/env python3

def main():
    data = []
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    idx = 0
    _, seeds = data[idx].split(": ")
    seeds = list(map(int, seeds.split()))
    idx += 3
    print(seeds)

    seed_to_soil = []
    while data[idx] != "":
        seed_to_soil.append(list(map(int, data[idx].split())))
        idx += 1
    idx += 2

    for i, entry in enumerate(seed_to_soil):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        seed_to_soil[i] = [src_map, dst_map]

    soil_to_fert = []
    while data[idx] != "":
        soil_to_fert.append(list(map(int, data[idx].split())))
        idx += 1
    idx += 2

    for i, entry in enumerate(soil_to_fert):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        soil_to_fert[i] = [src_map, dst_map]

    fert_to_water = []
    while data[idx] != "":
        fert_to_water.append(list(map(int, data[idx].split())))
        idx += 1
    idx += 2

    for i, entry in enumerate(fert_to_water):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        fert_to_water[i] = [src_map, dst_map]

    water_to_light = []
    while data[idx] != "":
        water_to_light.append(list(map(int, data[idx].split())))
        idx += 1
    idx += 2

    for i, entry in enumerate(water_to_light):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        water_to_light[i] = [src_map, dst_map]

    light_to_temp = []
    while data[idx] != "":
        light_to_temp.append(list(map(int, data[idx].split())))
        idx += 1
    idx += 2

    for i, entry in enumerate(light_to_temp):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        light_to_temp[i] = [src_map, dst_map]

    temp_to_humid = []
    while data[idx] != "":
        temp_to_humid.append(list(map(int, data[idx].split())))
        idx += 1
    idx += 2

    for i, entry in enumerate(temp_to_humid):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        temp_to_humid[i] = [src_map, dst_map]

    humid_to_loc = []
    for line in data[idx:]:
        humid_to_loc.append(list(map(int, line.split())))
    print(humid_to_loc)

    for i, entry in enumerate(humid_to_loc):
        src_map = list(range(entry[1], entry[1] + entry[2]))
        dst_map = list(range(entry[0], entry[0] + entry[2]))
        humid_to_loc[i] = [src_map, dst_map]

    print(humid_to_loc)

    locs = []
    for curr in seeds:
        for seed, soil in seed_to_soil:
            if curr in seed:
                curr = soil[seed.index(curr)]
                break

        for soil, fert in soil_to_fert:
            if curr in soil:
                curr = fert[soil.index(curr)]
                break

        for fert, water in fert_to_water:
            if curr in fert:
                curr = water[fert.index(curr)]
                break

        for water, light in water_to_light:
            if curr in water:
                curr = light[water.index(curr)]
                break

        for light, temp in light_to_temp:
            if curr in light:
                curr = temp[light.index(curr)]
                break

        for temp, humid in temp_to_humid:
            if curr in temp:
                curr = humid[temp.index(curr)]
                break

        for humid, loc in humid_to_loc:
            if curr in humid:
                curr = loc[humid.index(curr)]
                break

        locs.append(curr)

    print(seeds)
    print(locs)

if __name__ == '__main__':
    main()
