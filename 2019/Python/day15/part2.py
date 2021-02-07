from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')

def addPos(one, two):
    return one[0] + two[0], one[1] + two[1]


def positionQueried(direction):
    global rob
    offset = (0, 0)
    if direction == 1:
        offset = (0, 1)
    if direction == 2:
        offset = (0, -1)
    if direction == 3:
        offset = (-1, 0)
    if direction == 4:
        offset = (1, 0)
    return addPos(rob, offset)


def getLeft():
    global facing
    if facing == 1:
        return 3
    if facing == 2:
        return 4
    if facing == 3:
        return 2
    if facing == 4:
        return 1

def getRight():
    global facing
    if facing == 1:
        return 4
    if facing == 2:
        return 3
    if facing == 3:
        return 1
    if facing == 4:
        return 2

def getNeighborRooms(thisRoom):
    rooms = []
    rooms.append((thisRoom[0], thisRoom[1] + 1))
    rooms.append((thisRoom[0], thisRoom[1] - 1))
    rooms.append((thisRoom[0] + 1, thisRoom[1]))
    rooms.append((thisRoom[0] - 1, thisRoom[1]))
    return rooms


def drawMap(special):
    global grid
    smallestx = 9999
    smallesty = 9999
    biggestx = -9999
    biggesty = -9999
    for space in grid:
        if grid[space] != -1:
            if space[0] < smallestx:
                smallestx = space[0]
            if space[0] > biggestx:
                biggestx = space[0]
            if space[1] < smallesty:
                smallesty = space[1]
            if space[1] > biggesty:
                biggesty = space[1]
    for i in range(smallestx-5, biggestx+5):
        for j in range(smallesty-5, biggesty+5):
            if (i,j) in special:
                print("@",end="")
            elif grid[(i, j)] == -1:
                print(" ", end="")
            elif grid[(i, j)] == 0:
                print(" ", end="")
            elif grid[(i, j)] == 2:
                print("@", end="")
            else:
                print("▓", end="")
        print("")


grid = defaultdict(lambda: -1)
robot = IntcodeVM(memry)
startPos = (0,0)
grid[startPos] = 1
rob = startPos
OXYGEN = (1234,1234)
facing = 1

while True:
    robot.run(getLeft())
    if robot.prgOutput == 2:
        rob = positionQueried(getLeft())
        facing = getLeft()
        OXYGEN = rob
        grid[OXYGEN] = 1
    elif robot.prgOutput == 0:
        grid[positionQueried(getLeft())] = 0
        robot.run(facing)
        if robot.prgOutput == 2:
            rob = positionQueried(facing)
            OXYGEN = rob
            grid[OXYGEN] = 1
        elif robot.prgOutput == 0:
            grid[positionQueried(facing)] = 0
            facing = getRight()
        elif robot.prgOutput == 1:
            grid[positionQueried(facing)] = 1
            rob = positionQueried(facing)
            if rob == startPos:
                break
    elif robot.prgOutput == 1:
        grid[positionQueried(getLeft())] = 1
        rob = positionQueried(getLeft())
        facing = getLeft()
        if rob == startPos:
            break

howManyRooms = 0
for place in grid:
    if grid[place] == 1:
        howManyRooms += 1
roomsWithOxygen = [OXYGEN]

minutes = 0
while len(roomsWithOxygen) < howManyRooms:
    roomsToBeAdded = []
    for oxygenatedRoom in roomsWithOxygen:
        for neighborRoom in getNeighborRooms(oxygenatedRoom):
            if grid[neighborRoom] == 1 and neighborRoom not in roomsWithOxygen:
                roomsToBeAdded.append(neighborRoom)
    for roomToBeAdded in roomsToBeAdded:
        roomsWithOxygen.append(roomToBeAdded)
    minutes += 1



print(minutes)