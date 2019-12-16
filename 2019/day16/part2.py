file = open('input.txt', 'r')

code = []
howManyPhases = 1
pattern = [0, 1, 0, -1]

for line in file:
    for digit in line:
        code.append(int(digit.rstrip()))

skip = 0
for n in code[0:7]:
    skip = skip * 10 + n

code = code * 10000
part2Code = code[skip:]
length = len(part2Code)

for phase in range(100):
    for i in range(length - 2, -1, -1):
        part2Code[i] = (part2Code[i + 1] + part2Code[i]) % 10

for i in part2Code[:8]:
    print(i,end="")
print("")