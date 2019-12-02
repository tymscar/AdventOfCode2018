import math


file = open('input.txt','r')

	
for line in file:
	memory = line.split(',')
	
opcode = 0
pc = 0

memory[1] = 12
memory[2] = 2
	
while True:
	opcode = memory[pc]
	if int(opcode) == 99:
		break
		
	operandOne = int(memory[pc+1])
	operandTwo = int(memory[pc+2])
	
	if int(opcode) == 1:
		memory[int(memory[pc+3])] = int(memory[operandOne]) + int(memory[operandTwo])
	if int(opcode) == 2:
		memory[int(memory[pc+3])] = int(memory [operandOne]) * int(memory[operandTwo])
	
	pc = pc + 4
	opcode = int(memory[pc])
	
print(memory [0])
