### mod inv from https://rosettacode.org/wiki/Modular_inverse#Python

from collections import defaultdict

file = open('input.txt', 'r')

positionToFind = 2020
howManyCards = 119315717514047
howManyTimes = 101741582076661
moves = defaultdict(lambda: ("",0))
seen = defaultdict(lambda: 0)

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


comNum = 0
for line in file:
    command = line.split(" ")
    if command[0] == "cut":
        howMany = int(command[1])
        moves[comNum] = ("cut", howMany)
    else:
        if command[1] == "into":
            moves[comNum] = ("inc", howManyCards - 1)
            comNum += 1
            moves[comNum] = ("cut", 1)
        else:
            increment = int(command[3])
            moves[comNum] = ("inc", increment)
    comNum += 1

commands = []
for m in moves:
    commands.append(moves[m])


def compress(com):
    commands = com

    while len(commands) > 2:
        newCommands = []
        if commands[0][0] == "cut":
            currComm = (commands[0][0], 0)
        else:
            currComm = (commands[0][0], 1)
        for c in commands:
            if c[0] != currComm[0]:
                newCommands.append(currComm)
                currComm = c
            else:
                if c[0] == "cut":
                    currComm = (c[0], (c[1] + currComm[1]) % howManyCards)
                else:
                    currComm = (c[0], (c[1] * currComm[1]) % howManyCards)
        newCommands.append(currComm)
        commands = newCommands
        if len(commands) > 2:
            for i in range(0, len(commands) // 2 + 1):
                if commands[i][0] == "cut":
                    temp = (commands[i][0], (commands[i][1] * commands[i + 1][1]) % howManyCards)
                    commands[i] = commands[i + 1]
                    commands[i + 1] = temp
                    break

    return commands


hugeComm = defaultdict(lambda: [])
hugeComm[0] = compress(commands)

finalCommands = []

for i in range(1, 48):
    hugeComm[i] = hugeComm[i - 1] * 2
    hugeComm[i] = compress(hugeComm[i])

for i in range(47, -1, -1):
    if pow(2, i) <= howManyTimes:
        howManyTimes -= pow(2, i)
        finalCommands += hugeComm[i]

finalAnswer = compress(finalCommands)
finalCommands.reverse()

for command in finalCommands:
    if command[0] == "cut":
        howMany = int(command[1])
        positionToFind = (positionToFind + howMany) % howManyCards
    else:
        increment = int(command[1])
        positionToFind = (positionToFind * modinv(increment, howManyCards)) % howManyCards
            
print(positionToFind)