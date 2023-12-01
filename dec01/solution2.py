#!/usr/bin/env python3
def main():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    total = 0
    for line in data:
        line_len = len(line)
        line_nums = []
        for idx in range(line_len):
            if line[idx].isdigit():
                line_nums.append(int(line[idx]))

            for num in nums.keys():
                if line.startswith(num, idx):
                    line_nums.append(nums[num])

        total += int(f"{line_nums[0]}{line_nums[-1]}")
    print(total)
    


if __name__ == '__main__':
    main()

