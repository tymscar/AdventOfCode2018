prgInput = 2
file = open('input.txt', 'r')

for line in file:
    memory = line.split(',')


prgOutput = 0
instructionRead = 0
pc = 0
rbase = 0

def padMemory(toThis, mem):
    while len(mem) < toThis + 1:
        mem.append(0)

padMemory(100000, memory)

while True:
    instructionRead = int(memory[pc])
    opcode = instructionRead % 100
    modes = int(instructionRead/100)

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
    elif modes % 10 == 2 and (paramOne + rbase) < len(memory):
        operandOne = int(memory[paramOne + rbase])
    else:
        operandOne = paramOne

    if int((modes % 100) / 10) == 0 and paramTwo < len(memory):
        operandTwo = int(memory[paramTwo])
    elif int((modes % 100) / 10) == 2 and (paramTwo + rbase) < len(memory):
        operandTwo = int(memory[paramTwo + rbase])
    else:
        operandTwo = paramTwo

    if int(int(modes%1000) / 100) == 0 and paramThree < len(memory):
        operandThree = int(memory[paramThree])
    elif int(int(modes%1000) / 100) == 2 and (paramThree + rbase) < len(memory):
        operandThree = int(memory[paramThree + rbase])
    else:
        operandThree = paramThree






    if int(opcode) == 1:
        length = 4
        if int(int(modes%1000) / 100) == 2:
            memory[paramThree + rbase] = operandOne + operandTwo
        else:
            memory[paramThree] = operandOne + operandTwo

    if int(opcode) == 2:
        length = 4
        if int(int(modes%1000) / 100) == 2:
            memory[paramThree + rbase] = operandOne * operandTwo
        else:
            memory[paramThree] = operandOne * operandTwo

    if int(opcode) == 3:
        length = 2
        if modes % 10 == 2:
            memory[paramOne + rbase] = prgInput
        else:
            memory[paramOne] = prgInput

    if int(opcode) == 4:
        length = 2
        prgOutput = operandOne
        print(prgOutput)

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
        ans = 0
        if operandOne < operandTwo:
            ans = 1
        else:
            ans = 0
        if int(int(modes%1000) / 100) == 2:
            memory[paramThree + rbase] = ans
        else:
            memory[paramThree] = ans

    if int(opcode) == 8:
        length = 4
        ans = 0
        if operandOne == operandTwo:
            ans = 1
        else:
            ans = 0

        if int(int(modes%1000) / 100) == 2:
            memory[paramThree + rbase] = ans
        else:
            memory[paramThree] = ans

    if int(opcode) == 9:
        length = 2
        rbase += operandOne



    if jumped == False:
        pc = pc + length
        instructionRead = int(memory[pc])
