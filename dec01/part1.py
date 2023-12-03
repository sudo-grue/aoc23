#!/usr/bin/env python3
def main():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    total = 0
    for line in data:
        line_len = len(line)

        nums = []
        for idx in range(line_len):
            if line[idx].isdigit():
                nums.append(int(line[idx]))

        total += int(f"{nums[0]}{nums[-1]}")

    print(total)
    


if __name__ == '__main__':
    main()

