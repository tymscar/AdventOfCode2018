def part_1():
    file = open('input.txt', 'r')

    for lineWithOptionNewLine in file:
        if lineWithOptionNewLine == "\n":
            pass
        else:
            line = lineWithOptionNewLine.strip('\n')

    return 0


print(part_1())