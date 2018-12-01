#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

int main(){
	std::ifstream inputFileStream;
	std::string lineInTheFile;
	std::unordered_map<int, int> freqCheck;

	int finalNumber = 0;
	bool foundFreqTwice = false;

	freqCheck[0] = 1;

	while(!foundFreqTwice){
		inputFileStream.open("input.txt");
		while(inputFileStream >> lineInTheFile){
			if(lineInTheFile[0] == '+'){
				finalNumber += std::stoi(lineInTheFile.substr(1));
			} else {
				finalNumber -= std::stoi(lineInTheFile.substr(1));
			}
			if (freqCheck.find(finalNumber) == freqCheck.end()){
				freqCheck[finalNumber] = 0;
			}
			freqCheck[finalNumber]++;
			if(freqCheck[finalNumber] == 2){
				foundFreqTwice = true;
				std::cout << finalNumber << std::endl;
				break;
			}
		}
		inputFileStream.close();
	}
}
