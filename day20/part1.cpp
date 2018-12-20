#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>

struct vec2 {
	int x,y;
};

struct room {
 	vec2 pos;
	bool n,w,s,e;
	int distanceFromStart;
};

std::vector<std::string> getAllPaths(std::string from){
	std::vector<std::string> allPaths;
	std::vector<std::string> pathsPreDash;
	std::vector<std::string> paths;
	std::string currpath = "";
	paths.push_back(currpath);
	pathsPreDash.push_back(currpath);
	int left = 0;
	int leftInd = 0;
	int rightInd = from.size();
	while(left < from.size()){
		if(from[left] != '('){
			if(from[left] == '|'){ // Problema la | consecutive
				pathsPreDash = paths;
				paths.clear();
				std::string tmp = "";
				paths.push_back(tmp);
				left++;	
			} else{
				for(auto& currentPaths: paths){
					currentPaths += from[left];
					left ++;
				}
			}
		} else {
			leftInd = left+1;
			for(rightInd=from.size() -1; from[rightInd] != ')'; rightInd--);
			
			std::vector<std::string> combinedPaths;
			for(auto& p: getAllPaths(from.substr(leftInd, rightInd-leftInd))){
				for(auto& currentPaths: paths){
					std::string tempPath = currentPaths + p;
					combinedPaths.push_back(tempPath);
				}
			}
			paths = combinedPaths;
			left = rightInd+1;
		}
	}

	for(auto& pat: pathsPreDash)
		allPaths.push_back(pat);
	for(auto& pat: paths)
		allPaths.push_back(pat);
	return allPaths;
}

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string input;
	file >> input;
	file.close();

	std::vector<std::string> allPaths;
	std::vector<room*> rooms;
	room* start = new room();
	start->pos.x = 0;
	start->pos.y = 0;
	start->n = nullptr;
	start->s = nullptr;
	start->w = nullptr;
	start->e = nullptr;
	start->distanceFromStart = 0;

	vec2 currPos;
	currPos.x = 0;
	currPos.y = 0;

	input = input.substr(1, input.size()-2);
	allPaths = getAllPaths(input);
	for(auto& p: allPaths){
		for(int i=0; i<p.size(); i++){
			std::cout << p[i];
		}
		std::cout << std::endl;
	}
}
