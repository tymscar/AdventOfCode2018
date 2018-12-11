#include <iostream>
#include <string>

const int INPUT = 2568;

struct vec2 {
	int x, y;
};

struct cell {
	int rackID;
	int powerLevel;
};

int main()
{
	cell matrix[301][301];
	for (int i = 1; i < 301; i++) {
		for (int j = 1; j < 301; j++) {
			matrix[i][j].rackID = 10 + i;
			matrix[i][j].powerLevel = (matrix[i][j].rackID * j);
			matrix[i][j].powerLevel += INPUT;
			matrix[i][j].powerLevel *= matrix[i][j].rackID;
			if (matrix[i][j].powerLevel < 100)
				matrix[i][j].powerLevel = 0;
			else {
				std::string num = std::to_string(matrix[i][j].powerLevel);
				matrix[i][j].powerLevel = num[num.size()-3] - '0';
			}
			matrix[i][j].powerLevel -= 5;
		}
	}
	
	long int bestScore = INT_MIN;
	int bestSize;
	vec2 bestPos;
	for (int sizeOfSquare = 1; sizeOfSquare <= 300; sizeOfSquare++) {
		for (int i = 1; i < 301 - (sizeOfSquare - 1); i++) {
			for (int j = 1; j < 301 - (sizeOfSquare - 1); j++) {
				long score = 0;
				for (int k = 0; k < sizeOfSquare; k++) {
					for (int l = 0; l < sizeOfSquare; l++) {
						score += matrix[i + k][j + l].powerLevel;
					}
				}
				if (score > bestScore) {
					bestScore = score;
					bestPos.x = i;
					bestPos.y = j;
					bestSize = sizeOfSquare;
				}
			}
		}
	}
	


	std::cout << bestPos.x << "," << bestPos.y << "," << bestSize;
}