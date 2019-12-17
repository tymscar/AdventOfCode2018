from intcode import IntcodeVM

file = open('input.txt', 'r')

memry = []

for line in file:
    memry = line.split(',')

memry[0] = 2
robot = IntcodeVM(memry)

UserInput = [65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 65, 44, 67, 44, 65, 44, 67, 44, 66, 10,
             76, 44, 49, 50, 44, 76, 44, 56, 44, 76, 44, 56, 10,
             76, 44, 49, 50, 44, 82, 44, 52, 44, 76, 44, 49, 50, 44, 82, 44, 54, 10,
             82, 44, 52, 44, 76, 44, 49, 50, 44, 76, 44, 49, 50, 44, 82, 44, 54, 10,
             110, 10]

robot.updateInput(UserInput)

while robot.finished == False:
    robot.run()

print(robot.prgOutput)