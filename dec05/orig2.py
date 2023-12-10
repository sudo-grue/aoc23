#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as f:
        raw_seeds, *chunks = f.read().split("\n\n")

    seeds = raw_seeds.split(":")[1]  # extract number portion of string
    seeds = list(map(int, seeds.split()))  # convert string to list(ints)
    seed_ranges = [range(seeds[idx], seeds[idx] + seeds[idx + 1]) for idx in range(0, len(seeds), 2)]

    chunks.reverse()

    for idx, chunk in enumerate(chunks):
        chunks[idx] = [tuple(map(int, sieve.split())) for sieve in chunk.strip().split("\n")[1:]]


    loc = -1
    found = False
    while not found:
        loc += 1
        if (loc % 1000000 == 0):
            print(f"{loc = }")
        seed = loc
        for chunk in chunks:
            for dst, src, step in chunk:
                if dst <= seed < (dst + step):
                    seed += src - dst
                    break

        for seed_range in seed_ranges:    
            if seed in seed_range:
                found = True
                break

    print(loc)

if __name__ == '__main__':
    main()
