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
        limits = {"red": 12, "green": 13, "blue": 14}
        print(game)
        for subgame in game.split("; "):
            for chunk in subgame.split(","):
                num, color = chunk.split()
                if limits[color] < int(num):
                    limits[color] = int(num)
        if limits["red"] <= 12 and limits["green"] <= 13 and limits["blue"] <= 14:
            print(f"\tSUCCESS: {limits}")
            total += game_id

    print(total)


if __name__ == '__main__':
    main()

