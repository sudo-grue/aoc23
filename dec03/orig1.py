#!/usr/bin/env python3

def has_digit(data):
    return any(char.isdigit() for char in data)


def main():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    total = 0
    symbols = set(["/", "*", "#", "$", "@", "%", "&", "*", "-", "+", "="])
    for row, line in enumerate(data):
        for col, point in enumerate(line):

            # we found a valid starting point
            if point in symbols:

                # row above symbol
                # setup and extend left/right slicing until we know we have full number
                mod1 = 1
                mod2 = 2
                substring = data[row - 1][col - mod1: col + mod2]
                if has_digit(substring):
                    while 0 < (col - mod1) and not substring.startswith('.'):
                        mod1 += 1
                        substring = data[row - 1][col - mod1: col + mod2]
                    while (col + mod2) < len(line) and substring[-1] != ".":
                        mod2 += 1
                        substring = data[row - 1][col - mod1: col + mod2]
                total += sum(int(val) for val in substring.split('.') if val)


                # row with symbol
                mod1 = 1
                mod2 = 2
                substring = data[row][col - mod1: col + mod2]
                if has_digit(substring):
                    while 0 < (col - mod1) and not substring.startswith('.'):
                        mod1 += 1
                        substring = data[row][col - mod1: col + mod2]
                    while (col + mod2) < len(line) and substring[-1] != ".":
                        mod2 += 1
                        substring = data[row][col - mod1: col + mod2]

                # replace the special character to allow normal handling
                substring = substring.replace(point, ".")
                total += sum(int(val) for val in substring.split('.') if val)


                # row below symbol
                mod1 = 1
                mod2 = 2
                substring = data[row + 1][col - mod1: col + mod2]
                if has_digit(substring):
                    while 0 < (col - mod1) and not substring.startswith('.'):
                        mod1 += 1
                        substring = data[row + 1][col - mod1: col + mod2]
                    while (col + mod2) < len(line) and substring[-1] != ".":
                        mod2 += 1
                        substring = data[row + 1][col - mod1: col + mod2]
                total += sum(int(val) for val in substring.split('.') if val)


    print(total)

if __name__ == '__main__':
    main()

