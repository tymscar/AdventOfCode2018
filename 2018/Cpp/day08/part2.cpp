#include <iostream>
#include <string>
#include <fstream>
#include <vector>

struct node{
	int nrk,nrm;
	std::vector<node> kids;
	std::vector<int> meta;
};

node createNode(std::ifstream& f){
	node tempNode;
	std::string line;
	f >> line;
	tempNode.nrk = std::stoi(line);
	f >> line;
	tempNode.nrm = std::stoi(line);
	for(int i=0; i<tempNode.nrk; i++){
		tempNode.kids.push_back(createNode(f));
	}
	for(int i=0;i<tempNode.nrm; i++){
		f >> line;
		tempNode.meta.push_back(std::stoi(line));
	}
	return tempNode;
}

int findVal(node& travNode){
	int sum = 0;
	if(travNode.nrk == 0){
		for(int i=0; i<travNode.nrm; i++){
			sum += travNode.meta[i];
		}
		return sum;
	}
	for(int i=0;i<travNode.nrm; i++){
		if((travNode.meta[i] > 0) && (travNode.meta[i] <= travNode.nrk)){
			sum += findVal(travNode.kids[travNode.meta[i] -1]);	
		}	
	}
	return sum;

}

int main() {
    std::ifstream file;
    file.open("input.txt");
    std::string line;
    
    node root = createNode(file);

    std::cout << findVal(root);


    return 0;
}
