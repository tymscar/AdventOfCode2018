#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool found(std::vector<int>& these, std::vector<int>& here){
	if(here.size() > these.size()){
		for(int i=here.size() - (these.size() + 1); i<here.size();i++){
			if(here[i] == these[0] && here.size() > i + these.size()){
				bool found = true;
				for(int j=0;j<these.size();j++){
					if(here[i+j] != these[j])
						found = false;
				}
				if(found)
					return true;
			}
		}
	}
	
	return false;
}

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string input;
	file >> input;
	file.close();

	std::vector<int> recipes, inputRecipes;
	
	recipes.push_back(3);
	recipes.push_back(7);

	for(int i=0; i<input.length(); i++){
		std::string s(1, input[i]);
		inputRecipes.push_back(std::stoi(s));
	}

	int firstElf = 0;
	int secondElf = 1;

	long long int nrOfRecipes = 2;

	while(!found(inputRecipes, recipes)){
		int sum = recipes[firstElf] + recipes[secondElf]; 
		if(sum > 9){
			nrOfRecipes++;
			recipes.push_back(sum/10);
		}
		nrOfRecipes++;
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
		//std::cout << recipes.size() <<" " <<answerStartingPos + 10 << std::endl;
		//std::cout <<nrOfRecipes<<std::endl;
	}

	std::cout << "Found " << input << " after " << (nrOfRecipes - input.size()) - 1 << std::endl;
}
