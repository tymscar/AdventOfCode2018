def part_1():
    file = open('input.txt', 'r')
    minimap = [line for line in file]

    width = len(minimap[0]) - 1
    pos = [0,0]
    slope = [1,3]

    trees = 0

    while pos[0] < len(minimap):
        if minimap[pos[0]][pos[1]] == "#":
            trees += 1
        pos[0] += slope[0]
        pos[1] += slope[1]
        pos[1] = pos[1] % width




    return trees

print(part_1())