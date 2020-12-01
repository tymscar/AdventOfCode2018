def product_of_two_numbers_that_sum_to(list_of_numbers, value_they_have_to_sum_to, how_many_numbers_to_sum):
    if how_many_numbers_to_sum == 0:
        return 1
    if how_many_numbers_to_sum == 1:
        if value_they_have_to_sum_to in list_of_numbers:
            return value_they_have_to_sum_to
        else:
            return 0


    for number in list_of_numbers:
        complement = value_they_have_to_sum_to - number
        product = product_of_two_numbers_that_sum_to(list_of_numbers, complement, how_many_numbers_to_sum - 1)
        if product > 0:
            return number * product
    return 0


def part_2():
    file = open('input.txt', 'r')

    expenses = {}

    for line in file:
        expenses[int(line)] = True

    return product_of_two_numbers_that_sum_to(expenses, 2020, 3)


print(part_2())