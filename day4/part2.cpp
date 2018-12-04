#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

struct guard{
	int id;
	int lastZz;
	std::unordered_map<int, int> minSleeping;
	int simSleep;
	int mostSleepyMin;
};

int main(){
	std::unordered_map<int, guard> guards;
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
			if(currentGuard.id != -1){
				guards[currentGuard.id] = currentGuard;
			}
			bool wasInHashmap = false;
			for(auto& g : guards){
				if(g.first == std::stoi(lineInTheFile)){
					wasInHashmap = true;
					currentGuard = g.second;
				}
			}
			if(!wasInHashmap){
				guard empty;
				currentGuard = empty;
				currentGuard.id = std::stoi(lineInTheFile);
				currentGuard.simSleep = 0;
				currentGuard.mostSleepyMin = 0;
			}
			inputFileStream >> lineInTheFile;	
			inputFileStream >> lineInTheFile;
		}	

		if((elemCheck+1) % 4 == 0){
			if(lineInTheFile[0] == 'a'){ //a from asleep
				currentGuard.lastZz = minute;
			}
			if(lineInTheFile[0] == 'u'){ //u from up
				for(int i=currentGuard.lastZz; i<minute; i++){
					bool minSlept = false;
					for(auto& m : currentGuard.minSleeping){
						if(m.first == i)
							minSlept = true;
					}
					if(minSlept)
						currentGuard.minSleeping[i]++;
					else
						currentGuard.minSleeping[i] = 1;
				}
			}	
		}

		if((elemCheck + 3) % 4 == 0){
			minute = std::stoi(lineInTheFile.substr(3,2));
		}
		elemCheck++;
	}
	guards[currentGuard.id] = currentGuard;


	for(auto& g : guards){
		for(auto& m : g.second.minSleeping){
			if(m.second > g.second.simSleep){
				g.second.simSleep = m.second;
				g.second.mostSleepyMin = m.first;
			}
		}		
	}
	int topSleepMin;
	int topSleeperID;
	int howSleepy = 0;
	for(auto& g: guards){
		if(g.second.simSleep > howSleepy){
			howSleepy = g.second.simSleep;
			topSleepMin = g.second.mostSleepyMin;
			topSleeperID = g.first;
		}
	}

	std::cout << topSleeperID * topSleepMin;


}
