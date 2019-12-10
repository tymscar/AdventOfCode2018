from collections import defaultdict
import math

file = open('input.txt', 'r')
asteroids = []

height = 0
length = 0
for line in file:
    length = len(line) - 1
    for i in range(0,len(line)-1):
        if line[i] == "#":
            asteroids.append((i,height))
    height +=1

lineOfSightDirections = defaultdict(list)
asteroidsSeenFrom = defaultdict(list)

def checkIfSeen(by, what):
    if by == what:
        return (0,0)
    xoff = by[0]
    yoff = by[1]
    tempWhat = (what[0] - xoff,what[1]-yoff)
    commonDen = math.gcd(tempWhat[0], tempWhat[1])
    directionOfWhat = (tempWhat[0]/commonDen,tempWhat[1]/commonDen)
    if directionOfWhat not in lineOfSightDirections[by]:
        return directionOfWhat
    return (0,0)


for asteroid in asteroids:
    for otherAsteroid in asteroids:
        if asteroid != otherAsteroid:
            dirr = checkIfSeen(asteroid,otherAsteroid)
            if dirr != (0,0):
                lineOfSightDirections[asteroid].append(dirr)

myLocation = (0,0)
mostDetected = 0
for asteroid in asteroids:
    if len(lineOfSightDirections[asteroid]) > mostDetected:
        myLocation = asteroid
        mostDetected = len(lineOfSightDirections[asteroid])

def angleBetween(a, b):
    return (180-math.degrees(math.atan2((a[0] - b[0]), (a[1] - b[1]))))%360

def angleToHome(aster):
    return angleBetween(aster,myLocation)


destoroyed = []

while len(asteroids) != 1:
    lineOfSightDirections.clear()
    seenFromHome = []
    for asteroid in asteroids:
        dirr = checkIfSeen(myLocation, asteroid)
        if dirr != (0, 0):
            lineOfSightDirections[myLocation].append(dirr)

    for vectors in lineOfSightDirections[myLocation]:

        for i in range(1,length+height):
            if (vectors[0] * i + myLocation[0],vectors[1] * i + myLocation[1]) in asteroids:
                seenFromHome.append((vectors[0] * i + myLocation[0],vectors[1] * i + myLocation[1]))
                break

    seenFromHome.sort(key=angleToHome)

    for seen in seenFromHome:
        destoroyed.append(seen)
        asteroids.remove(seen)


print(int(destoroyed[199][0] * 100 + destoroyed[199][1]))