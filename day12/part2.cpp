#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

const int generations = 200;
const long long int wantedGeneration = 50000000000;

bool matchesAnyPatch(std::string current, std::vector<std::string> patches){
	for(auto p : patches){
		if(current == p)
			return true;
	}
	return false;
}

int main()
{
	std::ifstream file;
	file.open("input.txt");

	std::string layout;

	std::vector<std::string> growPatches;

	file >> layout >> layout >> layout;

	std::string line;
	while (file >> line) {
		std::string shape = line;
		file >> line >> line;
		std::string result = line;
		if (result[0] != '.')
			growPatches.push_back(shape);
	}

	std::string padding = "";
	int offset = 0;
	for(int i=0;i<generations;i++){
		padding += "..";
		offset += 2;
	}

	layout = padding + layout + padding;

	long long int lastGenerationNum = 0;
	int diff = 0;

	for(int i=1; i<=generations; i++){
		std::string newLayout = layout;
		for(int j=2;j<layout.size()-2;j++){
			std::string currLine = layout.substr(j-2,5);
			if(matchesAnyPatch(currLine, growPatches))
				newLayout[j] = '#';
			else
				newLayout[j] = '.';
		}
		layout = newLayout;
		
		long long int score = 0;
		for(int i=0;i<layout.size();i++){
			if(layout[i] == '#'){
				score += (i-offset);
			}
		}
		diff = score - lastGenerationNum;

		std::cout <<i << ": " <<  score << " diff from last gen: " << diff <<std::endl;

		lastGenerationNum = score;
	}

	std::cout << std::endl << lastGenerationNum + ( (wantedGeneration - generations) * diff) << std::endl;



}
