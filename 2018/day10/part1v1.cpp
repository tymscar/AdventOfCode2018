#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

struct vec2{
	int x, y;
};

struct lamp{
	vec2 pos;
	vec2 vel;
};

int howManyEmptyRows(std::vector<std::vector<char> >& matrix){
	int linesEmpty = 0;

	for (int j = 0; j < matrix[0].size(); j++){
		bool empty = true;
		for (int i = 0; i < matrix.size(); i++){
			if (matrix[i][j] == '#'){
				empty = false;
			}
		}
		if (empty)
			linesEmpty++;
	}
	return linesEmpty;
}

void printMatrix(std::vector<std::vector<char> >& matrix, int sx, int sy, int bx, int by){
	for (int j = 0; j < matrix[0].size(); j++){
		for (int i = 0; i < matrix.size(); i++){
			std::cout << matrix[i][j];
		}
		std::cout << std::endl;
	}

}

void redrawMatrix(std::vector<std::vector<char> >& matrix, int sx, int sy, int bx, int by, std::vector<lamp>& lamps){
	for (int i = 0; i < matrix.size(); i++){
		for (int j = 0; j < matrix[0].size(); j++){
			matrix[i][j] = '.';
		}
	}

	for (auto l : lamps){
		matrix[l.pos.x - sx][l.pos.y - sy] = '#';
	}
}

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;

	std::vector<std::vector<char> > matrix;


	std::vector<lamp> lamps;
	
	while (std::getline(file,line)){
		lamp currentLamp;
		std::istringstream iss(line);
		std::string word;
		iss >> word;
		if (word[word.size()-1] == ','){
			word.erase(0, 10);
			word.erase(word.size() - 1, 1);	
		}
		else {
			iss >> word;
			word.erase(word.size() - 1, 1);
		}
		currentLamp.pos.x = std::stoi(word);
		iss >> word;
		word.erase(word.size() - 1, 1);
		currentLamp.pos.y = std::stoi(word);
		iss >> word;
		if (word[word.size() - 1] == ','){
			word.erase(0, 10);
			word.erase(word.size() - 1, 1);
		}
		else {
			iss >> word;
			word.erase(word.size() - 1, 1);
		}
		currentLamp.vel.x = std::stoi(word);
		iss >> word;
		word.erase(word.size() - 1, 1);
		currentLamp.vel.y = std::stoi(word);

		lamps.push_back(currentLamp);
	}
	
	int smallestx = INT_MAX;
	int smallesty = INT_MAX;
	int biggestx = INT_MIN;
	int biggesty = INT_MIN;

	for (auto l : lamps){
		if (l.pos.x < smallestx)
			smallestx = l.pos.x;
		if (l.pos.x > biggestx)
			biggestx = l.pos.x;
		if (l.pos.y < smallesty)
			smallesty = l.pos.y;
		if (l.pos.y > biggesty)
			biggesty = l.pos.y;
	}

	
	std::vector<char> row;
	row.reserve(abs(smallesty) + biggesty + 1);
	for (int j = 0; j <= abs(smallesty) + biggesty; j++){
		row.push_back('.');
	}
	for (int i = smallestx; i <= biggestx; i++){
		std::cout << i << "/" << biggestx << std::endl;
		matrix.push_back(row);
	}

	std::cout << "Finished creating the matrix" << std::endl;


	redrawMatrix(matrix, smallestx, smallesty, biggestx, biggesty, lamps);
	
	std::cout << "Finished populating the matrix" << std::endl;

	int oldFreeLines = howManyEmptyRows(matrix);
	std::vector<std::vector<char> > finalMatrix;
	while (howManyEmptyRows(matrix) >= oldFreeLines){
		for (auto& l : lamps){
			l.pos.x += l.vel.x;
			l.pos.y += l.vel.y;
		}
		oldFreeLines = howManyEmptyRows(matrix);
		finalMatrix = matrix;
		redrawMatrix(matrix, smallestx, smallesty, biggestx, biggesty, lamps);
		std::cout << "Finished one iteration" << std::endl;
	}

	std::cout << "Printing the result!" << std::endl;

	printMatrix(finalMatrix, smallestx, smallesty, biggestx, biggesty);

	std::cin >> oldFreeLines;
}
