from collections import defaultdict

def part2():
    file = open('input.txt', 'r')

    pos = [0,0]
    rot = 0
    visited = defaultdict(lambda: False)
    visited[tuple(pos)] = True
    for line in file:
        instr = line.strip("\n").split(", ")

    
    while True:
        line = instr
        for instruction in line:
            if instruction[0] == "L":
                rot = (rot - 1) % 4
            else:
                rot = (rot + 1) % 4
                
            if rot == 0:
                for i in range(int(instruction[1:])):
                    pos[1] += 1
                    if visited[tuple(pos)] == True:
                        return abs(pos[0]) + abs(pos[1])
                    visited[tuple(pos)] = True
            elif rot == 1:
                for i in range(int(instruction[1:])):
                    pos[0] += 1
                    if visited[tuple(pos)] == True:
                        return abs(pos[0]) + abs(pos[1])
                    visited[tuple(pos)] = True
            elif rot == 2:
                for i in range(int(instruction[1:])):
                    pos[1] -= 1
                    if visited[tuple(pos)] == True:
                        return abs(pos[0]) + abs(pos[1])
                    visited[tuple(pos)] = True
            else:
                for i in range(int(instruction[1:])):
                    pos[0] -= 1
                    if visited[tuple(pos)] == True:
                        return abs(pos[0]) + abs(pos[1])
                    visited[tuple(pos)] = True
            
            
    
    
print(part2())