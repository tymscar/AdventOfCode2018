from collections import defaultdict

file = open('input.txt', 'r')

parents = defaultdict(str)

for line in file:
    inpt = line.split(')')
    inpt[1] = inpt[1].rstrip()
    parents[inpt[1]] = inpt[0]

total = 0

for moon in parents:
    currmoon = moon
    howMany = 0
    while parents[currmoon] != "COM":
        howMany += 1
        currmoon = parents[currmoon]
    total += howMany + 1

print(total)
