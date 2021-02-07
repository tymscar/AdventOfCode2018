from collections import defaultdict
from math import ceil

file = open('input.txt', 'r')

makingUpOf = defaultdict(list)
minimumOf = defaultdict(int)
currentlyHave = defaultdict(int)
oreUsed = 0

for line in file:
    result = line.split("=>")[1].rstrip().lstrip()
    goingIn = []
    for elem in line.split("=>")[0].split(","):
        goingIn.append(elem.rstrip().lstrip())
    makingUpOf[result.split(" ")[1]] = goingIn
    minimumOf[result.split(" ")[1]] = int(result.split(" ")[0])


def makeElement(thisElem):
    global oreUsed
    for neededElem in makingUpOf[thisElem]:
        elem = neededElem.split(" ")[1]
        qty = int(neededElem.split(" ")[0])

        if currentlyHave[elem] >= qty:
            currentlyHave[elem] -= qty
        else:
            if elem == "ORE":
                oreUsed += qty
            else:
                howManyTimes = int(ceil((qty - currentlyHave[elem]) / minimumOf[elem]))
                for i in range(0,howManyTimes):
                    makeElement(elem)
                currentlyHave[elem] -= qty
    currentlyHave[thisElem] += minimumOf[thisElem]

makeElement("FUEL")
print(oreUsed)
