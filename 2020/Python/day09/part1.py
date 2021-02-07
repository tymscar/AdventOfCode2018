def two_num_sum(arr, start, end, find):
    for i in range(start, end + 1):
        complement = find - arr[i]
        if complement != arr[i] and complement in arr[start:end + 1]:
            return True
    return False


def part_1():
    file = open('input.txt', 'r')

    XMAS = []

    for line in file:
        line = line.strip("\n")
        XMAS.append(int(line))

    for i in range(25, len(XMAS)):
        if not two_num_sum(XMAS, i - 25, i - 1, XMAS[i]):
            return XMAS[i]

    return "All codes are sadly fine"


print(part_1())