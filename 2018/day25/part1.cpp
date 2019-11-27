#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct vec4{
	int x,y,z,t;
};

void removeEmptyConstellations(std::vector<std::vector<vec4*>*>& constellations){
	std::vector<std::vector<vec4*>*> newMap;

	for(auto c: constellations){
		if(c->size() > 0)
			newMap.push_back(c);
	}

	constellations = newMap;
}

bool mergeGroups(std::vector<std::vector<vec4*>*>& constellations){
	for(auto& c1: constellations){
		for(auto& c2: constellations){
			if(c1 != c2){
				bool merge = false;
				for(auto& currStar: *c1){
					for(auto& s: *c2){
						if((std::abs(s->x - currStar->x) + std::abs(s->y - currStar->y) + std::abs(s->z - currStar->z) + std::abs(s->t - currStar->t)) <= 3 ){
							merge = true;
						}
					}
				}
				
				if(merge){
					for(auto& s: *c2)
						c1->push_back(s);
					c2->clear();
					return true;
				}
			}
		}
	}
	return false;
}

int main(){
	std::ifstream input;
	input.open("input.txt");
	std::string line;

	std::vector<std::vector<vec4*>* > constelations;

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
		
		std::vector<vec4*>* constel = new std::vector<vec4*>;
		constel->push_back(currStar);
		constelations.push_back(constel);
	}

	while(mergeGroups(constelations));

	removeEmptyConstellations(constelations);

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
