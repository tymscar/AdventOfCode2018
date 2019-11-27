#include <iostream>
#include <algorithm>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <string>

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;

	std::unordered_map<char, std::vector<char>> dependenciesOf;

	std::vector<char> stepsRem;
	std::vector<char> stepsDone; // Maybe remove?

	std::string installOrder = "";

	while (file >> line)
	{
		//step currentStep;
		char program, dependsOn;
		file >> line;
		//currentStep.id = line[0];
		dependsOn = line[0];
		file >> line >> line >> line >> line >> line >> line;
		//currentStep.depOf = line[0];
		program = line[0];
		file >> line >> line;
		if (std::find(stepsRem.begin(), stepsRem.end(), program) == stepsRem.end()){
			stepsRem.push_back(program);
		}
		if (std::find(stepsRem.begin(), stepsRem.end(), dependsOn) == stepsRem.end()){
			stepsRem.push_back(dependsOn);
		}
		//stepsRem.push_back(currentStep);
		dependenciesOf[program].push_back(dependsOn);
	}

	while (static_cast<int>(stepsRem.size()) != 0){
		char currentProgram = 'Z';
		for (auto s : stepsRem){
			if (static_cast<int>(dependenciesOf[s].size()) == 0 && s < currentProgram){
				currentProgram = s;
			}
		}
		stepsRem.erase(std::remove(stepsRem.begin(), stepsRem.end(), currentProgram), stepsRem.end());
		
		for (auto prog : stepsRem){
			dependenciesOf[prog].erase(std::remove(dependenciesOf[prog].begin(), dependenciesOf[prog].end(), currentProgram), dependenciesOf[prog].end());
		}

		stepsDone.push_back(currentProgram);
		installOrder += currentProgram;
	}

	std::cout << installOrder;
}