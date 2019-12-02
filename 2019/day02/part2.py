import math


file = open('input.txt','r')

	
for line in file:
	initialMemory = line.split(',')
	
bruteforce = -1
result = 0


while result != 19690720:
	
	memory = initialMemory.copy()
	bruteforce = bruteforce + 1
	opcode = 0
	pc = 0
	
	memory[1] = int(bruteforce/100)
	memory[2] = int(bruteforce%100)
		
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
		
	result = memory[0]
	
print(bruteforce)
