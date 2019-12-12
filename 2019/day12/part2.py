import math
from collections import defaultdict
from parse import *

def lcm(listOfValues):
    lowComDen = listOfValues[0]
    for i in listOfValues[1:]:
        lowComDen = int(int(lowComDen) * i / math.gcd(int(lowComDen), i))
    return lowComDen


file = open('input.txt','r')

class Moon():
    def __init__(self, x, y, z):
        self.posX = x
        self.posY = y
        self.posZ = z
        self.velX = 0
        self.velY = 0
        self.velZ = 0
        self.name = ""

moons = []


for line in file:
    parsedLine = parse("<x={}, y={}, z={}>",line)
    point = Moon(int(parsedLine[0]), int(parsedLine[1]), int(parsedLine[2]))
    moons.append(point)

moons[0].name = "Io"
moons[1].name = "Europa"
moons[2].name = "Ganymede"
moons[3].name = "Callisto"


statesX = defaultdict(bool)
statesY = defaultdict(bool)
statesZ = defaultdict(bool)

statesX[(moons[0].posX, moons[1].posX, moons[2].posX, moons[3].posX, moons[0].velX, moons[1].velX, moons[2].velX, moons[3].velX)] = True
statesY[(moons[0].posY, moons[1].posY, moons[2].posY, moons[3].posY, moons[0].velY, moons[1].velY, moons[2].velY, moons[3].velY)] = True
statesZ[(moons[0].posZ, moons[1].posZ, moons[2].posZ, moons[3].posZ, moons[0].velZ, moons[1].velZ, moons[2].velZ, moons[3].velZ)] = True

xRepeat = -1
yRepeat = -1
zRepeat = -1


step = 0

while xRepeat == -1 or yRepeat == -1 or zRepeat == -1:
    for moonOne in moons:
        for moonTwo in moons:
            if moonOne.name != moonTwo.name:
                if moonOne.posX > moonTwo.posX:
                    moonOne.velX -= 1
                if moonOne.posX < moonTwo.posX:
                    moonOne.velX += 1
                if moonOne.posY > moonTwo.posY:
                    moonOne.velY -= 1
                if moonOne.posY < moonTwo.posY:
                    moonOne.velY += 1
                if moonOne.posZ > moonTwo.posZ:
                    moonOne.velZ -= 1
                if moonOne.posZ < moonTwo.posZ:
                    moonOne.velZ += 1

    for moon in moons:
        moon.posX += moon.velX
        moon.posY += moon.velY
        moon.posZ += moon.velZ
    step += 1

    if xRepeat == -1:
        thisXState = (moons[0].posX, moons[1].posX, moons[2].posX, moons[3].posX, moons[0].velX, moons[1].velX, moons[2].velX, moons[3].velX)
        if statesX[thisXState]:
            xRepeat = step
        else:
            statesX[thisXState] = True

    if yRepeat == -1:
        thisYState = (moons[0].posY, moons[1].posY, moons[2].posY, moons[3].posY, moons[0].velY, moons[1].velY, moons[2].velY, moons[3].velY)
        if statesY[thisYState]:
            yRepeat = step
        else:
            statesY[thisYState] = True

    if zRepeat == -1:
        thisZState = (moons[0].posZ, moons[1].posZ, moons[2].posZ, moons[3].posZ, moons[0].velZ, moons[1].velZ, moons[2].velZ, moons[3].velZ)
        if statesZ[thisZState]:
            zRepeat = step
        else:
            statesZ[thisZState] = True

print("System repeats after ", lcm([int(xRepeat),int(yRepeat),int(zRepeat)]), " steps")
