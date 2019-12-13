from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')

tiles =  defaultdict(int)

memry[0] = 2

robot = IntcodeVM(memry)
score = 0
ballPos = (0,0)
playerPos = (0,0)
playerInput = 0

while robot.finished == False:
    robot.run(playerInput)
    xpos = robot.prgOutput
    robot.run(playerInput)
    ypos = robot.prgOutput
    robot.run(playerInput)
    tileID = robot.prgOutput
    pos = (xpos,ypos)

    if pos == (-1,0):
        score = tileID
    else:
        tiles[pos] = tileID
        if tileID == 4:
            ballPos = pos
        if tileID == 3:
            playerPos = pos

    if ballPos[0] < playerPos[0]:
        playerInput = -1
    if ballPos[0] == playerPos[0]:
        playerInput = 0
    if ballPos[0] > playerPos[0]:
        playerInput = 1

print("Final score: ",score)
