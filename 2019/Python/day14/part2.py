from collections import defaultdict
from math import ceil

file = open('input.txt', 'r')

makingUpOf = defaultdict(list)
minimumOf = defaultdict(int)
oreUsed = 0

for line in file:
    result = line.split("=>")[1].rstrip().lstrip()
    goingIn = []
    for elem in line.split("=>")[0].split(","):
        goingIn.append(elem.rstrip().lstrip())
    for inn in goingIn:
        makingUpOf[result.split(" ")[1]].append((inn.split(" ")[1], int(inn.split(" ")[0])))
    minimumOf[result.split(" ")[1]] = int(result.split(" ")[0])


def minOreNeeded(thisElem, howMany, extra = None):
    if thisElem == "ORE":
        return howMany

    if thisElem == "FUEL":
        extra = defaultdict(int)

    if extra[thisElem] > howMany:
        howMany = 0
        extra[thisElem] -= howMany
        return 0
    else:
        howMany -= extra[thisElem]
        extra[thisElem] = 0

    howManyTimes = int(ceil(howMany / minimumOf[thisElem]))

    oreUsed = 0
    for elem, qty in makingUpOf[thisElem]:
        oreUsed += minOreNeeded(elem, qty*howManyTimes, extra)

    extra[thisElem] += howManyTimes * minimumOf[thisElem] - howMany

    return oreUsed


howMuchOreWeHave = 1000000000000
minFuel = int(howMuchOreWeHave / minOreNeeded("FUEL",1))
maxFuel = howMuchOreWeHave

while abs(minFuel - maxFuel) > 1:
    midWay = (minFuel + maxFuel)//2
    oreAtMidway = minOreNeeded("FUEL",midWay)
    if oreAtMidway > howMuchOreWeHave:
        maxFuel = midWay
    else:
        minFuel = midWay

print(minFuel)