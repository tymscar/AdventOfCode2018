#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>

struct point{
	int x, y;
	char letter;
};

int main()
{
	std::ifstream file;
	file.open("input.txt");
	std::vector<point> points;
	std::vector<char> infiniteChars;
	std::string lineInTheFile;
	std::unordered_map<char, int> area;
	std::vector< std::vector<char> > matrix;
	
	point newPoint;
	char letter = char(96);
	while (file >> lineInTheFile){
		letter += 1;
		lineInTheFile.erase(lineInTheFile.size() - 1, 1);
		int x = std::stoi(lineInTheFile);
		file >> lineInTheFile;
		int y = std::stoi(lineInTheFile);
		newPoint.x = x;
		newPoint.y = y;
		newPoint.letter = letter;
		points.push_back(newPoint);
		area[letter] = 0;
	}

	int largestX = 0;
	int largestY = 0;

	for (auto p : points){
		if (p.x > largestX)
			largestX = p.x;
		if (p.y > largestY)
			largestY = p.y;
	}

	for (int i = 0; i <= largestX; i++){
		std::vector<char> row;
		for (int j = 0; j <= largestY; j++){
			char closestLetter;
			int distance = INT_MAX;
			for (auto p: points){
				if (std::abs(i - p.x) + std::abs(j - p.y) < distance){
					distance = std::abs(i - p.x) + std::abs(j - p.y);
					closestLetter = p.letter;
				}
			}
			for (auto p : points){
				if (((std::abs(i - p.x) + std::abs(j - p.y)) == distance) && (p.letter != closestLetter)){
					closestLetter = '.';
				}
			}
			if (closestLetter != '.'){
				area[closestLetter]++;
			}
			row.push_back(closestLetter);
		}
		matrix.push_back(row);
	}

	for (int i = 0; i <= largestX; i++){
			infiniteChars.push_back(matrix[i][0]);
			infiniteChars.push_back(matrix[i][largestY]);
	}
	for (int i = 0; i <= largestY; i++){
			infiniteChars.push_back(matrix[0][i]);
			infiniteChars.push_back(matrix[largestX][i]);
	}


	int biggestArea = 0;
	for (auto a : area){
		if (std::find(infiniteChars.begin(), infiniteChars.end(), a.first) == infiniteChars.end()){
			if (a.second > biggestArea)
				biggestArea = a.second;
		}
	}

	std::cout << biggestArea;
}
