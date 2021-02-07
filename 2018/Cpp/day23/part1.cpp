#include <iostream>
#include <fstream>
#include <vector>
#include <string>

struct vec2{
	int x,y,z;
};

struct nanobot{
	int radius;
	vec2 pos;
};

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string input;

	std::vector<nanobot*> nanobots;

	while(file >> input){

		nanobot* currbot = new nanobot;

		std::vector<int> xyz;
		std::string temp = " ";
		int ii = 5;
		while(input[ii] != '>'){
			if(input[ii] == ','){
				xyz.push_back(std::stoi(temp));
				temp = " ";
			} else {
				temp += input[ii];
			}
			ii++;
		}
		xyz.push_back(std::stoi(temp));

		currbot->pos.x = xyz[0];
		currbot->pos.y = xyz[1];
		currbot->pos.z = xyz[2];

		file >> input;

		currbot->radius = std::stoi(input.substr(2,(input.size() - 2)));


		nanobots.push_back(currbot);
	}

	int strongestSignal = INT_MIN;
	nanobot* strongestNanobot = new nanobot;


	for(int i=0; i<nanobots.size(); i++){
		if(nanobots[i]->radius > strongestSignal){
			strongestSignal = nanobots[i]->radius;
			strongestNanobot = nanobots[i];
		}
	}

	int botsInRange = 0;

	for(int i=0; i<nanobots.size(); i++){
		int distance = 0;
		distance += std::abs(nanobots[i]->pos.x - strongestNanobot->pos.x);
		distance += std::abs(nanobots[i]->pos.y - strongestNanobot->pos.y);
		distance += std::abs(nanobots[i]->pos.z - strongestNanobot->pos.z);

		if(distance <= strongestSignal){
			botsInRange++;
		}
	}

	std::cout << botsInRange << std::endl;
}
