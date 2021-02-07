from intcode import IntcodeVM
from _collections import defaultdict

file = open('input.txt', 'r')

memry = []

for line in file:
    memry = line.split(',')


UserInput = []

def checkPoint(thisPoint):
    robot = IntcodeVM(memry.copy())
    robot.updateInput([thisPoint[0], thisPoint[1]])
    robot.run()
    return robot.prgOutput

def isTopRightCorner(thisPoint):
    if checkPoint((thisPoint[0], thisPoint[1] - 99)) == 0:
        return False
    else:
        if checkPoint((thisPoint[0] + 99, thisPoint[1] - 99)) == 0:
            return False
        else:
            return True

def findRightEdge(thisPoint):
    while True:
        old = checkPoint(thisPoint)
        new = checkPoint((thisPoint[0], thisPoint[1] + 1))
        if new != old and old == 1:
            return thisPoint
        else:
            thisPoint = (thisPoint[0], thisPoint[1] + 1)



def firstVisiblePoint():
    for i in range(1,50):
        for j in range(1,50):
            UserInput.append((i, j))

    for spot in UserInput:
        robot = IntcodeVM(memry.copy())
        robot.updateInput([spot[0], spot[1]])
        robot.run()
        if robot.prgOutput == 1:
            return (spot[0], spot[1])


def findSanta(searchPos):
    while True:
        if isTopRightCorner(searchPos):
            return searchPos
        else:
            searchPos = findRightEdge((searchPos[0] + 1,searchPos[1]))


startPoint = firstVisiblePoint()

santaPos = findSanta(findRightEdge(startPoint))
print((santaPos[0] * 10000) + (santaPos[1] - 99))