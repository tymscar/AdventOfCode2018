def part_1():
    file = open('input.txt', 'r')

    for lineWithOptionNewLine in file:
        line = lineWithOptionNewLine.strip('\n')
        print(line)


print(part_1())