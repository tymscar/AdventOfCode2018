#include <iostream>
#include <algorithm>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <string>

struct time{
	int timeLeft;
	char program;
};

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;

	std::unordered_map<char, std::vector<char>> dependenciesOf;

	std::vector<time> currentProgram;

	std::vector<char> stepsRem;
	std::vector<char> inProgress;

	int timePassed = -1;

	std::string installOrder = "";

	// add workers
	for (int i = 0; i < 5; i++){
		time worker;
		worker.program = '.';
		worker.timeLeft = 0;
		currentProgram.push_back(worker);
	}

	while (file >> line)
	{
		char program, dependsOn;
		file >> line;
		dependsOn = line[0];
		file >> line >> line >> line >> line >> line >> line;
		program = line[0];
		file >> line >> line;
		if (std::find(stepsRem.begin(), stepsRem.end(), program) == stepsRem.end()){
			stepsRem.push_back(program);
		}
		if (std::find(stepsRem.begin(), stepsRem.end(), dependsOn) == stepsRem.end()){
			stepsRem.push_back(dependsOn);
		}
		dependenciesOf[program].push_back(dependsOn);
	}
	
	while (static_cast<int>(stepsRem.size()) != 0 || static_cast<int>(inProgress.size()) != 0){
		

		for (auto& worker : currentProgram){
			if (worker.program != '.') {
				worker.timeLeft--;
			}
			if (worker.timeLeft == 0 && worker.program != '.'){
				for (auto prog : stepsRem){
					dependenciesOf[prog].erase(std::remove(dependenciesOf[prog].begin(), dependenciesOf[prog].end(), worker.program), dependenciesOf[prog].end());
				}
				stepsRem.erase(std::remove(stepsRem.begin(), stepsRem.end(), worker.program), stepsRem.end());
				inProgress.erase(std::remove(inProgress.begin(), inProgress.end(), worker.program), inProgress.end());
				
				installOrder += worker.program;
				worker.program = '.';
			}

			char potentialProgram = '{';

			for (auto s : stepsRem){
				if (std::find(inProgress.begin(), inProgress.end(), s) == inProgress.end()){
					if (static_cast<int>(dependenciesOf[s].size()) == 0 && s < potentialProgram){
						potentialProgram = s;
					}
				}
			}

			if (worker.program == '.' && potentialProgram != '{'){
				worker.program = potentialProgram;
				worker.timeLeft = int(potentialProgram) - 4;
				inProgress.push_back(potentialProgram);
			}
		}
		if (static_cast<int>(stepsRem.size()) != 0 || static_cast<int>(inProgress.size()) != 0){
			timePassed++;
		}
	}

	std::cout << timePassed << std::endl;
}