from sympy.utilities.iterables import multiset_permutations

def intcodeVM(programSeq, inpt, inpt2):
    prgInput = inpt
    prgOutput = 0
    instructionRead = 0
    pc = 0
    memory = programSeq

    while True:
        instructionRead = int(memory[pc])
        opcode = instructionRead % 100
        modes = int(instructionRead / 100)

        if int(opcode) == 99:
            break

        jumped = False
        length = 0
        paramOne = 0
        paramTwo = 0
        paramThree = 0
        operandOne = 0
        operandTwo = 0
        operandThree = 0

        if (pc + 1) < len(memory):
            paramOne = int(memory[pc + 1])
        if (pc + 2) < len(memory):
            paramTwo = int(memory[pc + 2])
        if (pc + 3) < len(memory):
            paramThree = int(memory[pc + 3])

        if modes % 10 == 0 and paramOne < len(memory):
            operandOne = int(memory[paramOne])
        else:
            operandOne = paramOne

        if int((modes % 100) / 10) == 0 and paramTwo < len(memory):
            operandTwo = int(memory[paramTwo])
        else:
            operandTwo = paramTwo

        if int(modes / 1000) == 0 and paramThree < len(memory):
            operandThree = int(memory[paramThree])
        else:
            operandThree = paramThree

        if int(opcode) == 1:
            length = 4
            memory[paramThree] = operandOne + operandTwo

        if int(opcode) == 2:
            length = 4
            memory[paramThree] = operandOne * operandTwo

        if int(opcode) == 3:
            length = 2
            memory[paramOne] = prgInput
            prgInput = inpt2

        if int(opcode) == 4:
            length = 2
            prgOutput = operandOne

        if int(opcode) == 5:
            length = 3
            if operandOne != 0:
                pc = operandTwo
                jumped = True

        if int(opcode) == 6:
            length = 3
            if operandOne == 0:
                pc = operandTwo
                jumped = True

        if int(opcode) == 7:
            length = 4
            if operandOne < operandTwo:
                memory[paramThree] = 1
            else:
                memory[paramThree] = 0

        if int(opcode) == 8:
            length = 4
            if operandOne == operandTwo:
                memory[paramThree] = 1
            else:
                memory[paramThree] = 0

        if jumped == False:
            pc = pc + length
            instructionRead = int(memory[pc])

    return prgOutput

file = open('input.txt', 'r')

for line in file:
    origPrg = line.split(',')

phaseSettings = list(multiset_permutations([0,1,2,3,4]))
maxSignal = 0

for phaseSetting in phaseSettings:
    prg = origPrg.copy()
    output = intcodeVM(prg, phaseSetting[0], 0)
    prg = origPrg.copy()
    output = intcodeVM(prg, phaseSetting[1], output)
    prg = origPrg.copy()
    output = intcodeVM(prg, phaseSetting[2], output)
    prg = origPrg.copy()
    output = intcodeVM(prg, phaseSetting[3], output)
    prg = origPrg.copy()
    output = intcodeVM(prg, phaseSetting[4], output)

    if output > maxSignal:
        maxSignal = output

print(maxSignal)

