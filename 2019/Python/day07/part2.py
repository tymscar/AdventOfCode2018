from sympy.utilities.iterables import multiset_permutations

def intcodeVM(stp, whichVM, progcount, runstate, memoryIn, inpt, inpt2):
    prgInput = 0
    if runstate[whichVM] == 0:
        prgInput = inpt[whichVM]
    else:
        prgInput = inpt2
    prgOutput = 0
    instructionRead = 0
    memory = memoryIn[whichVM]
    pc = progcount[whichVM]

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
            if runstate[whichVM] == 0:
                prgInput = inpt2


        if int(opcode) == 4:
            length = 2
            prgOutput = operandOne
            memoryIn[whichVM] = memory
            pc = pc + length
            progcount[whichVM] = pc
            return prgOutput

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

        runstate[whichVM] = 1 # this program ran at least once
        if jumped == False:
            pc = pc + length
            instructionRead = int(memory[pc])

    stp[0] = True
    memoryIn[whichVM] = memory
    progcount[whichVM] = pc
    return prgOutput

file = open('input.txt', 'r')

for line in file:
    origPrg = line.split(',')

phaseSettings = list(multiset_permutations([5,6,7,8,9]))
prg = []

output = [0,0,0,0,0]
maxSignal = 0

for phaseSetting in phaseSettings:
    prg.clear()
    for i in range(0, 5):
        prg.append(origPrg.copy())
    output = [0, 0, 0, 0, 0]
    RUNSTATES = [0,0,0,0,0]
    programCounters = [0,0,0,0,0]
    STOP = [False]
    thrusterEOutPut = 0
    while STOP[0] == False:
        thrusterEOutPut = output[4]

        # halted,which vm is this, this vms program counter, has this run before, memorymap, phase, actual input
        output[0] = intcodeVM(STOP, 0, programCounters, RUNSTATES, prg, phaseSetting, output[4])
        output[1] = intcodeVM(STOP, 1, programCounters, RUNSTATES, prg, phaseSetting, output[0])
        output[2] = intcodeVM(STOP, 2, programCounters, RUNSTATES, prg, phaseSetting, output[1])
        output[3] = intcodeVM(STOP, 3, programCounters, RUNSTATES, prg, phaseSetting, output[2])
        output[4] = intcodeVM(STOP, 4, programCounters, RUNSTATES, prg, phaseSetting, output[3])

    if thrusterEOutPut > maxSignal:
        maxSignal = thrusterEOutPut

print(maxSignal)