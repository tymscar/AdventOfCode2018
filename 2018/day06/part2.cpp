#include <iostream>
#include <fstream>
#include <vector>
#include <string>

struct point{
	int x, y;
};

int main()
{
	std::ifstream file;
	file.open("input.txt");
	std::vector<point> points;
	std::string lineInTheFile;
	
	point newPoint;

	while (file >> lineInTheFile){
		lineInTheFile.erase(lineInTheFile.size() - 1, 1);
		int x = std::stoi(lineInTheFile);
		file >> lineInTheFile;
		int y = std::stoi(lineInTheFile);
		newPoint.x = x;
		newPoint.y = y;
		points.push_back(newPoint);
	}

	int largestX = 0;
	int largestY = 0;

	for (auto p : points){
		if (p.x > largestX)
			largestX = p.x;
		if (p.y > largestY)
			largestY = p.y;
	}

	int numberOfPointsInMiddle = 0;

	for (int i = 0; i <= largestX; i++){
		for (int j = 0; j <= largestY; j++){
			int totalDistance = 0;
			for (auto p: points){
				totalDistance += std::abs(i - p.x) + std::abs(j - p.y);
			}
			if (totalDistance < 10000){
				numberOfPointsInMiddle++;
			}
		}
	}

	std::cout << numberOfPointsInMiddle << std::endl;

}