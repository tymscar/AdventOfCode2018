### (!A && D) || (!B && D) || (!C && D && H)

from intcode import IntcodeVM


file = open('input.txt', 'r')

memry = []

for line in file:
    memry = line.split(',')


robot = IntcodeVM(memry)

UserInput = []
answer = "NOT A T\nNOT B J\nAND D J\nOR T J\nNOT C T\nAND D T\nAND H T\nOR T J\nRUN\n"

for a in answer:
    UserInput.append(ord(a))


robot.updateInput(UserInput)

while robot.finished == False:
    robot.run()
    if robot.prgOutput < 255:
        print(chr(robot.prgOutput),end="")
    else:
        print(robot.prgOutput)

