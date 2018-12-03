#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct point{
	int x,y;
};

struct patch{
	int id;
	point start;
	point size;
	bool atLeastOneIntersect;
};

int main(){
	int* fabric = new int[1000000];
	std::vector<patch> patches;
	std::ifstream inputFileStream;
	inputFileStream.open("input.txt");
	std::string lineInTheFile, coords, size;
	int elemCheck = 0;
	patch currentPatch;
	while(inputFileStream >> lineInTheFile){
		patch currentPatch;
		if(elemCheck % 4 == 0){
			lineInTheFile.erase(0, 1);
			currentPatch.id = std::stoi(lineInTheFile);
		}
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
			currentPatch.atLeastOneIntersect = false;
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
	for(auto& p: patches){
		for(int i=p.start.x; i< p.start.x + p.size.x; i++){
			for(int j=p.start.y; j< p.start.y + p.size.y; j++){
				if(fabric[i * 1000 + j] >= 2)
					p.atLeastOneIntersect = true;
			}
		}
		if(p.atLeastOneIntersect == false)
			std::cout << p.id << std::endl;
	}
}
