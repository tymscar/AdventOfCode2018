### My A* is a modified version of the one found at https://rosettacode.org/wiki/A*_search_algorithm#Python


from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

for line in file:
    memry = line.split(',')


class AStarGraph(object):
    # Define a class board like grid with two barriers

    def __init__(self, basedOnGrid):
        self.walkable = []
        for spot in basedOnGrid:
            if basedOnGrid[spot] == 1:
                self.walkable.append(spot)

    def heuristic(self, start, goal):
        # MAYBE CHANGE
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def get_vertex_neighbours(self, pos):
        n = []
        # Moves allow link a chess king
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        if b in self.walkable:
            return 1
        return 999999


def AStarSearch(start, end, graph):
    G = {}
    F = {}

    G[start] = 0
    F[start] = graph.heuristic(start, end)

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
            path.reverse()
            return path  # Done!

        openVertices.remove(current)
        closedVertices.add(current)

        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue
            candidateG = G[current] + graph.move_cost(current, neighbour)

            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue

            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    return []





def addPos(one, two):
    return one[0] + two[0], one[1] + two[1]


def positionQueried(direction):
    global rob
    offset = (0, 0)
    if direction == 1:
        offset = (0, 1)
    if direction == 2:
        offset = (0, -1)
    if direction == 3:
        offset = (-1, 0)
    if direction == 4:
        offset = (1, 0)
    return addPos(rob, offset)


def getLeft():
    global facing
    if facing == 1:
        return 3
    if facing == 2:
        return 4
    if facing == 3:
        return 2
    if facing == 4:
        return 1

def getRight():
    global facing
    if facing == 1:
        return 4
    if facing == 2:
        return 3
    if facing == 3:
        return 1
    if facing == 4:
        return 2



def drawMap(special):
    global grid
    smallestx = 9999
    smallesty = 9999
    biggestx = -9999
    biggesty = -9999
    for space in grid:
        if grid[space] != -1:
            if space[0] < smallestx:
                smallestx = space[0]
            if space[0] > biggestx:
                biggestx = space[0]
            if space[1] < smallesty:
                smallesty = space[1]
            if space[1] > biggesty:
                biggesty = space[1]
    for i in range(smallestx-5, biggestx+5):
        for j in range(smallesty-5, biggesty+5):
            if (i,j) in special:
                print("@",end="")
            elif grid[(i, j)] == -1:
                print(" ", end="")
            elif grid[(i, j)] == 0:
                print(" ", end="")
            elif grid[(i, j)] == 2:
                print("@", end="")
            else:
                print("▓", end="")
        print("")


grid = defaultdict(lambda: -1)
robot = IntcodeVM(memry)
startPos = (0,0)
grid[startPos] = 1
rob = startPos
OXYGEN = (1234,1234)
facing = 1

while True:
    robot.run(getLeft())
    if robot.prgOutput == 2: #finished
        rob = positionQueried(getLeft())
        facing = getLeft()
        OXYGEN = rob
        grid[OXYGEN] = 1
        break;
    elif robot.prgOutput == 0:
        grid[positionQueried(getLeft())] = 0
        robot.run(facing)
        if robot.prgOutput == 2: #finished
            rob = positionQueried(facing)
            OXYGEN = rob
            grid[OXYGEN] = 1
            break;
        elif robot.prgOutput == 0:
            grid[positionQueried(facing)] = 0
            facing = getRight()
        elif robot.prgOutput == 1:
            grid[positionQueried(facing)] = 1
            rob = positionQueried(facing)
    elif robot.prgOutput == 1:
        grid[positionQueried(getLeft())] = 1
        rob = positionQueried(getLeft())
        facing = getLeft()



graphA = AStarGraph(grid)
print(len(AStarSearch(startPos,OXYGEN,graphA))-1)