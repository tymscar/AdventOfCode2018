#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

std::vector<char> adjacentTiles(int ofX, int ofY, std::vector<std::vector<char> > matrix){
	std::vector<char> adjTiles;
	if (ofX > 0)
		adjTiles.push_back(matrix[ofX - 1][ofY]);
	if (ofY > 0)
		adjTiles.push_back(matrix[ofX][ofY - 1]);
	if (ofX < matrix.size() - 1)
		adjTiles.push_back(matrix[ofX + 1][ofY]);
	if (ofY < matrix[0].size() - 1)
		adjTiles.push_back(matrix[ofX][ofY + 1]);

	if (ofX > 0 && ofY > 0)
		adjTiles.push_back(matrix[ofX - 1][ofY - 1]);

	if (ofX > 0 && ofY < matrix[0].size() - 1)
		adjTiles.push_back(matrix[ofX - 1][ofY + 1]);

	if (ofX < matrix.size() - 1 && ofY < matrix[0].size() - 1)
		adjTiles.push_back(matrix[ofX + 1][ofY + 1]);

	if (ofX < matrix.size() - 1 && ofY > 0)
		adjTiles.push_back(matrix[ofX + 1][ofY - 1]);

	return adjTiles;
}

char nextState(int x, int y, std::vector<std::vector<char> > matrix){
	int openAcres = 0;
	int trees = 0;
	int lumberyards = 0;
	for (auto c : adjacentTiles(x, y, matrix)){
		if (c == '.')
			openAcres++;
		if (c == '|')
			trees++;
		if (c == '#')
			lumberyards++;
	}
	if (matrix[x][y] == '.'){
		if (trees >= 3)
			return '|';
		else
			return '.';
	}
	if (matrix[x][y] == '|'){
		if (lumberyards >= 3)
			return '#';
		else
			return '|';
	}
	if (matrix[x][y] == '#'){
		if (trees >= 1 && lumberyards >= 1)
			return '#';
		else
			return '.';
	}
}

void printMatrix(std::vector<std::vector<char> > matrix){
	for (int i = 0; i < matrix.size(); i++){
		for (int j = 0; j < matrix[0].size(); j++){
			std::cout << matrix[i][j];
		}
		std::cout << std::endl;
	}
	std::cout << std::endl << std::endl;
}

int main(){
	std::fstream file;
	file.open("input.txt");
	std::string line;

	std::vector<std::vector<char> > matrix;

	while (file >> line){
		std::vector<char> row;
		for (int i = 0; i < line.size(); i++){
			row.push_back(line[i]);
		}
		matrix.push_back(row);
	}

	int minutes = 0;
	//printMatrix(matrix);
	while (minutes < 10){
		minutes++;
		std::vector<std::vector<char> > newMatrix;
		newMatrix = matrix;
		for (int i = 0; i < matrix.size(); i++){
			for (int j = 0; j < matrix[0].size(); j++){
				newMatrix[i][j] = nextState(i, j, matrix);
			}
		}
		matrix = newMatrix;

		//std::cout << minutes << std::endl;
		//printMatrix(matrix);
	}

	int wood = 0;
	int lum = 0;
	for (int i = 0; i < matrix.size(); i++){
		for (int j = 0; j < matrix[0].size(); j++){
			if (matrix[i][j] == '|')
				wood++;
			if (matrix[i][j] == '#')
				lum++;
		}
	}

	std::cout << wood * lum << std::endl;
}