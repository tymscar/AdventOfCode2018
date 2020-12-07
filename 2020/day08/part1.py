def part_1():
    file = open('input.txt', 'r')

    for line in file:
        print(line.strip("\n"))


    return "done"


print(part_1())