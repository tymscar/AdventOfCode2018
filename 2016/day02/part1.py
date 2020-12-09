file = open('input.txt', 'r')
keypad = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
pos = [1,1]

def part1():
    ans = []

    for line in file:
        line = line.strip("\n")
        for char in line:
            if char == "L":
                pos[1] -= 1
            elif char == "R":
                pos[1] += 1
            elif char == "U":
                pos[0] -= 1
            else:
                pos[0] += 1
            pos[0] = max(0, pos[0])
            pos[0] = min(pos[0], 2)
            pos[1] = max(0, pos[1])
            pos[1] = min(pos[1], 2)
        ans.append(keypad[pos[0]][pos[1]])
        
        
                
    return "".join(ans)
    
print(part1())