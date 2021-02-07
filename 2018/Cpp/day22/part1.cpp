#include <iostream>
#include <string>
#include <fstream>
#include <vector>

struct vec2{
	int x,y;
};

struct region{
	long long int type;
	long long int errosionLevel;
	long long int geoIndex;
};

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;

	int depth;
	vec2 targetPos;
	std::vector<std::vector<region*> > map;

	file >> line >> line; 

	depth = std::stoi(line);
	file >> line >> line;
	file.close();
	{
		int i;
		std::string temp = " ";
		std::vector<int> pos;
		for(i = 0; i< line.size(); i++){
			if(line[i] != ',')
				temp += line[i];
			else {
				pos.push_back(std::stoi(temp));
				temp = " ";
			}
		}
		pos.push_back(std::stoi(temp));
		targetPos.x = pos[0];
		targetPos.y = pos[1];
	}

	for(int i=0; i<=targetPos.x; i++){
		std::vector<region*> row;
		for(int j=0; j<=targetPos.y; j++){
			region* curr = new region;
			if(i==0 && j==0)
				curr->geoIndex = 0;
			if(i==0 && j!=0){
				curr->geoIndex = j * 48271;
			}
			if(j==0 && i!=0){
				curr->geoIndex = i * 16807;
			}
			//if(i !=0 && j!= 0)
			//§	curr->geoIndex = map[i-1][j]->errosionLevel * map[i][j-1]->errosionLevel;
			if(i==targetPos.x && j==targetPos.y)
				curr->geoIndex = 0;
			curr->errosionLevel = (curr->geoIndex + depth) % 20183;
			curr->type = curr->errosionLevel % 3;			
			row.push_back(curr);
		}
		map.push_back(row);
	}

	
	for(int i=1; i<=targetPos.x; i++){
		for(int j=1;j<=targetPos.y;j++){
			region* curr = map[i][j];
			curr->geoIndex = map[i-1][j]->errosionLevel * map[i][j-1]->errosionLevel;
			curr->errosionLevel = (curr->geoIndex + depth) % 20183;
			curr->type = curr->errosionLevel % 3;
		}
	}
	

	long int risk = 0;
	for(int i=0; i<=targetPos.y;i++){
		for(int j=0; j<=targetPos.x; j++){
			if(map[j][i]->type == 0){
				std::cout << ".";
			}
			if(map[j][i]->type == 1){
				std::cout << "=";
			}
			if(map[j][i]->type == 2){
				std::cout << "|";
			}	
			risk += map[j][i]->type;
		}
		std::cout << std::endl;
	}

	risk -= map[0][0]->type;
	risk -= map[targetPos.x][targetPos.y]->type;

	std::cout << risk << std::endl;
	
}
