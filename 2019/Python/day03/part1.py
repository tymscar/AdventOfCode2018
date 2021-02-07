import math
from parse import *
from collections import defaultdict


file = open('input.txt','r')

strandOneInstruction = file.readline().rstrip().split(",")

strandTwoInstruction = file.readline().rstrip().split(",")

strandOne = defaultdict(int)
strandTwo = defaultdict(int)

def distanceToBase(fromPoint):
	return abs(fromPoint[0]) + abs(fromPoint[1])
	
	

currentPos = (0,0)
for instruction in strandOneInstruction:
	currx = currentPos[0]
	curry = currentPos[1]
	leftRight = instruction[0]
	
	if leftRight == "L":
		newX = currentPos[0] - int(parse("L{}",instruction)[0])
		while currentPos[0] > newX:
			currx -= 1
			currentPos = (currx,curry)
			strandOne[currentPos] += 1
	
	if leftRight == "R":
		newX = currentPos[0] + int(parse("R{}", instruction)[0])
		while currentPos[0] < newX:
			currx += 1
			currentPos = (currx,curry)
			strandOne[currentPos] += 1
		
	if leftRight == "U":
		newY = currentPos[1] + int(parse("U{}", instruction)[0])
		while currentPos[1] < newY:
			curry += 1
			currentPos = (currx,curry)
			strandOne[currentPos] += 1
		
	if leftRight == "D":
		newY = currentPos[1] - int(parse("D{}", instruction)[0])
		while currentPos[1] > newY:
			curry -= 1
			currentPos = (currx,curry)
			strandOne[currentPos] += 1
		
	currentPos = (currx,curry)
	strandOne[currentPos] += 1
	

currentPos = (0,0)
for instruction in strandTwoInstruction:
	currx = currentPos[0]
	curry = currentPos[1]
	leftRight = instruction[0]
	
	if leftRight == "L":
		newX = currentPos[0] - int(parse("L{}",instruction)[0])
		while currentPos[0] > newX:
			currx -= 1
			currentPos = (currx,curry)
			strandTwo[currentPos] += 1
	
	if leftRight == "R":
		newX = currentPos[0] + int(parse("R{}", instruction)[0])
		while currentPos[0] < newX:
			currx += 1
			currentPos = (currx,curry)
			strandTwo[currentPos] += 1
		
	if leftRight == "U":
		newY = currentPos[1] + int(parse("U{}", instruction)[0])
		while currentPos[1] < newY:
			curry += 1
			currentPos = (currx,curry)
			strandTwo[currentPos] += 1
		
	if leftRight == "D":
		newY = currentPos[1] - int(parse("D{}", instruction)[0])
		while currentPos[1] > newY:
			curry -= 1
			currentPos = (currx,curry)
			strandTwo[currentPos] += 1
		
	currentPos = (currx,curry)
	strandTwo[currentPos] += 1


	

matches = []

for posOne in strandOne:
		if strandTwo[posOne] > 0:
			matches.append(posOne)
			
			
closestMatch = matches[0]

for match in matches:
	if distanceToBase(match) < distanceToBase(closestMatch):
		closestMatch = match
		
print(distanceToBase(closestMatch))
