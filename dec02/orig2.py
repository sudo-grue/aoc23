#!/usr/bin/env python3

def main():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    games = []
    for line in data:
        for game in (line.split(": ")):
            if game.startswith("Game"):
                continue
            games.append(game)

    total = 0
    for game_id, game in enumerate(games, 1):
        limits = {"red": 1, "green": 1, "blue": 1}
        print(game)
        for subgame in game.split("; "):
            for chunk in subgame.split(","):
                num, color = chunk.split()
                if limits[color] < int(num):
                    limits[color] = int(num)
        total += limits["red"] * limits["green"] * limits["blue"]

    print(total)


if __name__ == '__main__':
    main()

