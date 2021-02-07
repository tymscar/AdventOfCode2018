from intcode import IntcodeVM
from collections import defaultdict
from os import system
import sys



everyHowManyFrame = int(input("How fast do you want it?🙈\n"))

def drawScreen(values, score):
    system('clear')
    for j in range(0, 26):
        for i in range(0, 37):
            tile = tiles[(i, j)]
            if tile == 0:
                print("░", end="")
            if tile == 1:
                print("█", end="")
            if tile == 2:
                print("▒", end="")
            if tile == 3:
                print("▓", end="")
            if tile == 4:
                print("■", end="")
        print("")
    print("Score:", score)


file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')

tiles = defaultdict(int)

memry[0] = 2

robot = IntcodeVM(memry)
score = 0
ballPos = (0, 0)
playerPos = (0, 0)
playerInput = 0
frameCounter = 0

while robot.finished == False:
    robot.run(playerInput)
    xpos = robot.prgOutput
    robot.run(playerInput)
    ypos = robot.prgOutput
    robot.run(playerInput)
    tileID = robot.prgOutput
    pos = (xpos, ypos)

    if pos == (-1, 0):
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

    frameCounter += 1
    if frameCounter % everyHowManyFrame == 0:
        drawScreen(tiles,score)

drawScreen(tiles,score)