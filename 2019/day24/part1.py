from collections import defaultdict

file = open('input.txt', 'r')

mapp = defaultdict(lambda: 0)
powof2 = defaultdict(lambda: 0)
seenBefore = defaultdict(lambda: 0)

rows = 0
columns = 0
for line in file:
    columns = len(line)
    column = 0
    for character in line:
        if character == "#":
            mapp[(rows, column)] = 1
        else:
            mapp[(rows, column)] = 0
        column += 1
    rows += 1

for i in range(rows * columns):
    powof2[i] = pow(2, i)


def get_vertex_neighbours(pos):
    n = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x2 = pos[0] + dx
        y2 = pos[1] + dy
        n.append((x2, y2))
    return n

def calculateBiodiversity():
    global mapp
    biodiv = 0
    for i in range(rows):
        for j in range(columns):
            biodiv += powof2[j + i * rows] * mapp[(i,j)]
    return biodiv


def simulate():
    global mapp
    newMapp = mapp.copy()
    for i in range(rows):
        for j in range(columns):
            pos = (i, j)
            bugsAdjacent = 0
            for nei in get_vertex_neighbours(pos):
                bugsAdjacent += mapp[nei]
            if mapp[pos] == 0 and 1 <= bugsAdjacent <= 2:
                newMapp[pos] = 1
            if mapp[pos] == 1 and bugsAdjacent != 1:
                newMapp[pos] = 0
    mapp = newMapp
    thisBioDiv = calculateBiodiversity()
    seenBefore[thisBioDiv] += 1
    if seenBefore[thisBioDiv] == 2:
        print(thisBioDiv)
        return False
    return True


while simulate():
    continue