from parse import *

howManySteps = 1000

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

    def getPotEnergy(self):
        return abs(self.posX) + abs(self.posY) + abs(self.posZ)

    def getKinEnergy(self):
        return abs(self.velX) + abs(self.velY) + abs(self.velZ)

    def getTotEnergy(self):
        return self.getPotEnergy() * self.getKinEnergy()

moons = []



for line in file:
    parsedLine = parse("<x={}, y={}, z={}>",line)
    point = Moon(int(parsedLine[0]), int(parsedLine[1]), int(parsedLine[2]))
    moons.append(point)

moons[0].name = "Io"
moons[1].name = "Europa"
moons[2].name = "Ganymede"
moons[3].name = "Callisto"

for step in range(0,howManySteps):

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

totalSystemEnergy = 0
print("After ",howManySteps," total energy is: ",end="")
for moon in moons:
    totalSystemEnergy += moon.getTotEnergy()
print(totalSystemEnergy)