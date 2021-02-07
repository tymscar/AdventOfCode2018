from functools import reduce

def valid_answer(n, mod, answer):
    return (n+answer)%mod == 0

# Source: https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/helpers.py
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Source: https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/helpers.py
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part_2():
    file = open('input.txt', 'r')

    busses = []
    offsets = []


    file.readline()
    timetable = [bus for bus in file.readline().split(sep=",")]

    for i in range(len(timetable)):
        if timetable[i] != "x":
            busses.append(int(timetable[i]))
            offsets.append(int(timetable[i]) - i)

    return chinese_remainder(busses, offsets)

print(part_2())
