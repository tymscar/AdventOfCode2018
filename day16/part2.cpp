#include <iostream>
#include <algorithm>
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

void execute(int opcode, int A, int B, int C, std::unordered_map<int, std::string>& opcodeToNameOfFunction, std::vector<int>& registers){
	if(opcodeToNameOfFunction[opcode] == "addr"){
		registers = addr(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "addi"){
		registers = addi(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "mulr"){
		registers = mulr(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "muli"){
		registers = muli(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "banr"){
		registers = banr(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "bani"){
		registers = bani(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "borr"){
		registers = borr(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "bori"){
		registers = bori(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "setr"){
		registers = setr(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "seti"){
		registers = seti(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "gtir"){
		registers = gtir(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "gtri"){
		registers = gtri(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "gtrr"){
		registers = gtrr(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "eqir"){
		registers = eqir(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "eqri"){
		registers = eqri(A, B, C, registers);
	}
	if(opcodeToNameOfFunction[opcode] == "eqrr"){
		registers = eqrr(A, B, C, registers);
	}
}
 

int main(){
	std::ifstream file;
	file.open("part1in.txt");
	std::string input;
	
	std::unordered_map<int, std::vector<std::string> > opcodeNameList;
	for(int i=0;i<16;i++){
		opcodeNameList[i].push_back("addr");		
		opcodeNameList[i].push_back("addi");
		opcodeNameList[i].push_back("mulr");	
		opcodeNameList[i].push_back("muli");	
		opcodeNameList[i].push_back("banr");	
		opcodeNameList[i].push_back("bani");	
		opcodeNameList[i].push_back("borr");	
		opcodeNameList[i].push_back("bori");	
		opcodeNameList[i].push_back("setr");	
		opcodeNameList[i].push_back("seti");	
		opcodeNameList[i].push_back("gtir");	
		opcodeNameList[i].push_back("gtri");	
		opcodeNameList[i].push_back("gtrr");	
		opcodeNameList[i].push_back("eqir");	
		opcodeNameList[i].push_back("eqri");	
		opcodeNameList[i].push_back("eqrr");
	}
	std::unordered_map<std::string, std::vector<int> >nameOpcodeList;
	for(int i=0; i<16; i++){
		nameOpcodeList["addr"].push_back(i);		
		nameOpcodeList["addi"].push_back(i);
		nameOpcodeList["mulr"].push_back(i);	
		nameOpcodeList["muli"].push_back(i);
		nameOpcodeList["banr"].push_back(i);
		nameOpcodeList["bani"].push_back(i);
		nameOpcodeList["borr"].push_back(i);
		nameOpcodeList["bori"].push_back(i);
		nameOpcodeList["setr"].push_back(i);
		nameOpcodeList["seti"].push_back(i);
		nameOpcodeList["gtir"].push_back(i);
		nameOpcodeList["gtri"].push_back(i);
		nameOpcodeList["gtrr"].push_back(i);
		nameOpcodeList["eqir"].push_back(i);
		nameOpcodeList["eqri"].push_back(i);
		nameOpcodeList["eqrr"].push_back(i);
	}

	int opcodesLeft = 16;

	std::unordered_map<std::string, int> opcodeId;

	opcodeId["addr"] = -1;
	opcodeId["addi"] = -1;
	opcodeId["mulr"] = -1;	
	opcodeId["muli"] = -1;
	opcodeId["banr"] = -1;
	opcodeId["bani"] = -1;
	opcodeId["borr"] = -1;
	opcodeId["bori"] = -1;
	opcodeId["setr"] = -1;
	opcodeId["seti"] = -1;
	opcodeId["gtir"] = -1;
	opcodeId["gtri"] = -1;
	opcodeId["gtrr"] = -1;
	opcodeId["eqir"] = -1;
	opcodeId["eqri"] = -1;
	opcodeId["eqrr"] = -1;

	

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

		if(addr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "addr"), opcodeNameList[opcode].end());
			nameOpcodeList["addr"].erase(std::remove(nameOpcodeList["addr"].begin(), nameOpcodeList["addr"].end(), opcode), nameOpcodeList["addr"].end());
		}

		if(addi(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "addi"), opcodeNameList[opcode].end());
			nameOpcodeList["addi"].erase(std::remove(nameOpcodeList["addi"].begin(), nameOpcodeList["addi"].end(), opcode), nameOpcodeList["addi"].end());
		}

		if(mulr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "mulr"), opcodeNameList[opcode].end());
			nameOpcodeList["mulr"].erase(std::remove(nameOpcodeList["mulr"].begin(), nameOpcodeList["mulr"].end(), opcode), nameOpcodeList["mulr"].end());
		}

		if(muli(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "muli"), opcodeNameList[opcode].end());
			nameOpcodeList["muli"].erase(std::remove(nameOpcodeList["muli"].begin(), nameOpcodeList["muli"].end(), opcode), nameOpcodeList["muli"].end());
		}

		if(banr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "banr"), opcodeNameList[opcode].end());
			nameOpcodeList["banr"].erase(std::remove(nameOpcodeList["banr"].begin(), nameOpcodeList["banr"].end(), opcode), nameOpcodeList["banr"].end());
		}

		if(bani(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "bani"), opcodeNameList[opcode].end());
			nameOpcodeList["bani"].erase(std::remove(nameOpcodeList["bani"].begin(), nameOpcodeList["bani"].end(), opcode), nameOpcodeList["bani"].end());
		}

		if(borr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "borr"), opcodeNameList[opcode].end());
			nameOpcodeList["borr"].erase(std::remove(nameOpcodeList["borr"].begin(), nameOpcodeList["borr"].end(), opcode), nameOpcodeList["borr"].end());
		}

		if(bori(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "bori"), opcodeNameList[opcode].end());
			nameOpcodeList["bori"].erase(std::remove(nameOpcodeList["bori"].begin(), nameOpcodeList["bori"].end(), opcode), nameOpcodeList["bori"].end());
		}

		if(setr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "setr"), opcodeNameList[opcode].end());
			nameOpcodeList["setr"].erase(std::remove(nameOpcodeList["setr"].begin(), nameOpcodeList["setr"].end(), opcode), nameOpcodeList["setr"].end());
		}

		if(seti(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "seti"), opcodeNameList[opcode].end());
			nameOpcodeList["seti"].erase(std::remove(nameOpcodeList["seti"].begin(), nameOpcodeList["seti"].end(), opcode), nameOpcodeList["seti"].end());
		}

		if(gtir(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "gtir"), opcodeNameList[opcode].end());
			nameOpcodeList["gtir"].erase(std::remove(nameOpcodeList["gtir"].begin(), nameOpcodeList["gtir"].end(), opcode), nameOpcodeList["gtir"].end());
		}

		if(gtri(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "gtri"), opcodeNameList[opcode].end());
			nameOpcodeList["gtri"].erase(std::remove(nameOpcodeList["gtri"].begin(), nameOpcodeList["gtri"].end(), opcode), nameOpcodeList["gtri"].end());
		}

		if(gtrr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "gtrr"), opcodeNameList[opcode].end());
			nameOpcodeList["gtrr"].erase(std::remove(nameOpcodeList["gtrr"].begin(), nameOpcodeList["gtrr"].end(), opcode), nameOpcodeList["gtrr"].end());
		}

		if(eqir(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "eqir"), opcodeNameList[opcode].end());
			nameOpcodeList["eqir"].erase(std::remove(nameOpcodeList["eqir"].begin(), nameOpcodeList["eqir"].end(), opcode), nameOpcodeList["eqir"].end());
		}

		if(eqri(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "eqri"), opcodeNameList[opcode].end());
			nameOpcodeList["eqri"].erase(std::remove(nameOpcodeList["eqri"].begin(), nameOpcodeList["eqri"].end(), opcode), nameOpcodeList["eqri"].end());
		}

		if(eqrr(A, B, C, registorsOld) != registorsNew){
			opcodeNameList[opcode].erase(std::remove(opcodeNameList[opcode].begin(), opcodeNameList[opcode].end(), "eqrr"), opcodeNameList[opcode].end());
			nameOpcodeList["eqrr"].erase(std::remove(nameOpcodeList["eqrr"].begin(), nameOpcodeList["eqrr"].end(), opcode), nameOpcodeList["eqrr"].end());
		}
	}
	while(opcodesLeft > -10){
		for(int i=0;i<16;i++){
			if(opcodeNameList[i].size() == 1){
				opcodeId[opcodeNameList[i][0]] = i;
				std::string opToRem = opcodeNameList[i][0];
				for(int j=0; j<16; j++){
					opcodeNameList[j].erase(std::remove(opcodeNameList[j].begin(), opcodeNameList[j].end(), opToRem), opcodeNameList[j].end());
				}
				for(auto f: nameOpcodeList){
					f.second.erase(std::remove(f.second.begin(), f.second.end(), i), f.second.end());
				}
				opcodesLeft--;
			}
		}
		for(auto f: nameOpcodeList){
			if(f.second.size() == 1){
				opcodeId[f.first] = f.second[0];
				int insToRem = f.second[0];
				for(int i=0; i<16; i++){
					//daca gaseste
					opcodeNameList[i].erase(std::remove(opcodeNameList[i].begin(), opcodeNameList[i].end(), f.first), opcodeNameList[i].end());
				}
				for(auto g: nameOpcodeList){
					//daca gaseste
					g.second.erase(std::remove(g.second.begin(), g.second.end(), insToRem), g.second.end());
				}
				opcodesLeft--;
			}
		}
	}

	std::unordered_map<int, std::string> opcodeToNameOfFunction;
	for(int i=0; i<16; i++){
		opcodeToNameOfFunction[i] = " ";
	}

	for(auto o: opcodeId){
		opcodeToNameOfFunction[o.second] = o.first;	
	}

	std::ifstream fileTwo;
	fileTwo.open("part2in.txt");
	std::string inputPart2;


	std::vector<int> part2regs;
	part2regs.push_back(0);
	part2regs.push_back(0);
	part2regs.push_back(0);
	part2regs.push_back(0);
	
	
	while(fileTwo >> inputPart2){
		int opcode = std::stoi(inputPart2);
		fileTwo >> inputPart2;
		int A = std::stoi(inputPart2);
		fileTwo >> inputPart2;
		int B = std::stoi(inputPart2);
		fileTwo >> inputPart2;
		int C = std::stoi(inputPart2);
		execute(opcode, A, B, C, opcodeToNameOfFunction, part2regs);
	}
	

	std::cout << part2regs[0] << std::endl;

}
