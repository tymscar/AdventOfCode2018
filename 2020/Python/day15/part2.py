def part_2():
    last_spoken = {}
    pos = 1
    next_num = 0

    file = open('input.txt', 'r')
    inp = file.readline().strip("\n").split(',')

    for num in inp:
        last_spoken[int(num)] = pos
        pos += 1

    while pos <= 30000000:
        current_num = next_num
        if current_num in last_spoken:
            next_num = pos - last_spoken[current_num]
        else:
            next_num = 0
        last_spoken[current_num] = pos
        pos +=1

    return current_num


print(part_2())