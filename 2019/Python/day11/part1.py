from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')

currentLocation = (0,0)
facing = 0
panels =  defaultdict(int)

robot = IntcodeVM(memry)


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

print(len(panels) - 1)