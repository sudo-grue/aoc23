#!/usr/bin/env python3

class Converter:
    def __init__(self, dst, src, steps):
        self.dst = dst
        self.src = src
        self.steps = steps

    def convert(self, in_val):
        if self.src <= in_val < self.src + self.steps:
            return in_val + (self.dst - self.src)
        raise ValueError

def main():
    data = []
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    idx = 0
    _, seeds = data[idx].split(": ")
    seeds = list(map(int, seeds.split()))
    idx += 3

    seed_to_soil = []
    while data[idx] != "":
        seed_to_soil.append(Converter(*map(int, data[idx].split())))
        idx += 1
    idx += 2

    soil_to_fert = []
    while data[idx] != "":
        soil_to_fert.append(Converter(*map(int, data[idx].split())))
        idx += 1
    idx += 2

    fert_to_water = []
    while data[idx] != "":
        fert_to_water.append(Converter(*map(int, data[idx].split())))
        idx += 1
    idx += 2

    water_to_light = []
    while data[idx] != "":
        water_to_light.append(Converter(*map(int, data[idx].split())))
        idx += 1
    idx += 2

    light_to_temp = []
    while data[idx] != "":
        light_to_temp.append(Converter(*map(int, data[idx].split())))
        idx += 1
    idx += 2

    temp_to_humid = []
    while data[idx] != "":
        temp_to_humid.append(Converter(*map(int, data[idx].split())))
        idx += 1
    idx += 2

    humid_to_loc = []
    for line in data[idx:]:
        humid_to_loc.append(Converter(*map(int, line.split())))


    locs = []
    for curr in seeds:
        for machine in seed_to_soil:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        for machine in soil_to_fert:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        for machine in fert_to_water:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        for machine in water_to_light:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        for machine in light_to_temp:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        for machine in temp_to_humid:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        for machine in humid_to_loc:
            try:
                curr = machine.convert(curr)
                break
            except ValueError:
                pass

        locs.append(curr)

    print(seeds)
    print(locs)

    print(min(locs))

if __name__ == '__main__':
    main()
