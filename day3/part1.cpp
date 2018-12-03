#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct point{
	int x,y;
};

struct patch{
	point start;
	point size;
};

int main(){
	int* fabric = new int[1000000];
	std::vector<patch> patches;
	std::ifstream inputFileStream;
	inputFileStream.open("input.txt");
	std::string lineInTheFile, coords, size;
	int elemCheck = 0;
	patch currentPatch;
	int howManyOverlaps = 0;
	while(inputFileStream >> lineInTheFile){
		patch currentPatch;
		if((elemCheck + 2) % 4 == 0){
			std::string x = "";
			std::string y = "";
			int i = 0;
			while(lineInTheFile[i] != ','){
				x += lineInTheFile[i];
				i++;
			}
			i++;
			while(lineInTheFile[i] != ':'){
				y += lineInTheFile[i];
				i++;
			}
			currentPatch.start.x = std::stoi(x);
			currentPatch.start.y = std::stoi(y);
		}
		if((elemCheck + 1) % 4 == 0){
			std::string x = "";
			std::string y = "";
			int i = 0;
			while(lineInTheFile[i] != 'x'){
				x += lineInTheFile[i];
				i++;
			}
			i++;
			while(i < lineInTheFile.size()){
				y += lineInTheFile[i];
				i++;
			}
			currentPatch.size.x = std::stoi(x);
			currentPatch.size.y = std::stoi(y);
			patches.push_back(currentPatch);
		}
		elemCheck++;
	}


	for(auto& p: patches){
		for(int i=p.start.x; i< p.start.x + p.size.x; i++){
			for(int j=p.start.y; j< p.start.y + p.size.y; j++){
				fabric[i * 1000 + j]++;
			}
		}
	}
	for(int i=0; i<1000; i++)
		for(int j=0; j<1000; j++){
			if(fabric[i*1000 + j] >=2)
				howManyOverlaps++;
		}
	std::cout << howManyOverlaps << std::endl;
}
