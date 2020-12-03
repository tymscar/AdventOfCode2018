def part_2():
    file = open('input.txt', 'r')
    minimap = [line for line in file]

    width = len(minimap[0]) - 1
    slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]

    answer = 1

    for slope in slopes:
        trees = 0
        pos = [0, 0]
        while pos[0] < len(minimap):
            if minimap[pos[0]][pos[1]] == "#":
                trees += 1
            pos[0] += slope[0]
            pos[1] += slope[1]
            pos[1] = pos[1] % width
        answer *= trees



    return answer

print(part_2())