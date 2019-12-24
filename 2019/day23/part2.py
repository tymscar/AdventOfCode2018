from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')


memry = []
computers = []

inputFrom = defaultdict(lambda: [])
ysentFromNat = defaultdict(lambda: 0)


NATInputX = -137137137
NATInputY = -137137137

for line in file:
    memry = line.split(',')

for i in range(50):
    comp = IntcodeVM(memry.copy())
    comp.updateInput(i)
    computers.append(comp)

stopped = False

while not stopped:
    howManyPackagesInQueue = 0
    for i in range(50):
        computers[i].run()
        if computers[i].output:
            inputFrom[i].append(computers[i].prgOutput)
        if len(inputFrom[i]) >= 3:
            who = inputFrom[i].pop(0)
            xtoSend = inputFrom[i].pop(0)
            ytoSend = inputFrom[i].pop(0)
            if who != 255:
                computers[who].updateInput(xtoSend)
                computers[who].updateInput(ytoSend)
            else:
                NATInputX = xtoSend
                NATInputY = ytoSend
        howManyPackagesInQueue += len(computers[i].prgInputList)
        
    if howManyPackagesInQueue == 0 and NATInputY != -137137137:
        computers[0].updateInput(NATInputX)
        computers[0].updateInput(NATInputY)
        ysentFromNat[NATInputY] += 1
        if ysentFromNat[NATInputY] >= 4:
            print(NATInputY, " has been sent twice")
            stopped = True