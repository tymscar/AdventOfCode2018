from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')

currentLocation = (0,0)
facing = 0
panels =  defaultdict(int)

robot = IntcodeVM(memry)
panels[currentLocation] = 1

while robot.finished == False:
    robot.run(panels[currentLocation])
    colourToPaint = robot.prgOutput
    robot.run(panels[currentLocation])
    turn = robot.prgOutput
    panels[currentLocation] = colourToPaint
    if turn == 0:
        facing -= 1
    if turn == 1:
        facing += 1
    facing = facing % 4
    if facing == 0:
        currentLocation = (currentLocation[0], currentLocation[1] + 1)
    if facing == 1:
        currentLocation = (currentLocation[0] + 1, currentLocation[1])
    if facing == 2:
        currentLocation = (currentLocation[0], currentLocation[1] - 1)
    if facing == 3:
        currentLocation = (currentLocation[0] - 1, currentLocation[1])


lowestCoord = (999,999)
highestCoord = (-999,-999)
for panel in panels:
    if panel[0] < lowestCoord[0]:
        lowestCoord = (panel[0], lowestCoord[1])
    if panel[1] < lowestCoord[1]:
        lowestCoord = (lowestCoord[0], panel[1])
    if panel[0] > highestCoord[0]:
        highestCoord = (panel[0], highestCoord[1])
    if panel[1] > highestCoord[1]:
        highestCoord = (highestCoord[0], panel[1])

for i in range(highestCoord[1]+1, lowestCoord[1] - 2, -1):
    for j in range(lowestCoord[0] - 1,highestCoord[0]+1):
        if panels[(j,i)] == 0:
            print("░",end="")
        else:
            print("▓",end="")
    print("")