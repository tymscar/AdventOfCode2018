import math

file = open('input.txt', 'r')

for line in file:
    memory = line.split(',')

prgInput = 1
prgOutput = 0

instructionRead = 0
pc = 0


while True:
    instructionRead = int(memory[pc])

    jumped = False
    opcode = instructionRead % 100
    modes = int(instructionRead/100)

    if int(opcode) == 99:
        break

    length = 0

    if int(opcode) == 1:
        length = 4
        paramOne = int(memory[pc + 1])
        paramTwo = int(memory[pc + 2])
        operandOne = 0
        operandTwo = 0
        if modes % 10 == 0:
            operandOne = int(memory[paramOne])
        else:
            operandOne = paramOne

        if int((modes % 100)/10) == 0:
            operandTwo = int(memory[paramTwo])
        else:
            operandTwo = paramTwo

        memory[int(memory[pc + 3])] = operandOne + operandTwo
    if int(opcode) == 2:
        length = 4
        paramOne = int(memory[pc + 1])
        paramTwo = int(memory[pc + 2])
        operandOne = 0
        operandTwo = 0
        if modes % 10 == 0:
            operandOne = int(memory[paramOne])
        else:
            operandOne = paramOne

        if int((modes % 100) / 10) == 0:
            operandTwo = int(memory[paramTwo])
        else:
            operandTwo = paramTwo

        memory[int(memory[pc + 3])] = operandOne * operandTwo

    if int(opcode) == 3:
        length = 2
        paramOne = int(memory[pc + 1])
        memory[paramOne] = prgInput

    if int(opcode) == 4:
        length = 2
        paramOne = int(memory[pc + 1])
        prgOutput = memory[paramOne]
    pc = pc + length
    instructionRead = int(memory[pc])

print(prgOutput)
