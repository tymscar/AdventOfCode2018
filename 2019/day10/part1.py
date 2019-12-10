from collections import defaultdict
import math

file = open('input.txt', 'r')
asteroids = []

lineNr = 0
for line in file:
    for i in range(0,len(line)-1):
        if line[i] == "#":
            asteroids.append((i,lineNr))
    lineNr +=1

lineOfSightDirections = defaultdict(list)

def checkIfSeen(by, what):
    xoff = by[0]
    yoff = by[1]
    tempWhat = (what[0] - xoff,what[1]-yoff)
    commonDen = math.gcd(tempWhat[0], tempWhat[1])
    directionOfWhat = (tempWhat[0]/commonDen,tempWhat[1]/commonDen)
    if directionOfWhat not in lineOfSightDirections[by]:
        lineOfSightDirections[by].append(directionOfWhat)


for asteroid in asteroids:
    for otherAsteroid in asteroids:
        if asteroid != otherAsteroid:
            checkIfSeen(asteroid,otherAsteroid)

mostDetected = 0
for asteroid in asteroids:
    if len(lineOfSightDirections[asteroid]) > mostDetected:
        mostDetected = len(lineOfSightDirections[asteroid])

print(mostDetected)