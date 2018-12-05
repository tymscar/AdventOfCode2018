#include <iostream>
#include <fstream>
#include <string>

bool canReducePolymer(std::string& polymer){
	bool didSomething = false;
	for(int i=0;i<polymer.size();i++){
		if((int(polymer[i]) + 32) == int(polymer[i+1]) || (int(polymer[i]) - 32) == int(polymer[i+1])){
			polymer.erase(i,2);
			didSomething = true;
		}	
	}
	return didSomething;
}

int main(){
	std::ifstream inputFileStream;
	inputFileStream.open("input.txt");
	std::string polymer;
	inputFileStream >> polymer;
	while(canReducePolymer(polymer)){
	};
	std::cout << polymer.size();
}
