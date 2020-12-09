file = open('input.txt', 'r')

pos = [0,0]
rot = 0

for line in file:
    line = line.strip("\n").split(", ")
    for instruction in line:
        if instruction[0] == "L":
            rot = (rot - 1) % 4
        else:
            rot = (rot + 1) % 4
            
        if rot == 0:
            pos[1] += int(instruction[1:])
        elif rot == 1:
            pos[0] += int(instruction[1:])
        elif rot == 2:
            pos[1] -= int(instruction[1:])
        else:
            pos[0] -= int(instruction[1:])
    
print(abs(pos[0]) + abs(pos[1]))