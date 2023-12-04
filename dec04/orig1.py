#!/usr/bin/env python3

def main():
    data = []
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    score = 0
    for line in data:
        card, game = line.split(":")
        winning, numbers = game.split("|")
        winning = set(map(int, winning.split()))
        numbers = set(map(int, numbers.split()))

        factor = len(winning.intersection(numbers))
        score += 1 << (factor - 1) if factor else 0

    print(score)


if __name__ == '__main__':
    main()
