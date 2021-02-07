def part_1():
    file = open('input.txt', 'r')
    jolts = [0]
    highest = 0

    one_jumps = 0
    three_jumps = 0

    for line in file:
        line = line.strip("\n")
        jolts.append(int(line))
        highest = max(highest, int(line))
    
    jolts.append(highest + 3)
    
    jolts = sorted(jolts)

    for i in range(len(jolts)-1):
        if jolts[i+1] - jolts[i] == 1:
            one_jumps += 1
        else:
            three_jumps += 1

    return one_jumps * three_jumps


print(part_1())