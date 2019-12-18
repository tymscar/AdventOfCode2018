### My A* is a modified version of the one found at https://rosettacode.org/wiki/A*_search_algorithm#Python

from collections import defaultdict
import math

file = open('input.txt', 'r')

mapp = defaultdict(lambda: "#")

rows = 0
columns = 0
for line in file:
    columns = len(line)
    column = 0
    for character in line.rstrip().lstrip():
        mapp[(rows,column)] = character
        column += 1
    rows += 1

playerpos = (137,137)
keys = defaultdict(lambda: (0,0))
doors = defaultdict(lambda: (0,0))

for i in range(rows):
    for j in range(columns):
        if mapp[(i,j)] == "@":
            playerpos = (i,j)
        elif mapp[(i,j)].isalpha():
            if mapp[(i,j)].isupper():
                doors[mapp[(i,j)]] = (i,j)
            else:
                keys[mapp[(i,j)]] = (i,j)
        print(mapp[(i,j)],end="")
    print("")


def heuristic(start, goal):
    D = 1
    D2 = 1
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    return dx + dy

def get_vertex_neighbours(pos):
    n = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x2 = pos[0] + dx
        y2 = pos[1] + dy
        n.append((x2, y2))
    return n

def move_cost(b, keysOwned):
    if mapp[b] == "#":
        return 999999
    elif mapp[b] == "." or mapp[b] == "@":
        return 1
    elif mapp[b].islower():
        return 1
    else:
        if mapp[b].lower() in keysOwned:
            return 1
        return 999999


def AStarSearch(start, end, keysOwned):
    G = {}
    F = {}

    G[start] = 0
    F[start] = heuristic(start, end)

    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}

    while len(openVertices) > 0:
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        if current == end:
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.pop()
            path.reverse()
            return path  # Done!

        openVertices.remove(current)
        closedVertices.add(current)

        for neighbour in get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue
            candidateG = G[current] + move_cost(neighbour,keysOwned)

            if candidateG >= 999999:
                continue

            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue

            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    return []



def diff(first, second):
    return [item for item in first if item not in second]

def allDoorsUnlockedBetween(startPos,endPos,keysOwned):
    global doorsBetween
    global mapp
    for door in doorsBetween[startPos,endPos]:
        if mapp[door].lower() not in keysOwned:
            return False
    return True



def keysInReach(pos, keysHave):
    return [inReach for inReach in diff(keys,keysHave) if allDoorsUnlockedBetween(pos,keys[inReach],keysHave) and inReach not in keysHave]

def search(firstKey, keysIHave, fromWhere, distanceSoFar):
    global totals
    global moveCache
    global distanceBetween

    movesHere = distanceBetween[fromWhere[quadOf[keys[firstKey]]], keys[firstKey]] + distanceSoFar
    
    keysIHave.append(firstKey)

    if moveCache[(frozenset(keysIHave),firstKey)] >= movesHere:
        moveCache[(frozenset(keysIHave),firstKey)]  = movesHere
    else:
        return

    fromWhere[quadOf[keys[firstKey]]] = keys[firstKey]
    reachableKeysIdontHave = []
    reachableKeysIdontHave.append(keysInReach(fromWhere[0],keysIHave))
    reachableKeysIdontHave.append(keysInReach(fromWhere[1],keysIHave))
    reachableKeysIdontHave.append(keysInReach(fromWhere[2],keysIHave))
    reachableKeysIdontHave.append(keysInReach(fromWhere[3],keysIHave))

    #print(reachableKeysIdontHave)
    if len(reachableKeysIdontHave) == 0:
        if len(keysIHave) == len(keys):
            totals.append(movesHere)
        else:
            totals.append(999999)
    else:
        for key in reachableKeysIdontHave:
            search(key, keysIHave.copy(),fromWhere.copy(), movesHere)


ownedKeys = []
totals = [999999]
moveCache = defaultdict(lambda: 999999)
distanceBetween = defaultdict(lambda: 0)
doorsBetween = defaultdict(lambda: [])
quadOf = defaultdict(lambda: -1)
posOfPlayer = [(0,0),(0,0),(0,0),(0,0)]

posOfPlayer[0] = (playerpos[0]-1,playerpos[1]-1)
posOfPlayer[1] = (playerpos[0]-1,playerpos[1]+1)
posOfPlayer[2] = (playerpos[0]+1,playerpos[1]+1)
posOfPlayer[3] = (playerpos[0]+1,playerpos[1]-1)
mapp[playerpos] = "#"

keys["@"] = posOfPlayer[0]
keys["%"] = posOfPlayer[1]
keys["^"] = posOfPlayer[2]
keys["&"] = posOfPlayer[3]
for key1 in keys:
    for key2 in keys:
        if key1 != key2:
            if distanceBetween[keys[key1],keys[key2]] == 0:
                road = AStarSearch(keys[key1], keys[key2], keys)
                listOfDoors = []
                for point in road:
                    if mapp[point].isalpha():
                        if mapp[point].isupper():
                            listOfDoors.append(point)
                distanceBetween[keys[key1],keys[key2]] = len(road)
                distanceBetween[keys[key2],keys[key1]] = len(road)
                doorsBetween[keys[key1],keys[key2]] = listOfDoors
                doorsBetween[keys[key2],keys[key1]] = listOfDoors
    if keys[key1][0] < playerpos[0]:
        if keys[key1][1] < playerpos[1]:
            quadOf[keys[key1]] = 1
        else:
            quadOf[keys[key1]] = 2
    else:
        if keys[key1][1] < playerpos[1]:
            quadOf[keys[key1]] = 4
        else:
            quadOf[keys[key1]] = 3

for door1 in doors:
    if doors[door1][0] < playerpos[0]:
        if doors[door1][1] < playerpos[1]:
            quadOf[doors[door1]] = 1
        else:
            quadOf[doors[door1]] = 2
    else:
        if doors[door1][1] < playerpos[1]:
            quadOf[doors[door1]] = 4
        else:
            quadOf[doors[door1]] = 3 
print("Done marking distances and assigning doors and quads")
keys.pop("@")
keys.pop("%")
keys.pop("^")
keys.pop("&")



for key in keysInReach(playerpos,ownedKeys):
    moves = search(key, ownedKeys.copy(),posOfPlayer.copy(),0)



totals.sort()
print(totals[0])
