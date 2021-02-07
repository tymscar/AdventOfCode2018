class IntcodeVM:
    def __init__(self, memoryLayout):
        self.memory = memoryLayout
        self.prgOutput = 0
        self.instructionRead = 0
        self.pc = 0
        self.rbase = 0
        self.padMemory(100000)
        self.finished = False

    def padMemory(self, toThis):
        while len(self.memory) < toThis + 1:
            self.memory.append(0)

    def run(self, in1):
        self.prgInput = in1
        while True:
            self.instructionRead = int(self.memory[self.pc])
            opcode = self.instructionRead % 100
            modes = int(self.instructionRead / 100)

            if int(opcode) == 99:
                self.finished = True
                break

            stop = False
            jumped = False
            length = 0
            paramOne = 0
            paramTwo = 0
            paramThree = 0
            operandOne = 0
            operandTwo = 0
            operandThree = 0

            if (self.pc + 1) < len(self.memory):
                paramOne = int(self.memory[self.pc + 1])
            if (self.pc + 2) < len(self.memory):
                paramTwo = int(self.memory[self.pc + 2])
            if (self.pc + 3) < len(self.memory):
                paramThree = int(self.memory[self.pc + 3])

            if modes % 10 == 0 and paramOne < len(self.memory):
                operandOne = int(self.memory[paramOne])
            elif modes % 10 == 2 and (paramOne + self.rbase) < len(self.memory):
                operandOne = int(self.memory[paramOne + self.rbase])
            else:
                operandOne = paramOne

            if int((modes % 100) / 10) == 0 and paramTwo < len(self.memory):
                operandTwo = int(self.memory[paramTwo])
            elif int((modes % 100) / 10) == 2 and (paramTwo + self.rbase) < len(self.memory):
                operandTwo = int(self.memory[paramTwo + self.rbase])
            else:
                operandTwo = paramTwo

            if int(int(modes % 1000) / 100) == 0 and paramThree < len(self.memory):
                operandThree = int(self.memory[paramThree])
            elif int(int(modes % 1000) / 100) == 2 and (paramThree + self.rbase) < len(self.memory):
                operandThree = int(self.memory[paramThree + self.rbase])
            else:
                operandThree = paramThree

            if int(opcode) == 1:
                length = 4
                if int(int(modes % 1000) / 100) == 2:
                    self.memory[paramThree + self.rbase] = operandOne + operandTwo
                else:
                    self.memory[paramThree] = operandOne + operandTwo

            if int(opcode) == 2:
                length = 4
                if int(int(modes % 1000) / 100) == 2:
                    self.memory[paramThree + self.rbase] = operandOne * operandTwo
                else:
                    self.memory[paramThree] = operandOne * operandTwo

            if int(opcode) == 3:
                length = 2
                if modes % 10 == 2:
                    self.memory[paramOne + self.rbase] = self.prgInput
                else:
                    self.memory[paramOne] = self.prgInput
                #self.prgInput = in2

            if int(opcode) == 4:
                length = 2
                self.prgOutput = operandOne
                stop = True

            if int(opcode) == 5:
                length = 3
                if operandOne != 0:
                    self.pc = operandTwo
                    jumped = True

            if int(opcode) == 6:
                length = 3
                if operandOne == 0:
                    self.pc = operandTwo
                    jumped = True

            if int(opcode) == 7:
                length = 4
                ans = 0
                if operandOne < operandTwo:
                    ans = 1
                else:
                    ans = 0
                if int(int(modes % 1000) / 100) == 2:
                    self.memory[paramThree + self.rbase] = ans
                else:
                    self.memory[paramThree] = ans

            if int(opcode) == 8:
                length = 4
                ans = 0
                if operandOne == operandTwo:
                    ans = 1
                else:
                    ans = 0

                if int(int(modes % 1000) / 100) == 2:
                    self.memory[paramThree + self.rbase] = ans
                else:
                    self.memory[paramThree] = ans

            if int(opcode) == 9:
                length = 2
                self.rbase += operandOne

            if jumped == False:
                self.pc = self.pc + length
                self.instructionRead = int(self.memory[self.pc])

            if stop:
                break