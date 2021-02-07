from collections import defaultdict

file = open('input.txt', 'r')

parents = defaultdict(str)

for line in file:
    inpt = line.split(')')
    inpt[1] = inpt[1].rstrip()
    parents[inpt[1]] = inpt[0]

def numberOfParentsTill(where, frm):
    jumps = 0
    currentMoon = frm
    while currentMoon != where:
        jumps += 1
        currentMoon = parents[currentMoon]
    return jumps - 1

def parentalHierarchy(forWho):
    theParents = []
    currentMoon = forWho
    while currentMoon != "COM":
        theParents.append(parents[currentMoon])
        currentMoon = parents[currentMoon]
    return theParents

myParents = parentalHierarchy("YOU")
myParents.reverse()
santasParents = parentalHierarchy("SAN")
santasParents.reverse()

firstCommon = "COM"
for i in range(1,len(myParents)-1):
    if myParents[i] != santasParents[i]:
        firstCommon = parents[myParents[i]]
        break;

print(numberOfParentsTill(firstCommon,"SAN") + numberOfParentsTill(firstCommon,"YOU"))
