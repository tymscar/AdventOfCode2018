#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>


std::vector<int> eqrr (int inputOne, int inputTwo, int output, std::vector<int> registorState){
	if(registorState[inputOne] == registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> eqri (int inputOne, int inputTwo, int output, std::vector<int> registorState){
	if(registorState[inputOne] == inputTwo)
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> eqir(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	if(inputOne == registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> gtrr (int inputOne, int inputTwo, int output, std::vector<int> registorState){
	if(registorState[inputOne] > registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> gtri (int inputOne, int inputTwo, int output, std::vector<int> registorState){
	if(registorState[inputOne] > inputTwo)
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> gtir(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	if(inputOne > registorState[inputTwo])
		registorState[output] = 1;
	else
		registorState[output] = 0;
	return registorState;
}

std::vector<int> seti(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = inputOne;
	return registorState;
}

std::vector<int> setr(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne];
	return registorState;
}

std::vector<int> bori(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] | inputTwo;
	return registorState;
}

std::vector<int> borr(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] | registorState[inputTwo];
	return registorState;
}

std::vector<int> bani(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] & inputTwo;
	return registorState;
}

std::vector<int> banr(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] & registorState[inputTwo];
	return registorState;
}

std::vector<int> mulr(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] * registorState[inputTwo];
	return registorState;
}

std::vector<int> muli(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] * inputTwo;
	return registorState;
}

std::vector<int> addr(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] + registorState[inputTwo];
	return registorState;
}

std::vector<int> addi(int inputOne, int inputTwo, int output, std::vector<int> registorState){
	registorState[output] = registorState[inputOne] + inputTwo;
	return registorState;
}

int main(){
	std::ifstream file;
	file.open("part1in.txt");
	std::string input;

	int howManyBehaveLike3OrMore = 0;

	while(file >> input){
		std::vector<int> registorsOld;
		file >> input;
		registorsOld.push_back(input[1] - '0');
		file >> input;
		registorsOld.push_back(input[0] - '0');
		file >> input;
		registorsOld.push_back(input[0] - '0');
		file >> input;
		registorsOld.push_back(input[0] - '0');


		int opcode, A, B, C;
		file >> input;
		opcode = std::stoi(input);
		file >> input;
		A = std::stoi(input);
		file >> input;
		B = std::stoi(input);
		file >> input;
		C = std::stoi(input);
		file >> input;

		std::vector<int> registorsNew;
		file >> input;
		registorsNew.push_back(input[1] - '0');
		file >> input;
		registorsNew.push_back(input[0] - '0');
		file >> input;
		registorsNew.push_back(input[0] - '0');
		file >> input;
		registorsNew.push_back(input[0] - '0');

		int howManyOpcodesDoesItBehaveLike = 0;

		if(addr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(addi(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(mulr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(muli(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(banr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(bani(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(borr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(bori(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(setr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(seti(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(gtir(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(gtri(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(gtrr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(eqir(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(eqri(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(eqrr(A, B, C, registorsOld) == registorsNew){
			howManyOpcodesDoesItBehaveLike++;
		}

		if(howManyOpcodesDoesItBehaveLike >= 3)
			howManyBehaveLike3OrMore++;

	}

	std::cout << howManyBehaveLike3OrMore << std::endl;
}
