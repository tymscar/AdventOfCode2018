#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>


std::vector<int> eqrr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	if (registorState[inputOne] == registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> eqri(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	if (registorState[inputOne] == inputTwo)
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> eqir(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	if (inputOne == registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> gtrr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	if (registorState[inputOne] > registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> gtri(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	if (registorState[inputOne] > inputTwo)
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> gtir(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	if (inputOne > registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> seti(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = inputOne;
	return registorState;
}

std::vector<int> setr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne];
	return registorState;
}

std::vector<int> bori(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] | inputTwo;
	return registorState;
}

std::vector<int> borr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] | registorState[inputTwo];
	return registorState;
}

std::vector<int> bani(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] & inputTwo;
	return registorState;
}

std::vector<int> banr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] & registorState[inputTwo];
	return registorState;
}

std::vector<int> mulr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] * registorState[inputTwo];
	return registorState;
}

std::vector<int> muli(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] * inputTwo;
	return registorState;
}

std::vector<int> addr(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] + registorState[inputTwo];
	return registorState;
}

std::vector<int> addi(int inputOne, int inputTwo, int output, std::vector<int> registorState) {
	registorState[output] = registorState[inputOne] + inputTwo;
	return registorState;
}


struct instruction {
	int id;
	std::string name;
	int A;
	int B;
	int C;
};

void runInstruction(instruction* inst, std::vector<int>& registers) {
	int A = inst->A;
	int B = inst->B;
	int C = inst->C;

	if (inst->name == "addr") {
		registers = addr(A, B, C, registers);
	}
	if (inst->name == "addi") {
		registers = addi(A, B, C, registers);
	}
	if (inst->name == "mulr") {
		registers = mulr(A, B, C, registers);
	}
	if (inst->name == "muli") {
		registers = muli(A, B, C, registers);
	}
	if (inst->name == "banr") {
		registers = banr(A, B, C, registers);
	}
	if (inst->name == "bani") {
		registers = bani(A, B, C, registers);
	}
	if (inst->name == "borr") {
		registers = borr(A, B, C, registers);
	}
	if (inst->name == "bori") {
		registers = bori(A, B, C, registers);
	}
	if (inst->name == "setr") {
		registers = setr(A, B, C, registers);
	}
	if (inst->name == "seti") {
		registers = seti(A, B, C, registers);
	}
	if (inst->name == "gtir") {
		registers = gtir(A, B, C, registers);
	}
	if (inst->name == "gtri") {
		registers = gtri(A, B, C, registers);
	}
	if (inst->name == "gtrr") {
		registers = gtrr(A, B, C, registers);
	}
	if (inst->name == "eqir") {
		registers = eqir(A, B, C, registers);
	}
	if (inst->name == "eqri") {
		registers = eqri(A, B, C, registers);
	}
	if (inst->name == "eqrr") {
		registers = eqrr(A, B, C, registers);
	}
}

int main()
{
	std::ifstream file;
	file.open("input.txt");
	std::string input;

	std::vector<int> registers;
	for (int i = 0; i < 6; i++) {
		registers.push_back(0);
	}
	registers[0] = 12213578;

	std::vector<instruction*> instructions;

	int instructionPointerRegister;
	file >> input;
	file >> input;
	instructionPointerRegister = std::stoi(input);
	while (file >> input) {
		instruction* currentInst = new instruction();
		currentInst->name = input;
		file >> input;
		currentInst->A = std::stoi(input);
		file >> input;
		currentInst->B = std::stoi(input);
		file >> input;
		currentInst->C = std::stoi(input);

		instructions.push_back(currentInst);
	}

	int ip = 0;
	while (ip < instructions.size()) {

		//	std::cout << "ip=" << ip << "  [";
		//	for (int i = 0; i < 6; i++) {
		//		std::cout << registers[i] << " ";
		//	}
		//	std::cout << "]  " << instructions[ip]->name << " ";
		//	std::cout << instructions[ip]->A << " " << instructions[ip]->B << " " << instructions[ip]->C ;


		runInstruction(instructions[ip], registers);


		//	std::cout << "  [";
		//	for (int i = 0; i < 6; i++) {
		//		std::cout << registers[i] << " ";
		//	}
		//	std::cout << "]" << std::endl;

		registers[instructionPointerRegister]++;
		ip = registers[instructionPointerRegister];
	}

	
	std::cout << registers[0] << std::endl;
}
