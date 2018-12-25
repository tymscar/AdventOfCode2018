#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct vec4{
	int x,y,z,t;
};

bool mergeGroups(std::vector<std::vector<vec4*>*>& constellations){
}

int main(){
	std::ifstream input;
	input.open("input.txt");
	std::string line;

	std::vector<std::vector<vec4*>* > constelations;
	std::vector<vec4*>* firstconstelation = new std::vector<vec4*>;
	vec4* firstStar = new vec4;

	getline(input, line, ',');
	firstStar->x = std::stoi(line);
	getline(input, line, ',');
	firstStar->y = std::stoi(line);
	getline(input, line, ',');
	firstStar->z = std::stoi(line);
	getline(input, line) ;
	firstStar->t = std::stoi(line);
	

	firstconstelation->push_back(firstStar);
	constelations.push_back(firstconstelation);
	
	while(getline(input, line, ','))
	{
		vec4* currStar = new vec4;
		currStar->x = std::stoi(line);		
		getline(input, line, ',');
		currStar->y = std::stoi(line);
		getline(input, line, ',');
		currStar->z = std::stoi(line);
		getline(input, line) ;
		currStar->t = std::stoi(line);
		
		bool matchesAConst = false;
		for(auto& c : constelations){
			for(auto& s : *c){
				if((std::abs(s->x - currStar->x) + std::abs(s->y - currStar->y) + std::abs(s->z - currStar->z) + std::abs(s->t - currStar->t)) <= 3 ){
					matchesAConst = true;
					c->push_back(currStar);
				}
			}
		}
		if(matchesAConst ==false){
			std::vector<vec4*>* newConst = new std::vector<vec4*>;
			newConst->push_back(currStar);
			constelations.push_back(newConst);
		}
	}



	for(auto& c: constelations){
		std::cout << "Constelation: " << std::endl;
		for(auto& s: *c){
			std::cout << s->x <<","<<s->y<<","<<s->z<<","<<s->t<<std::endl;
		}
		std::cout << std::endl;
	}
	std::cout << std::endl << std::endl << constelations.size();

	input.close();
}
