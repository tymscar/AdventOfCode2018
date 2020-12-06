def part_1():
    file = open('input.txt', 'r')

    for lineWithOptionNewLine in file:
        if lineWithOptionNewLine == "\n":
            line = lineWithOptionNewLine.strip('\n')

            print(line)

    return 0


print(part_1())