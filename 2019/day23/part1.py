from intcode import IntcodeVM
from collections import defaultdict

file = open('input.txt', 'r')


memry = []
computers = []
inputFrom = defaultdict(lambda: [])
NATInput = []

for line in file:
    memry = line.split(',')

for i in range(50):
    comp = IntcodeVM(memry.copy())
    comp.updateInput(i)
    computers.append(comp)


while len(NATInput) == 0:
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
                NATInput.append(xtoSend)
                NATInput.append(ytoSend)


print("Y value recieved by the NAT is ", NATInput[1])



