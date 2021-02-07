#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <cmath>


struct vec2{
	int x, y;
};

void resetMap(std::vector<std::vector<char> >& map){
	for(int i=0;i<map.size();i++){
		for(int j=0; j<map[0].size(); j++){
			if(map[i][j] == 'E' || map[i][j] == 'G')
				map[i][j] = '.';
		}
	}
}

void printMap(std::vector<std::vector<char> >& map){
	for(int i=0;i<map.size();i++){
		for(int j=0; j<map[0].size(); j++){
			std::cout << map[i][j];
		}
		std::cout << std::endl;
	}
	std::cout << std::endl << std::endl;
}

int twoDtoOneD(int x, int y, std::vector<std::vector<char> >& map){
	return (x * map[0].size() + y);
}

vec2 oneDtoTwoD(int pos, std::vector<std::vector<char> >& map){
	vec2 pos2d;
	pos2d.y = pos % map[0].size();
	pos2d.x = (pos - pos2d.y) / map[0].size();
	return pos2d;
}

int lowestFscore(std::vector<int> openset, std::unordered_map<int, int>& fscore){
	int lowscore = INT_MAX;
	int pos;
	for(auto& n : openset){
		if(fscore[n] < lowscore){
			lowscore = fscore[n];
			pos = n;
		}
	}
	return pos;
}

int hereustic(int start, int end, std::vector<std::vector<char> >& map){
	int distance = 0;

	vec2 posS = oneDtoTwoD(start, map);
	vec2 posE = oneDtoTwoD(end, map);

	distance += std::abs(posS.x - posE.x);
	distance += std::abs(posS.y - posE.y);

	return distance;
}

std::vector<int> neighboursOf(int point, std::vector<std::vector<char> >& map){
	std::vector<int> nei;
	vec2 pos = oneDtoTwoD(point, map);

	if(pos.x > 0)
		nei.push_back(twoDtoOneD(pos.x - 1, pos.y, map));
	if(pos.y > 0)
		nei.push_back(twoDtoOneD(pos.x, pos.y -1, map));
	if(pos.x + 1 < map.size())
		nei.push_back(twoDtoOneD(pos.x + 1, pos.y, map));
	if(pos.y + 1 < map[0].size())
		nei.push_back(twoDtoOneD(pos.x, pos.y + 1, map));
	
	return nei;
}

std::vector<int> constructPath(int start, int end, std::unordered_map<int, int>& cameFrom){
	std::vector<int> path;
	while(end != start){
		path.push_back(end);
		end = cameFrom[end];
	}
	path.push_back(end);
	return path;
}

std::vector<int> astar(int start, int end, std::vector<std::vector<char> >& map){
	std::vector<int> closedSet;
	std::vector<int> path;

	std::vector<int> openSet;
	openSet.push_back(start);
	
	std::unordered_map<int, int> cameFrom;
	
	std::unordered_map<int, int> gscore;
	for(int i=0;i<map.size();i++){
		for(int j=0;j<map[0].size();j++){
			gscore[twoDtoOneD(i, j, map)] = 999999;
		}
	}
	gscore[start] = 0;

	std::unordered_map<int, int> fscore;
	for(int i=0;i<map.size();i++){
		for(int j=0;j<map[0].size();j++){
			fscore[twoDtoOneD(i, j, map)] = 999999;
		}
	}
	fscore[start] = hereustic(start, end, map);

	while(!openSet.empty()){
		int current = lowestFscore(openSet, fscore);
		if(current == end){
			path = constructPath(start, end, cameFrom);
			return path;
		}
		openSet.erase(std::remove(openSet.begin(), openSet.end(), current), openSet.end());
		closedSet.push_back(current);
		for(int neigh : neighboursOf(current, map)){
			if(std::find(closedSet.begin(), closedSet.end(), neigh) != closedSet.end())
				continue;
			int cost = 9999999;
			if(map[oneDtoTwoD(neigh,map).x][oneDtoTwoD(neigh,map).y] == '.')
				cost = 1;
			int tempGscore = gscore[current] + cost;
			if(!(std::find(openSet.begin(), openSet.end(), neigh) != openSet.end()) && cost != 9999999)
				openSet.push_back(neigh);
			else if(tempGscore > gscore[neigh])
				continue;
			cameFrom[neigh] = current;
			gscore[neigh] = tempGscore;
			fscore[neigh] = gscore[neigh] + hereustic(neigh, end, map);
		}
	}

	return path;
}


int chooseFirst(std::vector<int> fromThis){
	int smallest = INT_MAX;
	for(auto a: fromThis){
		if(a < smallest)
			smallest = a;
	}
	return smallest;
}


struct humanoid{
	vec2 pos;
	int hp;
	int dmg;
	char sign;
	bool elf;
};

humanoid* getHum(int fromPos, std::vector<humanoid*> allHumanoids, std::vector< std::vector<char> >& map){
	for(auto& h : allHumanoids){
		if(h->pos.x == (oneDtoTwoD(fromPos, map)).x && h->pos.y == (oneDtoTwoD(fromPos, map)).y)	
			return h;
	}
}

int main(){
	std::ifstream file;
	file.open("input.txt");
	std::string line;
	
	std::vector< std::vector<char> > map;
	std::vector<humanoid*> allHumanoids;
	std::vector<humanoid*> units;
	std::vector<humanoid*> goblins;
	std::vector<humanoid*> elfs;

	while(std::getline(file, line)){
		std::vector<char> row;
		for(int i=0; i<line.length(); i++){
			row.push_back(line[i]);
		}
		map.push_back(row);
	}

	for(int i=0; i<map.size();i++){
		for(int j=0; j<map[0].size();j++){
			if(map[i][j] == 'E'){
				humanoid* elf = new humanoid;
				elf->pos.x = i;
				elf->pos.y = j;
				elf->hp = 200;
				elf->dmg = 3;
				elf->elf = true;
				elf->sign = 'E';
				units.push_back(elf);
				elfs.push_back(elf);
			}
			if(map[i][j] == 'G'){
				humanoid* goblin = new humanoid;
				goblin->pos.x = i;
				goblin->pos.y = j;
				goblin->hp = 200;
				goblin->dmg = 3;
				goblin->elf = false;
				goblin->sign = 'G';
				units.push_back(goblin);
				goblins.push_back(goblin);
			}
		}
	}

	printMap(map);

	allHumanoids = units;

	bool combatEnded = false;
	int rounds = 0;
	while(!combatEnded){
		std::vector<humanoid*> playedUnits;
		// Find the order of the units to play
		while(units.size() > 0){
			int smallestIndex = INT_MAX;
			humanoid* chosenUnit;
			for(auto& hum : units){
				if(twoDtoOneD(hum->pos.x, hum->pos.y, map) < smallestIndex){
					smallestIndex = twoDtoOneD(hum->pos.x, hum->pos.y, map);
					chosenUnit = hum;
				}
			}
			playedUnits.push_back(chosenUnit);
			units.erase(std::remove(units.begin(), units.end(), chosenUnit), units.end());

			char oppositeSign;
			bool alreadyFought = false;

			// At this point we have the unit
			if(chosenUnit->elf){
				oppositeSign = 'G';
				if(goblins.size() == 0){
					combatEnded = true;
					continue;
				}
			}
			if(chosenUnit->elf == false){
				oppositeSign = 'E';
				if(elfs.size() == 0){
					combatEnded = true;
					continue;
				}
			}

			//If in range of target
			std::vector<int> adjacentEnemies;
			for(auto& neighboursOfUnit : neighboursOf(smallestIndex, map)){
				if(map[oneDtoTwoD(neighboursOfUnit, map).x][oneDtoTwoD(neighboursOfUnit, map).y] == oppositeSign){
					adjacentEnemies.push_back(neighboursOfUnit);
				}
			}
			
			humanoid* target;

			alreadyFought = false;
			// If theres enemies next, attack them
			if(adjacentEnemies.size() > 0){
				alreadyFought = true;
				//If theres an enemy adjacent, target it
				std::vector<int> lowestHealthEnemy;
				int lowHealth = INT_MAX;
				for(auto& adjEn :adjacentEnemies){
					if(getHum(adjEn,allHumanoids, map)->hp == lowHealth){
						lowestHealthEnemy.push_back(adjEn);
					}
					if(getHum(adjEn,allHumanoids, map)->hp < lowHealth){
						lowHealth = getHum(adjEn, allHumanoids, map)->hp;
						lowestHealthEnemy.clear();
						lowestHealthEnemy.push_back(adjEn);
					}
				}
				target = getHum(chooseFirst(lowestHealthEnemy), allHumanoids, map);
				target->hp -= chosenUnit->dmg;
				if(target->hp <=0){ //dies
					map[target->pos.x][target->pos.y] = '.';

					if(std::find(units.begin(), units.end(), target) != units.end())
						units.erase(std::remove(units.begin(), units.end(), target), units.end());

					if(std::find(playedUnits.begin(), playedUnits.end(), target) != playedUnits.end())
						playedUnits.erase(std::remove(playedUnits.begin(), playedUnits.end(), target), playedUnits.end());

					if(std::find(allHumanoids.begin(), allHumanoids.end(), target) != allHumanoids.end())
						allHumanoids.erase(std::remove(allHumanoids.begin(), allHumanoids.end(), target), allHumanoids.end());

					if(std::find(goblins.begin(), goblins.end(), target) != goblins.end())
						goblins.erase(std::remove(goblins.begin(), goblins.end(), target), goblins.end());

					if(std::find(elfs.begin(), elfs.end(), target) != elfs.end())
						elfs.erase(std::remove(elfs.begin(), elfs.end(), target), elfs.end());
				}
			} else { //You can move
				std::vector<int> possiblePointsWhereToMode;
				// The reachable locations
				if(oppositeSign == 'G'){
					for(auto g: goblins){
						for(auto n: neighboursOf(twoDtoOneD(g->pos.x, g->pos.y, map), map)){
							if(map[oneDtoTwoD(n, map).x][oneDtoTwoD(n,map).y] == '.' && astar(smallestIndex, n, map).size() > 0)
								possiblePointsWhereToMode.push_back(n);
						}
					}
				} else {
					for(auto e: elfs){
						for(auto n: neighboursOf(twoDtoOneD(e->pos.x, e->pos.y, map), map)){
							if(map[oneDtoTwoD(n, map).x][oneDtoTwoD(n,map).y] == '.' && astar(smallestIndex, n, map).size() > 0)
								possiblePointsWhereToMode.push_back(n);
						}
					}
				}


				// A* pe toate cele reachable
				// caut cel mai scurt raspuns de la A*
				// daca sunt mai multe, il iau pe cel mai de sus
				// fac a* din nou ca sa vad pasul urmator

				if(possiblePointsWhereToMode.size() > 0){
					std::vector<int> nearestLocationsFromAstar;
					int prais = INT_MAX;
					for(auto pptm: possiblePointsWhereToMode){
						if(astar(smallestIndex, pptm, map).size() > 0){
							if(astar(smallestIndex, pptm, map).size() == prais){
								nearestLocationsFromAstar.push_back(pptm);
							}
							if(astar(smallestIndex, pptm, map).size() < prais){
								prais = astar(smallestIndex, pptm, map).size();
								nearestLocationsFromAstar.clear();
								nearestLocationsFromAstar.push_back(pptm);
							}
						}
					}
					int nearestLocationFromAstar = chooseFirst(nearestLocationsFromAstar);

					std::vector<int> nearestCornerAstar;
					int priz = INT_MAX;
					for(auto corner: neighboursOf(smallestIndex, map)){
						if(map[oneDtoTwoD(corner, map).x][oneDtoTwoD(corner, map).y] == '.'){
							if(astar(corner,nearestLocationFromAstar, map).size() >0){
								if(astar(corner,nearestLocationFromAstar, map).size() == priz){
									nearestCornerAstar.push_back(corner);
								}		
								if(astar(corner, nearestLocationFromAstar, map).size() < priz){
									priz = astar(corner, nearestLocationFromAstar, map).size();
									nearestCornerAstar.clear();
									nearestCornerAstar.push_back(corner);
								}
							}
						}	
					}
					
					vec2 nextPosForCurrent = oneDtoTwoD(chooseFirst(nearestCornerAstar), map);

	//				std::cout <<"Start: " << chosenUnit->pos.x << "," << chosenUnit->pos.y << std::endl;
		//			std::cout <<"End: " << oneDtoTwoD(nearestLocationFromAstar,map).x << "," << oneDtoTwoD(nearestLocationFromAstar, map).y  << std::endl;
					//if(astar(smallestIndex, nearestLocationFromAstar, map).size() > 1){
					//	vec2 nextPosForCurrent = oneDtoTwoD(astar(smallestIndex, nearestLocationFromAstar, map)[astar(smallestIndex, nearestLocationFromAstar, map).size()-2], map);
	//					std::cout <<"Next: " <<  nextPosForCurrent.x << "," << nextPosForCurrent.y << std::endl << std::endl;
						chosenUnit->pos = nextPosForCurrent;
					//}

					/*
					// The target nearest location
					std::vector<int> targetPosForMoveVec;//= oneDtoTwoD(chooseFirst(possiblePointsWhereToMode), map);
					int ieftin = INT_MAX;
					for(auto pozitie: possiblePointsWhereToMode){
						if(hereustic(smallestIndex, pozitie, map) == ieftin){
							targetPosForMoveVec.push_back(pozitie);
						}
						if(hereustic(smallestIndex, pozitie, map) < ieftin){
							ieftin = hereustic(smallestIndex, pozitie, map);
							targetPosForMoveVec.clear();
							targetPosForMoveVec.push_back(pozitie);
						}
					}

					// The literal next position to be on
					vec2 targetPosForMove = oneDtoTwoD(chooseFirst(targetPosForMoveVec), map);
					std::vector<int> listOfNextPositions;
					int smallestCost = INT_MAX;
					for(auto n: neighboursOf(smallestIndex, map)){
							if(map[oneDtoTwoD(n, map).x][oneDtoTwoD(n,map).y] == '.'){ //Should probably just use A*'s answer
								if(hereustic(n, twoDtoOneD(targetPosForMove.x, targetPosForMove.y, map), map) == smallestCost){
									listOfNextPositions.push_back(n);	
								}
								if(hereustic(n, twoDtoOneD(targetPosForMove.x, targetPosForMove.y, map), map) < smallestCost){
									listOfNextPositions.clear();
									listOfNextPositions.push_back(n);
									smallestCost = hereustic(n, twoDtoOneD(targetPosForMove.x, targetPosForMove.y, map), map); 
								}
							}
					}
					*/

//					vec2 nextPosForCurrent = oneDtoTwoD(chooseFirst(listOfNextPositions), map);
					//map[chosenUnit->pos.x][chosenUnit->pos.y] = '.';
//					chosenUnit->pos = nextPosForCurrent;
					//map[chosenUnit->pos.x][chosenUnit->pos.y] = chosenUnit->sign;
					//printMap(map);

				//	std::cout << oneDtoTwoD(smallestIndex, map).x << "," << oneDtoTwoD(smallestIndex, map).y << " will go to ";
				//	std::cout << nextPosForCurrent.x << "," << nextPosForCurrent.y << std::endl << std::endl;
					//std::cout << targetPosForMove.x << "," << targetPosForMove.y << "  " <<possiblePointsWhereToMode.size()<<std::endl << std::endl;
					
				}
			}

			resetMap(map);
			for(auto& pp : playedUnits){
				map[pp->pos.x][pp->pos.y] = pp->sign;
			}
			for(auto& pp : units){
				map[pp->pos.x][pp->pos.y] = pp->sign;
			}

			//Can he attack now?
			adjacentEnemies.clear();
			for(auto& neighboursOfUnit : neighboursOf(smallestIndex, map)){
				if(map[oneDtoTwoD(neighboursOfUnit, map).x][oneDtoTwoD(neighboursOfUnit, map).y] == oppositeSign){
					adjacentEnemies.push_back(neighboursOfUnit);
				}
			}

			if(adjacentEnemies.size() > 0 && !alreadyFought){
				//If theres an enemy adjacent, target it
				std::vector<int> lowestHealthEnemy;
				int lowHealth = INT_MAX;
				for(auto& adjEn :adjacentEnemies){
					if(getHum(adjEn,allHumanoids, map)->hp == lowHealth){
						lowestHealthEnemy.push_back(adjEn);
					}
					if(getHum(adjEn,allHumanoids, map)->hp < lowHealth){
						lowHealth = getHum(adjEn, allHumanoids, map)->hp;
						lowestHealthEnemy.clear();
						lowestHealthEnemy.push_back(adjEn);
					}
				}
				target = getHum(chooseFirst(lowestHealthEnemy), allHumanoids, map);
				target->hp -= chosenUnit->dmg;
				if(target->hp <=0){ //dies
					map[target->pos.x][target->pos.y] = '.';

					if(std::find(units.begin(), units.end(), target) != units.end())
						units.erase(std::remove(units.begin(), units.end(), target), units.end());

					if(std::find(playedUnits.begin(), playedUnits.end(), target) != playedUnits.end())
						playedUnits.erase(std::remove(playedUnits.begin(), playedUnits.end(), target), playedUnits.end());

					if(std::find(allHumanoids.begin(), allHumanoids.end(), target) != allHumanoids.end())
						allHumanoids.erase(std::remove(allHumanoids.begin(), allHumanoids.end(), target), allHumanoids.end());

					if(std::find(goblins.begin(), goblins.end(), target) != goblins.end())
						goblins.erase(std::remove(goblins.begin(), goblins.end(), target), goblins.end());

					if(std::find(elfs.begin(), elfs.end(), target) != elfs.end())
						elfs.erase(std::remove(elfs.begin(), elfs.end(), target), elfs.end());
				}
			}
		}
		units = playedUnits;
		rounds++;
		resetMap(map);
		for(auto& pp : playedUnits){
			map[pp->pos.x][pp->pos.y] = pp->sign;
		}
		//std::cout << "ROUND " << rounds-1 << std::endl;
		printMap(map);
	}

	int sumHP = 0;
	for(auto remainingUnit : units){
		std::cout << remainingUnit->hp << std::endl;
		sumHP += remainingUnit->hp;
	}


	std::cout << "Rounds " << rounds - 2 << ". Sum HP: " << sumHP<<". Answer: " << (rounds -2) * sumHP << std::endl;
}
