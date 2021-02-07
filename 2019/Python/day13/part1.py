from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')

robot = IntcodeVM(memry)

nrOfBlockTiles = 0

while robot.finished == False:
    robot.run(137)
    robot.run(137)
    robot.run(137)
    tileID = robot.prgOutput
    if tileID == 2:
        nrOfBlockTiles += 1

print(nrOfBlockTiles)