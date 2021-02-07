### (!B || !A || !C) && D
from intcode import IntcodeVM


file = open('input.txt', 'r')

memry = []

for line in file:
    memry = line.split(',')


robot = IntcodeVM(memry)

UserInput = []
answer = "NOT B J\nNOT A T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n"

for a in answer:
    UserInput.append(ord(a))

robot.updateInput(UserInput)

while robot.finished == False:
    robot.run()
    if robot.prgOutput < 255:
        print(chr(robot.prgOutput),end="")
    else:
        print(robot.prgOutput)

