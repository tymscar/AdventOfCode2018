file = open('input.txt', 'r')

code = []
codelength = 0
howManyPhases = 100
pattern = [0, 1, 0, -1]

for line in file:
    for digit in line:
        code.append(int(digit.rstrip()))
    codelength = len(code)

def getPatDigit(repeat, digit):
    global pattern
    return pattern[(digit//(repeat+1)) % len(pattern)]


for phase in range(0,howManyPhases):
    output = []
    for outputDigitPos in range(0,codelength):
        outputDigit = 0
        for digitPos in range(0,codelength):
            outputDigit += (code[digitPos] * getPatDigit(outputDigitPos,digitPos+1))
        output.append((abs(outputDigit)%10))

    code = output

for i in range(0,8):
    print(code[i],end="")
print("")