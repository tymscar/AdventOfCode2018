def part_1():
    file = open('input.txt', 'r')

    nums = {}

    for line in file:
        nums[int(line)] = True

    for num in nums:
        complement = 2020 - num
        if complement in nums:
            return num * complement


print(part_1())