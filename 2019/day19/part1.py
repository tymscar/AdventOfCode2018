from intcode import IntcodeVM


file = open('input.txt', 'r')

memry = []

for line in file:
    memry = line.split(',')

howBigIsTheScan = 50

UserInput = []

for i in range(howBigIsTheScan):
    for j in range(howBigIsTheScan):
        UserInput.append((i,j))

howManyTracks = 0

for spot in UserInput:
    robot = IntcodeVM(memry.copy())
    robot.updateInput([spot[0],spot[1]])
    robot.run()
    howManyTracks += robot.prgOutput

print(howManyTracks)

