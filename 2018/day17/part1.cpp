#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

struct vec2{
	int x, y;
};

struct clay{
	vec2 pos;
};

struct drip{
	vec2 pos;
	std::vector<vec2> visited;
};


void printMap( std::vector<std::vector<char> > matrix){
	for(int i=0; i< matrix.size(); i++){
		for(int j = 0; j < matrix[0].size(); j++){
			std::cout << matrix[i][j] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl << std::endl;
}


int main(){
	std::fstream file;
	file.open("input.txt");
	std::string line;

	std::vector<clay*> clays;

	while (file >> line){
		bool startingx;
		int xmin, xmax, ymin, ymax;
		if (line[0] == 'x'){
			xmin = std::stoi(line.substr(2, line.size() - 2));
			xmax = xmin;
			startingx = true;
		}
		if (line[0] == 'y') {
			ymin = std::stoi(line.substr(2, line.size() - 2));
			ymax = ymin;
			startingx = false;
		}
		file >> line;
		if (line[0] == 'x'){
			int i;
			for (i = 2; line[i] != '.'; i++);
			xmin = std::stoi(line.substr(2, i - 2));
			xmax = std::stoi(line.substr(i + 2, line.size() - i - 2));
		}
		if (line[0] == 'y') {
			int i;
			for (i = 2; line[i] != '.'; i++);
			ymin = std::stoi(line.substr(2, i - 2));
			ymax = std::stoi(line.substr(i + 2, line.size() - i - 2));
		}

		if (startingx){
			for (int i = ymin; i <= ymax; i++){
				clay* currentClay = new clay();
				currentClay->pos.x = xmin;
				currentClay->pos.y = i;
				//Check if duplicate
				bool dupl = false;
				for(auto c: clays){
					if(c->pos.x == currentClay->pos.x && c->pos.y == currentClay->pos.y)
						dupl = true;
				}
				if(!dupl)
					clays.push_back(currentClay);
			}
		}
		else {
			for (int i = xmin; i <= xmax; i++){
				clay* currentClay = new clay();
				currentClay->pos.x = i;
				currentClay->pos.y = ymin;
				//Check if duplicate
				bool dupl = false;
				for(auto c: clays){
					if(c->pos.x == currentClay->pos.x && c->pos.y == currentClay->pos.y)
						dupl = true;
				}
				if(!dupl)
					clays.push_back(currentClay);
			}
		}
	}

	std::vector< std::vector<char> > matrix;

	int minx = 500; // 500, 0 is where the spring is
	int miny = 0;
	int maxx = INT_MIN;
	int maxy = INT_MIN;
	for(auto c: clays){
		if(c->pos.x < minx)
			minx = c->pos.x;
		if(c->pos.x > maxx)
			maxx = c->pos.x;
		if(c->pos.y > maxy)
			maxy = c->pos.y;
	}
	minx--;
	maxx++;
	maxy++;

	for(int i=miny; i<= maxy; i++){
		std::vector<char> column;
		for(int j=minx; j<= maxx; j++){
			column.push_back('.');
		}
		matrix.push_back(column);
	}

	matrix[0 - miny][500- minx] = '+';
	for(auto c: clays){
		matrix[c->pos.y - miny][c->pos.x - minx] = '#';
	}

	std::vector<vec2> flowPositions;
	vec2 startpos;
	startpos.x = 500;
	startpos.y = 0;
	flowPositions.push_back(startpos);

	int stop;

	std::vector<vec2> backup;
	std::unordered_map<int, int> spawnedFromThisDepth;
	bool breakNextTurn = false;

	bool anythingChanged = true;
	while(anythingChanged || backup.size() > 0){
		if(anythingChanged == false){
			flowPositions = backup;
			backup.clear();
		} else {
			anythingChanged = false;
		}	
		if(breakNextTurn)
			break;
		
		for(vec2 poz : flowPositions){
			drip* drop = new drip;
			drop->pos = poz;
			if(spawnedFromThisDepth[poz.y] >= maxy)
				breakNextTurn = true;
			else
				spawnedFromThisDepth[poz.y]++;
			bool stopped = false;
			while(!stopped){
				if(drop->pos.y + 1 <= maxy){
					stopped = true;
					if((matrix[drop->pos.y - miny + 1][drop->pos.x - minx] == '.' || matrix[drop->pos.y - miny + 1][drop->pos.x - minx] == '|')){
						stopped = false;
						matrix[drop->pos.y - miny][drop->pos.x - minx] = '|';
						drop->pos.y += 1;
						//priintMap(matrix);
					} else { // daca nu mai poate pica, o ia la dreapta sau stanga
						bool hasDropLeft = false;
						bool hasDropRight = false;
						vec2 limitLeft, limitRight;
						vec2 probe = drop->pos;
						while(matrix[probe.y -miny][probe.x -minx -1] != '#' && (matrix[probe.y -miny +1][probe.x -minx -1 ] != '.' && matrix[probe.y -miny +1][probe.x -minx -1] != '|')&& (probe.x -1 > minx)){ // While the one to the left is not a wall or a drop
							probe.x--;
						}
						if(matrix[probe.y -miny][probe.x -minx-1] != '#'){
							hasDropLeft = true;
							probe.x -= 1;
							limitLeft = probe;
						} else {
							limitLeft = probe;
						}

						probe = drop->pos; // Now do it to the right
						while(matrix[probe.y -miny][probe.x -minx +1] != '#' && (matrix[probe.y -miny +1][probe.x -minx +1] != '.' && matrix[probe.y -miny +1][probe.x -minx +1] != '|')&& (probe.x + 1 < maxx)){ // While the one to the right is not a wall or a drop
							probe.x++;
						}
						if(matrix[probe.y -miny][probe.x -minx +1] != '#'){
							hasDropRight = true;
							probe.x += 1;
							limitRight = probe;
						} else {
							limitRight = probe;
						}
						int floodedAnything = 0;
						for(int i=limitLeft.x; i<=limitRight.x; i++){
							if(hasDropLeft || hasDropRight){
								if(matrix[drop->pos.y - miny][i - minx] == '.')
									floodedAnything++;
								matrix[drop->pos.y - miny][i - minx] = '|';
							}
							else{
								if(matrix[drop->pos.y - miny][i - minx] == '.')
									floodedAnything++;
								matrix[drop->pos.y - miny][i - minx] = '~';
							}
						}
						if(floodedAnything > 0)
							anythingChanged = true;
						else{
							if(hasDropLeft || hasDropRight)
							{
							//	backup.clear();
								backup.push_back(poz);
								flowPositions.clear();
							}
							if(hasDropLeft){
								anythingChanged = true;
								flowPositions.push_back(limitLeft);
							}
							if(hasDropRight){
								anythingChanged = true;
								flowPositions.push_back(limitRight);
							}
						}

						//std::cout << poz.y <<"/"<<maxy << std::endl;
						//std::cin >> stop;
						//printMap(matrix);
					}
				} else {
					stopped = true;
				}
			}
		}
	}

	long long int waterRelatedTiles = 0;

	for(int i=1; i< matrix.size(); i++){
		for(int j = 0; j < matrix[0].size(); j++){
			if(matrix[i][j] == '|' || matrix[i][j] == '~')
				waterRelatedTiles++;
		}
	}

	//printMap(matrix);


	std::cout << waterRelatedTiles << std::endl;
}
