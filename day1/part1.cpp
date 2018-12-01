#include <iostream>
#include <fstream>
#include <string>

int main(){
	std::ifstream inputFileStream;
	inputFileStream.open("input.txt");
	std::string lineInTheFile;
	int finalNumber = 0;
	while(inputFileStream >> lineInTheFile){
		if(lineInTheFile[0] == '+'){
			finalNumber += std::stoi(lineInTheFile.substr(1));
		} else {
			finalNumber -= std::stoi(lineInTheFile.substr(1));
		}
	}
	std::cout << finalNumber;
}
