#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

int main(){
	int twice = 0;
	int thrice = 0;
	std::ifstream inputFileStream;
	inputFileStream.open("input.txt");
	std::string lineInTheFile;
	std::unordered_map<char, int> lineMap;
	while(inputFileStream >> lineInTheFile){
		bool foundTwoAlready = false;
		bool foundThreeAlready = false;
		for(char& c : lineInTheFile){
			if(lineMap.find(c) == lineMap.end())
				lineMap[c] = 1;
			else
				lineMap[c]++;
		}
		for(auto& it : lineMap){
			if(!foundTwoAlready && it.second == 2){
				foundTwoAlready = true;
				twice++;
			}
			if(!foundThreeAlready && it.second == 3){
				foundThreeAlready = true;
				thrice++;
			}
		}
		lineMap.clear();
	}
	std::cout << (twice * thrice);
}
