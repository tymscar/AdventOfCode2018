from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')

memry = []

for line in file:
    memry = line.split(',')

robot = IntcodeVM(memry)
map = defaultdict(lambda: 46)

rows = 0
realColumns = 0
columns = 0
while not robot.finished:
    robot.run()
    char = robot.prgOutput
    if char == 10:
        rows += 1
        columns = 0
    else:
        columns += 1
        if columns > realColumns:
            realColumns = columns
        map[(rows,columns)] = char

columns = realColumns
rows -= 2


def returnNeighbours(spot):
    neighs = []
    neighs.append((spot[0] + 1, spot[1]))
    neighs.append((spot[0], spot[1] + 1))
    neighs.append((spot[0] - 1, spot[1]))
    neighs.append((spot[0], spot[1] - 1))
    return neighs

alignmentParam = 0
for i in range(rows):
    for j in range(1,columns+1):
        neighboursMatch = 0
        for neigh in returnNeighbours((i,j)):
            if map[(i,j)] == map[neigh] == 35:
                neighboursMatch += 1
        if neighboursMatch == 4:
            alignmentParam += i * (j-1)

print(alignmentParam)