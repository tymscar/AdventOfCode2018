def part_2():
    file = open('input.txt', 'r')

    valid_passwords = 0

    for line in file:

        spl = line.split()
        range_split = spl[0].split(sep="-")
        letter = spl[1][0]
        positions = (int(range_split[0]) - 1, int(range_split[1]) - 1)
        password = spl[2]

        appearances = 0
        if password[positions[0]] == letter:
            appearances += 1
        if password[positions[1]] == letter:
            appearances += 1

        if appearances == 1:
            valid_passwords += 1


    return valid_passwords

print(part_2())