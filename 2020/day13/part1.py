def part_1():
    file = open('input.txt', 'r')

    for line in file:
        line = line.strip("\n")
        print(line)


    return "Done"

print(part_1())
