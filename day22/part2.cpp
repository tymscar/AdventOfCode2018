#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <unordered_map>

struct vec2{
	int x,y;
};

std::vector<int> requires(int type){
	// 0 - neither
	// 1 - torch
	// 2 - climbing eq
	std::vector<int> req;
	if(type == 0){
		req.push_back(1);
		req.push_back(2);
	}
	if(type == 1){
		req.push_back(0);
		req.push_back(2);
	}
	if(type == 2){
		req.push_back(0);
		req.push_back(1);
	}
	return req;
}

struct region{
	long long int type;
	long long int errosionLevel;
	long long int geoIndex;
};

int twoDtoOneD(int x, int y, std::vector<std::vector<region*> >& map){
	return (x * map[0].size() + y);
}

vec2 oneDtoTwoD(int pos, std::vector<std::vector<region*> >& map){
	vec2 pos2d;
	pos2d.y = pos % map[0].size();
	pos2d.x = (pos - pos2d.y) / map[0].size();
	return pos2d;
}

int lowestFscore(std::vector<int> openset, std::unordered_map<int, int>& fscore){
	int lowscore = INT_MAX;
	int pos;
	for(auto& n : openset){
		if(fscore[n] < lowscore){
			lowscore = fscore[n];
			pos = n;
		}
	}
	return pos;
}

int hereustic(int start, int end, std::vector<std::vector<region*> >& map){
	int distance = 0;

	vec2 posS = oneDtoTwoD(start, map);
	vec2 posE = oneDtoTwoD(end, map);

	distance += std::abs(posS.x - posE.x);
	distance += std::abs(posS.y - posE.y);

	return distance;
}

std::vector<int> neighboursOf(int point, std::vector<std::vector<region*> >& map){
	std::vector<int> nei;
	vec2 pos = oneDtoTwoD(point, map);

	if(pos.x > 0)
		nei.push_back(twoDtoOneD(pos.x - 1, pos.y, map));
	if(pos.y > 0)
		nei.push_back(twoDtoOneD(pos.x, pos.y -1, map));
	if(pos.x + 1 < map.size())
		nei.push_back(twoDtoOneD(pos.x + 1, pos.y, map));
	if(pos.y + 1 < map[0].size())
		nei.push_back(twoDtoOneD(pos.x, pos.y + 1, map));

	return nei;
}

std::vector<int> constructPath(int start, int end, std::unordered_map<int, int>& cameFrom, std::unordered_map<int, int> gscore){
	std::vector<int> path;
	int time = 0;
	while(end != start){
		path.push_back(end);
		end = cameFrom[end];
		time += gscore[end];
	}
	std::cout << time << std::endl;
	//path.push_back(end);
	return path;
}

std::vector<int> astar(int start, int end, std::vector<std::vector<region*> >& map, int tool){
	std::vector<int> closedSet;
	std::vector<int> path;

	std::vector<int> openSet;
	openSet.push_back(start);

	std::unordered_map<int, int> cameFrom;

	std::unordered_map<int, int> gscore;
	for(int i=0;i<map.size();i++){
		for(int j=0;j<map[0].size();j++){
			gscore[twoDtoOneD(i, j, map)] = 999999;
		}
	}
	gscore[start] = 0;

	std::unordered_map<int, int> fscore;
	for(int i=0;i<map.size();i++){
		for(int j=0;j<map[0].size();j++){
			fscore[twoDtoOneD(i, j, map)] = 999999;
		}
	}
	fscore[start] = hereustic(start, end, map);

	while(!openSet.empty()){
		int current = lowestFscore(openSet, fscore);
		if(current == end){
			path = constructPath(start, end, cameFrom, gscore);
			return path;
		}
		openSet.erase(std::remove(openSet.begin(), openSet.end(), current), openSet.end());
		closedSet.push_back(current);
		for(int neigh : neighboursOf(current, map)){
			if(std::find(closedSet.begin(), closedSet.end(), neigh) != closedSet.end())
				continue;
			int cost;
			std::vector<int> requiredNei = requires(map[oneDtoTwoD(neigh,map).x][oneDtoTwoD(neigh,map).y]->type);
			std::vector<int> requiredCurr = requires(map[oneDtoTwoD(current,map).x][oneDtoTwoD(current,map).y]->type);

			if(tool == requiredNei[0] || tool == requiredNei[1]){
				cost = 1;
			} else {
				std::cout << "SWITH    from " << tool << " to ";
				cost = 8;
				int newTool = 0;
				bool notInBoth = false;
				do{
					notInBoth = false;
					if(!(newTool == requiredNei[0] || newTool == requiredNei[1]))
						notInBoth = true;
					if(!(newTool == requiredCurr[0] || newTool == requiredCurr[1]))
						notInBoth = true;
					if(notInBoth)
						newTool++;
				}while(notInBoth);
				tool = newTool;
				std::cout << tool << "    from tile " << oneDtoTwoD(current, map).x << "," << oneDtoTwoD(current, map).y <<"["<<map[oneDtoTwoD(current,map).x][oneDtoTwoD(current,map).y]->type << "]  to tile " << oneDtoTwoD(neigh,map).x << "," << oneDtoTwoD(neigh,map).y <<"[" << map[oneDtoTwoD(neigh,map).x][oneDtoTwoD(neigh,map).y]->type << "]" <<std::endl;
			}

			int tempGscore = gscore[current] + cost;
			if(!(std::find(openSet.begin(), openSet.end(), neigh) != openSet.end()) && cost != 9999999)
				openSet.push_back(neigh);
			else if(tempGscore > gscore[neigh])
				continue;
			cameFrom[neigh] = current;
			gscore[neigh] = tempGscore;
			fscore[neigh] = gscore[neigh] + hereustic(neigh, end, map);
		}
	}

	return path;
}


int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;

	int currTool = 1; 
	// 0 - neither
	// 1 - torch
	// 2 - climbing eq
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

	for(int i=0; i<=targetPos.x * 2; i++){
		std::vector<region*> row;
		for(int j=0; j<=targetPos.y * 2; j++){
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

	
	for(int i=1; i<=targetPos.x * 2; i++){
		for(int j=1;j<=targetPos.y * 2;j++){
			region* curr = map[i][j];
			curr->geoIndex = map[i-1][j]->errosionLevel * map[i][j-1]->errosionLevel;
			curr->errosionLevel = (curr->geoIndex + depth) % 20183;
			curr->type = curr->errosionLevel % 3;
		}
	}
	

	long int risk = 0;
	
	for(int i=0; i<=targetPos.y*2;i++){
		for(int j=0; j<=targetPos.x*2; j++){
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

//	std::cout << risk << std::endl;

	for(auto a: astar(twoDtoOneD(0,0,map), twoDtoOneD(targetPos.x,targetPos.y,map), map, 1)){
		std::cout << oneDtoTwoD(a,map).x <<", " <<  oneDtoTwoD(a,map).y << std::endl;
	}
}
