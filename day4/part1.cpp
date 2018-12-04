#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

struct guard{
	int id;
	int minSlept;
	int lastZz;
	std::unordered_map<int, int> minSleeping;
};

int main(){
	std::vector<guard> guards;
	std::ifstream inputFileStream;
	system("sort input.txt > inputSorted.txt");
	inputFileStream.open("inputSorted.txt");
	std::string lineInTheFile;
	int elemCheck = 0;
	int minute = 0;
	guard currentGuard;
	currentGuard.id = -1;
	while(inputFileStream >> lineInTheFile){
		//Skip the 'begin shift text'
		if((elemCheck + 1) % 4 == 0  && lineInTheFile[lineInTheFile.size()-1] != 'p'){
			lineInTheFile.erase(0,1);
			if(currentGuard.id != -1 ){
				guards.push_back(currentGuard);
			}

			currentGuard.id = std::stoi(lineInTheFile);
			currentGuard.minSlept = 0;
			for(auto& g : guards){
				if(g.id == currentGuard.id)
					currentGuard = g;
			}
			inputFileStream >> lineInTheFile;	
			inputFileStream >> lineInTheFile;
		}	
		if((elemCheck+1) % 4 == 0){
			if(lineInTheFile[0] == 'a'){ //a from asleep
				currentGuard.lastZz = minute;
			}
			if(lineInTheFile[0] == 'u'){ //u from up
				currentGuard.minSlept += minute - currentGuard.lastZz; 
				for(int i=currentGuard.lastZz; i< minute; i++){
					if(currentGuard.minSleeping.find(i) == currentGuard.minSleeping.end()){
						currentGuard.minSleeping[i] = 0;
					}
					currentGuard.minSleeping[i]++;
				}

			}	
		}

		if((elemCheck + 3) % 4 == 0){
			minute = std::stoi(lineInTheFile.substr(3,2));
		}
		elemCheck++;
	}
	guards.push_back(currentGuard);

	int mostSleptMins = 0;
	guard* sleepiestGuard;
	for(auto& g : guards){
		if(g.minSlept > mostSleptMins)
		{
			mostSleptMins = g.minSlept;
			sleepiestGuard = &g;
		}
	}
	int mostSleptTime = 0;
	int mostSleptMin = 0;
	for(auto min: sleepiestGuard->minSleeping){
		if(min.second > mostSleptTime){
			mostSleptTime = min.second;
			mostSleptMin = min.first;
		}
	}
	std::cout << mostSleptMin * sleepiestGuard->id;
}
