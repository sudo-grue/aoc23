#!/usr/bin/env python3
def main():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    total = 0
    for line in data:
        for idx in range(len(line)):
            num1 = 0
            num2 = 0
            if line[idx].isdigit():
                num1 = int(line[idx])
            for num in nums.keys():
                if line[idx:].startswith(num):
                    num1 = nums[num]
            if num1 != 0:
                break
        for idx in range(len(line) - 1, -1, -1):
            if line[idx].isdigit():
                num2 = int(line[idx])
            for num in nums.keys():
                if line.endswith(num, 0, idx + 1):
                    num2 = nums[num]
            if num2 != 0:
                break
        print(f"{line} = {num1}{num2}")
        total += int(f"{num1}{num2}")
    print(total)
    


if __name__ == '__main__':
    main()

