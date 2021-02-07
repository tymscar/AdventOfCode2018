from collections import defaultdict

file = open('input.txt', 'r')

mapp = defaultdict(lambda: " ")

startPos = (0, 0)
endPos = (0, 0)

rows = 0
columns = 0
for line in file:
    columns = len(line)
    column = 0
    for character in line:
        mapp[(rows, column)] = character
        column += 1
    rows += 1

portalsOfName = defaultdict(lambda: set())
nextStep = defaultdict(lambda: (999, 999))


class Point:
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent


for i in range(-5, columns + 5):
    for j in range(-5, rows + 5):
        if mapp[(i, j)].isalpha():
            if mapp[(i + 1, j)].isalpha():  # am above
                if mapp[(i + 2, j)] == ".":  # am top
                    portalsOfName[mapp[(i, j)] + mapp[(i + 1, j)]].add((i + 2, j))
                else:  # am mid
                    portalsOfName[mapp[(i, j)] + mapp[(i + 1, j)]].add((i - 1, j))
            if mapp[(i - 1, j)].isalpha():  # am under
                if mapp[(i - 2, j)] == ".":  # am bot
                    portalsOfName[mapp[(i - 1, j)] + mapp[(i, j)]].add((i - 2, j))
                else:  # am mid
                    portalsOfName[mapp[(i - 1, j)] + mapp[(i, j)]].add((i + 1, j))
            if mapp[(i, j - 1)].isalpha():  # am right
                if mapp[(i, j - 2)] == ".":  # am rightmost
                    portalsOfName[mapp[(i, j - 1)] + mapp[(i, j)]].add((i, j - 2))
                else:  # am mid
                    portalsOfName[mapp[(i, j - 1)] + mapp[(i, j)]].add((i, j + 1))
            if mapp[(i, j + 1)].isalpha():  # am left
                if mapp[(i, j + 2)] == ".":  # am leftmost
                    portalsOfName[mapp[(i, j)] + mapp[(i, j + 1)]].add((i, j + 2))
                else:  # am mid
                    portalsOfName[mapp[(i, j)] + mapp[(i, j + 1)]].add((i, j - 1))

startPos = list(portalsOfName["AA"])[0]
endPos = list(portalsOfName["ZZ"])[0]

for portal in portalsOfName:
    if portal != "AA" and portal != "ZZ":
        ptsInPortal = list(portalsOfName[portal])
        nextStep[ptsInPortal[0]] = ptsInPortal[1]
        nextStep[ptsInPortal[1]] = ptsInPortal[0]


def getNeighbours(ofPosition):
    global mapp
    global nextStep

    neighs = []

    if ofPosition in nextStep:
        if mapp[nextStep[ofPosition]] == ".":
            neighs.append(nextStep[ofPosition])

    if mapp[ofPosition[0] + 1, ofPosition[1]] == ".":
        neighs.append((ofPosition[0] + 1, ofPosition[1]))
    if mapp[ofPosition[0], ofPosition[1] + 1] == ".":
        neighs.append((ofPosition[0], ofPosition[1] + 1))
    if mapp[ofPosition[0] - 1, ofPosition[1]] == ".":
        neighs.append((ofPosition[0] - 1, ofPosition[1]))
    if mapp[ofPosition[0], ofPosition[1] - 1] == ".":
        neighs.append((ofPosition[0], ofPosition[1] - 1))

    return neighs


def getPathFrom(start):
    global endPos

    queue = []

    queue.append(Point(start, None))

    while len(queue) > 0:
        p = queue.pop(0)
        if p.pos == endPos:
            return p
        for position in getNeighbours(p.pos):
            mapp[position] = "*"
            nextP = Point(position, p)
            queue.append(nextP)
    return None


steps = 0

point = getPathFrom(startPos)

while point.parent != None:
    steps += 1
    point = point.parent
    
print(steps)

