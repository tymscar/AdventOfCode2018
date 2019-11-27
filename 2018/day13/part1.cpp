#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>

enum direction{ left, right, up, down };

struct vec2{
	int x, y;
};

struct cart{
	int id;
	vec2 pos;
	vec2 nextPos;
	direction dir;
	char sign;
	char tileUnder;
	long int turning;
};

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;

	std::vector<int> visited;

	std::vector<std::string> tracks;

	std::vector<cart> carts;

	while (std::getline(file, line)){
		tracks.push_back(line);
	}

	int height = tracks.size();
	int width = tracks[0].size();
	int idForVech = 0;

	// Find the carts
	for (int i = 0; i < height; i++){
		for (int j = 0; j < width; j++){
			if (tracks[i][j] == '<' || tracks[i][j] == '>' || tracks[i][j] == '^' || tracks[i][j] == 'v'){
				cart currentCart;
				currentCart.pos.x = i;
				currentCart.pos.y = j;
				vec2 newPos;
				if (tracks[i][j] == '<'){
					currentCart.sign = '<';
					currentCart.tileUnder = '-';
					newPos.x = i;
					newPos.y = j - 1;
					currentCart.dir = left;
				}
				if (tracks[i][j] == '>'){
					currentCart.sign = '>';
					currentCart.tileUnder = '-';
					newPos.x = i;
					newPos.y = j + 1;
					currentCart.dir = right;
				}
				if (tracks[i][j] == '^'){
					currentCart.sign = '^';
					currentCart.tileUnder = '|';
					newPos.x = i - 1;
					newPos.y = j;
					currentCart.dir = up;
				}
				if (tracks[i][j] == 'v'){
					currentCart.sign = 'v';
					currentCart.tileUnder = '|';
					newPos.x = i + 1;
					newPos.y = j;
					currentCart.dir = down;
				}
				currentCart.nextPos = newPos;
				currentCart.id = idForVech;
				idForVech++;
				currentCart.turning = 0;
				carts.push_back(currentCart);
			}
		}
	}

	bool crash = false;

	int frames = 10;

	while(!crash){ //TICKS
		for (int i = 0; i < height; i++){
			for (int j = 0; j < width; j++){
				if (tracks[i][j] == '<' || tracks[i][j] == '>' || tracks[i][j] == '^' || tracks[i][j] == 'v'){ //found a cart
					cart* currentCart;
					bool changedDir = false;
					for (auto& car : carts){ //reference it
						if (car.pos.x == i && car.pos.y == j){
							currentCart = &car;
							break;
						}
					}

					if (find(visited.begin(), visited.end(), currentCart->id) != visited.end()){
						continue;
					}

					tracks[currentCart->pos.x][currentCart->pos.y] = currentCart->tileUnder;
					currentCart->tileUnder = tracks[currentCart->nextPos.x][currentCart->nextPos.y];
					currentCart->pos = currentCart->nextPos;
					if (currentCart->tileUnder == '<' || currentCart->tileUnder == '>' || currentCart->tileUnder == '^' || currentCart->tileUnder == 'v'){
						currentCart->tileUnder = 'x';
						std::cout << "CRASH: " << currentCart->pos.y << "," << currentCart->pos.x << std::endl;
						tracks[currentCart->pos.x][currentCart->pos.y] = 'X';
						crash = true;
					}
					tracks[currentCart->pos.x][currentCart->pos.y] = currentCart->sign;

					if (currentCart->tileUnder == '\\'){
						if (currentCart->dir == right){
							currentCart->sign = 'v';
							currentCart->dir = down;
						}
						else if (currentCart->dir == left){
							currentCart->sign = '^';
							currentCart->dir = up;
						}
						else if (currentCart->dir == up){
							currentCart->sign = '<';
							currentCart->dir = left;
						}
						else if (currentCart->dir == down){
							currentCart->sign = '>';
							currentCart->dir = right;
						}
					}
					if (currentCart->tileUnder == '/'){
						if (currentCart->dir == right){
							currentCart->sign = '^';
							currentCart->dir = up;
						}
						else if (currentCart->dir == left){
							currentCart->sign = 'v';
							currentCart->dir = down;
						}
						else if (currentCart->dir == up){
							currentCart->sign = '>';
							currentCart->dir = right;
						}
						else if (currentCart->dir == down){
							currentCart->sign = '<';
							currentCart->dir = left;
						}
					}
					if (currentCart->tileUnder == '+'){ // Intersection
						if (currentCart->turning % 3 == 0){ // Turn left
							if (currentCart->dir == right){
								currentCart->sign = '^';
								currentCart->dir = up;
							}
							else if (currentCart->dir == left){
								currentCart->sign = 'v';
								currentCart->dir = down;
							}
							else if (currentCart->dir == up){
								currentCart->sign = '<';
								currentCart->dir = left;
							}
							else if (currentCart->dir == down){
								currentCart->sign = '>';
								currentCart->dir = right;
							}
						}
						if (currentCart->turning % 3 == 2){ // Turn right
							if (currentCart->dir == right){
								currentCart->sign = '^';
								currentCart->dir = down;
							}
							else if (currentCart->dir == left){
								currentCart->sign = 'v';
								currentCart->dir = up;
							}
							else if (currentCart->dir == up){
								currentCart->sign = '<';
								currentCart->dir = right;
							}
							else if (currentCart->dir == down){
								currentCart->sign = '>';
								currentCart->dir = left;
							}
						}
						currentCart->turning++;
					}

					if (currentCart->dir == up){
						currentCart->nextPos.x = currentCart->pos.x - 1;
						currentCart->nextPos.y = currentCart->pos.y;
					}
					if (currentCart->dir == down){
						currentCart->nextPos.x = currentCart->pos.x + 1;
						currentCart->nextPos.y = currentCart->pos.y;
					}
					if (currentCart->dir == left){
						currentCart->nextPos.x = currentCart->pos.x;
						currentCart->nextPos.y = currentCart->pos.y - 1;
					}
					if (currentCart->dir == right){
						currentCart->nextPos.x = currentCart->pos.x;
						currentCart->nextPos.y = currentCart->pos.y + 1;
					}
					visited.push_back(currentCart->id);
				}
			}
		}
		visited.clear();
	}
}
