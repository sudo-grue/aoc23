#!/usr/bin/env python3

from sys import argv

class Seed_Bag:
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __contains__(self, item):
        return self.start <= item < (self.start + self.step)

    def __str__(self):
        return f"[{self.start}, {self.start + self.step})"


class Converter:
    def __init__(self, dst, src, steps):
        self.dst = dst
        self.src = src
        self.steps = steps

    def convert(self, in_val):
        if self.src <= in_val < (self.src + self.steps):
            return in_val + (self.dst - self.src)
        raise ValueError

    def reverse(self, in_val):
        if self.dst <= in_val < (self.dst + self.steps):
            return in_val + (self.src - self.dst)
        raise ValueError

    def __str__(self):
        return f"[{self.dst}, {self.dst + self.steps}) -> [{self.src}, {self.src + self.steps})"

def main():
    data = []
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    idx = 0
    _, seeds = data[idx].split(": ")
    seeds = list(map(int, seeds.split()))
    idx += 3

    machines = []

    for _ in range(6):
        machine_category = []
        machines.append(machine_category)
        while data[idx] != "":
            machine_category.append(Converter(*map(int, data[idx].split())))
            idx += 1
        idx += 2

    humid_to_loc = []
    machines.append(humid_to_loc)
    for line in data[idx:]:
        humid_to_loc.append(Converter(*map(int, line.split())))

    machines.reverse()

    temp = []
    for idx in range(0, len(seeds), 2):
        start = seeds[idx]
        steps = seeds[idx + 1]
        temp.append(Seed_Bag(start, steps))

    seeds = temp

    curr_state = int(argv[1]) * 1000000
    end = curr_state + 1000000

    found = False
    while not found and curr_state < end:
        curr = curr_state
        for machine_type in machines:
            for machine in machine_type:
                try:
                    curr = machine.reverse(curr)
                    break
                except ValueError:
                    pass

        for bag in seeds:
            if curr in bag:
                found = True
                print(curr_state)
                break

        curr_state += 1


if __name__ == '__main__':
    main()
