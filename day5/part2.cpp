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

bool removeOneUnit(std::string& polymer, int unit){
	bool didSomething = false;
	for(int i=0;i<polymer.size();i++){
		int polint = int(polymer[i]);
		if((polint == unit) || (polint == (unit - 32)) || (polint == (unit + 32))){
			didSomething = true;
			polymer.erase(i,1);
		}
	}
	return didSomething;
}

int main(){
	std::ifstream inputFileStream;
	inputFileStream.open("input.txt");
	std::string polymer;
	inputFileStream >> polymer;
	int shortest = polymer.size();
	for(int i=65; i<=91; i++){
		std::string tempPoly = polymer;
		while(removeOneUnit(tempPoly, i));
		while(canReducePolymer(tempPoly));
		if(tempPoly.size() < shortest){
			shortest = tempPoly.size();
		}
	}

	std::cout << shortest << std::endl; 
}
