from collections import defaultdict


def part_1():
    file = open('input.txt', 'r')

    letters = defaultdict(lambda: 0)
    valid_passwords = 0

    for line in file:

        spl = line.split()
        range_split = spl[0].split(sep="-")
        letter = spl[1][0]
        range_for_letter = (int(range_split[0]) + letters[letter], int(range_split[1]) + letters[letter])
        password = spl[2]

        for char in password:
            if char == letter:
                letters[letter] += 1

        if letters[letter] >= range_for_letter[0] and letters[letter] <= range_for_letter[1]:
            valid_passwords += 1

    return valid_passwords

print(part_1())