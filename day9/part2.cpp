#include <iostream>
#include <string>
#include <fstream>
#include <unordered_map>

struct marble{
	unsigned long long pos;
	marble* right;
	marble* left;
};

int main(){
	std::ifstream file;
	file.open("input.txt");
	int nrPlayers;
	unsigned long long lastMarble;
	std::unordered_map<int,unsigned long long> score;

	std::string line;

	file >> line;
	nrPlayers = std::stoi(line);
	file >> line >> line >> line >> line >> line >> line;
	lastMarble = std::stoi(line);
	lastMarble = lastMarble * 100;
	file.close();

	for(int i=1; i<=nrPlayers; i++){
		score[i] = 0;
	}

	marble* firstOne = new marble();
	firstOne->pos = 0;
	firstOne->right = firstOne;
	firstOne->left = firstOne;

	marble* currentMarble = firstOne;
	int currentPlayer = 1;
	unsigned long long currentIndex = 1;
	while(currentMarble->pos < lastMarble){

		if(currentIndex % 23 == 0){
			score[currentPlayer] += currentIndex;
			currentMarble = currentMarble->left->left->left->left->left->left;
			score[currentPlayer] += currentMarble->left->pos;
			currentMarble->left = currentMarble->left->left;
			delete(currentMarble->left->right);
			currentMarble->left->right = currentMarble;
		} else {
			marble* newMarble = new marble();
			newMarble->pos = currentIndex;
			marble* left = currentMarble->right;
			marble* right = currentMarble->right->right;
			newMarble->left = left;
			newMarble->right = right;
			left->right = newMarble;
			right->left = newMarble;

			currentMarble = newMarble;
		}
		currentIndex++;

		currentPlayer++;
		if(currentPlayer > nrPlayers)
			currentPlayer = 1;
	}

	unsigned long long highscore = 0;
	for(auto s: score){
		if(s.second > highscore){
			highscore = s.second;
		}
	}

	std::cout << highscore;
}
