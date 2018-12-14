#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string input;
	file >> input;
	file.close();

	int answerStartingPos = std::stoi(input);

	std::vector<int> recipes;
	
	recipes.push_back(3);
	recipes.push_back(7);


	int firstElf = 0;
	int secondElf = 1;


	while(recipes.size() < (10 + answerStartingPos)){
		int sum = recipes[firstElf] + recipes[secondElf];
		if(sum > 9){
			recipes.push_back(sum/10);
		}
		recipes.push_back(sum%10);
		int advanceFirst = 1 + recipes[firstElf];
		int advanceSecond = 1 + recipes[secondElf];
		for(int i=0; i<advanceFirst; i++){
			firstElf++;
			if(firstElf >= recipes.size())
				firstElf = 0;
		}
		for(int i=0; i<advanceSecond; i++){
			secondElf++;
			if(secondElf >= recipes.size())
				secondElf = 0;
		}
	}

	for(int i=0;i<10;i++){
		std::cout << recipes[answerStartingPos + i];
	}
}
