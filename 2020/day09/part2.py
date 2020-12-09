def two_num_sum(arr, start, end, find):
    for i in range(start, end + 1):
        complement = find - arr[i]
        if complement != arr[i] and complement in arr[start:end + 1]:
            return True
    return False


def find_bad_num_index(arr):
    file = open('input.txt', 'r')

    for line in file:
        line = line.strip("\n")
        arr.append(int(line))

    for i in range(25, len(arr)):
        if not two_num_sum(arr, i - 25, i - 1, arr[i]):
            return i


def find_range_that_adds_up_to(what, arr, end):
    for i in range(end + 1):
        curr_sum = arr[i]
        for j in range(i + 1, end + 1):
            curr_sum += arr[j]
            if curr_sum == what:
                return i, j


def part_2():
    XMAS = []
    idx_bad_num = find_bad_num_index(XMAS)

    range_to_check = find_range_that_adds_up_to(XMAS[idx_bad_num], XMAS, idx_bad_num)

    min_in_range = min(XMAS[range_to_check[0]:range_to_check[1]+1])
    max_in_range = max(XMAS[range_to_check[0]:range_to_check[1]+1])

    return min_in_range + max_in_range


print(part_2())
