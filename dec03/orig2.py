#!/usr/bin/env python3

def has_digit(data):
    return any(char.isdigit() for char in data)

def main():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    total = 0
    for row, line in enumerate(data):
        for col, point in enumerate(line):
            if point == "*":
                nums = []
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
                for num in (int(val) for val in substring.split('.') if val):
                    nums.append(num)

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
                substring = substring.replace(point, ".")
                for num in (int(val) for val in substring.split('.') if val):
                    nums.append(num)

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
                for num in (int(val) for val in substring.split('.') if val):
                    nums.append(num)

                if len(nums) == 2:
                    total += nums[0] * nums[1]

    print(total)

if __name__ == '__main__':
    main()

