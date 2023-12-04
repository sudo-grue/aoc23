#!/usr/bin/env python3


def main():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]
        counts = [1] * len(data)

    for idx, line in enumerate(data):
        card, game = line.split(":")
        winning, numbers = game.split("|")
        winning = set(map(int, winning.split()))
        numbers = set(map(int, numbers.split()))

        data[idx] = len(winning.intersection(numbers))

        for num in range(1, data[idx] + 1):
            counts[idx + num] += (counts[idx])

    print(sum(counts))

if __name__ == '__main__':
    main()
