#!/usr/bin/env python3

def main():
    with open("input.txt", "r") as f:
        data = [line.strip() for line in f.readlines()]

    symbols = {tgt for line in data for tgt in line if not tgt.isdigit()}
    symbols.remove(".")

    total = 0
    for row, line in enumerate(data):
        for col, point in enumerate(line):

            if point in symbols:
                total += sum(get_adj_nums(data[row - 1], col))
                total += sum(get_adj_nums(data[row].replace(point, "."), col))
                total += sum(get_adj_nums(data[row + 1], col))

    print(total)


def has_digit(data):
    return any(char.isdigit() for char in data)


def get_adj_nums(string, start):
    llimit = start - 1
    rlimit = start + 2

    result = []
    if has_digit(string[llimit: rlimit]):
        while 0 < llimit and string[llimit] != ".":
            llimit -= 1
        while rlimit < len(string) and string[rlimit - 1] != ".":
            rlimit += 1

        result = [int(num) for num in string[llimit: rlimit].split(".") if num]

    return result


if __name__ == '__main__':
    main()
