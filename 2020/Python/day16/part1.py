def part_1():
    file = open('input.txt', 'r')
    good_ranges = []

    for line in file:
        line = line.strip('\n')
        if line == "":
            break
        ranges = line.split(":")[1].split(" or ")
        good_ranges.append([int(ranges[0].split("-")[0]),int(ranges[0].split("-")[1])])
        good_ranges.append([int(ranges[1].split("-")[0]),int(ranges[1].split("-")[1])])

    file.readline()
    file.readline()
    file.readline()
    file.readline()

    invalid_sum = 0

    for line in file:
        line = line.strip('\n')
        for val_string in line.split(","):
            val = int(val_string)
            bad_val = True
            for range in good_ranges:
                if val >= range[0] and val <= range[1]:
                    bad_val = False
                    break
            if bad_val:
                invalid_sum += val

    return invalid_sum

print(part_1())