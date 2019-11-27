#include <iostream>
#include <fstream>
#include <string>

int main(){
	std::ifstream firstReader, secondReader;
	std::string theAnswer;
	firstReader.open("input.txt");
	std::string firstLine, secondLine;
	bool finished = false;
	while(firstReader >> firstLine && !finished){
		secondReader.open("input.txt");
		while(secondReader >> secondLine){
			int mismatched = 0;
			for(int i=0; i<firstLine.size(); i++){
					if(firstLine[i] != secondLine[i]){
						mismatched++;
						theAnswer = firstLine;
						theAnswer.erase(i,1);
					}
			}
			if(mismatched == 1){
				finished = true;
				break;
			}
		}
		secondReader.close();
	}
	std::cout << theAnswer;
}
