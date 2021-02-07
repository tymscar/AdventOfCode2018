from collections import defaultdict

file = open('input.txt', 'r')

numOfMinutes = 200
mapp = defaultdict(lambda: 0)
emptyMapp = defaultdict(lambda: 0)
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
        emptyMapp[(rows, column)] = 0
        column += 1
    rows += 1

mapps = defaultdict(lambda: emptyMapp.copy())
mapps[0] = mapp

def printMap(atDepth):
    global mapps
    print("Depth ", 0 - atDepth,":")
    for i in range(rows):
        for j in range(columns):
            if mapps[atDepth][(i, j)] == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")

def get_vertex_neighbours(pos, depth):
    if pos == (0, 0):
        return [(depth + 1, 2, 1), (depth + 1, 1, 2), (depth, 0, 1), (depth, 1, 0)]
    if pos == (0, 1):
        return [(depth, 0, 0), (depth + 1, 1, 2), (depth, 0, 2), (depth, 1, 1)]
    if pos == (0, 2):
        return [(depth, 0, 1), (depth + 1, 1, 2), (depth, 0, 3), (depth, 1, 2)]
    if pos == (0, 3):
        return [(depth, 0, 2), (depth + 1, 1, 2), (depth, 0, 4), (depth, 1, 3)]
    if pos == (0, 4):
        return [(depth + 1, 2, 3), (depth + 1, 1, 2), (depth, 0, 3), (depth, 1, 4)]
    
    if pos == (1, 0):
        return [(depth + 1, 2, 1), (depth, 0, 0), (depth, 1, 1), (depth, 2, 0)]
    if pos == (1, 1):
        return [(depth, 1, 0), (depth, 0, 1), (depth, 1, 2), (depth, 2, 1)]
    if pos == (1, 2):
        return [(depth, 1, 1), (depth, 0, 2), (depth, 1, 3), (depth - 1, 0, 0), (depth - 1, 0, 1), (depth - 1, 0, 2), (depth - 1, 0, 3), (depth - 1, 0, 4)]
    if pos == (1, 3):
        return [(depth, 1, 2), (depth, 0, 3), (depth, 1, 4), (depth, 2, 3)]
    if pos == (1, 4):
        return [(depth, 1, 3), (depth, 0, 4), (depth + 1, 2, 3), (depth, 2, 4)]
    
    if pos == (2, 0):
        return [(depth + 1, 2, 1), (depth, 1, 0), (depth, 2, 1), (depth, 3, 0)]
    if pos == (2, 1):
        return [(depth, 2, 0), (depth, 1, 1), (depth - 1, 0, 0), (depth - 1, 1, 0), (depth - 1, 2, 0), (depth - 1, 3, 0), (depth - 1, 4, 0), (depth, 3, 1)]
    if pos == (2, 3):
        return [(depth - 1, 0, 4), (depth - 1, 1, 4), (depth - 1, 2, 4), (depth - 1, 3, 4), (depth - 1, 4, 4), (depth, 1, 3), (depth, 2, 4), (depth, 3, 3)]
    if pos == (2, 4):
        return [(depth, 2, 3), (depth, 1, 4), (depth + 1, 2, 3), (depth, 3, 4)]
    
    if pos == (3, 0):
        return [(depth + 1, 2, 1), (depth, 2, 0), (depth, 3, 1), (depth, 4, 0)]
    if pos == (3, 1):
        return [(depth, 3, 0), (depth, 2, 1), (depth, 3, 2), (depth, 4, 1)]
    if pos == (3, 2):
        return [(depth, 3, 1), (depth - 1, 4, 0), (depth - 1, 4, 1), (depth - 1, 4, 2), (depth - 1, 4, 3), (depth - 1, 4, 4), (depth, 3, 3), (depth, 4, 2)]
    if pos == (3, 3):
        return [(depth, 3, 2), (depth, 2, 3), (depth, 3, 4), (depth, 4, 3)]
    if pos == (3, 4):
        return [(depth, 3, 3), (depth, 2, 4), (depth + 1, 2, 3), (depth, 4, 4)]
    
    if pos == (4, 0):
        return [(depth + 1, 2, 1), (depth, 3, 0), (depth, 4, 1), (depth + 1, 3, 2)]
    if pos == (4, 1):
        return [(depth, 4, 0), (depth, 3, 1), (depth, 4, 2), (depth + 1, 3, 2)]
    if pos == (4, 2):
        return [(depth, 4, 1), (depth, 3, 2), (depth, 4, 3), (depth + 1, 3, 2)]
    if pos == (4, 3):
        return [(depth, 4, 2), (depth, 3, 3), (depth, 4, 4), (depth + 1, 3, 2)]
    if pos == (4, 4):
        return [(depth, 4, 3), (depth, 3, 4), (depth + 1, 2, 3), (depth + 1, 3, 2)]

def simulate():
    global mapps
    antsTotal = 0
    newMapps = mapps.copy()
    for depth in range(-200, 201):
        newMapp = newMapps[depth].copy()
        for i in range(rows):
            for j in range(columns):
                pos = (i, j)
                if pos != (2,2):
                    bugsAdjacent = 0
                    for nei in get_vertex_neighbours(pos,depth):
                        bugsAdjacent += mapps[nei[0]][(nei[1],nei[2])]
                    if mapps[depth][pos] == 0 and 1 <= bugsAdjacent <= 2:
                        newMapp[pos] = 1
                    if mapps[depth][pos] == 1 and bugsAdjacent != 1:
                        newMapp[pos] = 0
        newMapps[depth] = newMapp
        for s in newMapp:
            antsTotal += newMapp[s]
    mapps = newMapps
    return antsTotal

numOfAnts = 0
for min in range(numOfMinutes):
    numOfAnts = simulate()
    
print("Number of ants after ",numOfMinutes," minutes is ",numOfAnts)