file = open('input.txt', 'r')
keypad = [["#", "#", "#", "#", "#", "#", "#"], ["#", "#", "#", "1", "#", "#", "#"], ["#", "#", "2", "3", "4", "#", "#"], ["#", "5", "6", "7", "8", "9", "#"], ["#", "#", "A", "B", "C", "#", "#"], ["#", "#", "#", "D", "#", "#", "#"], ["#", "#", "#", "#", "#", "#", "#"]]
pos = [3,1]

def part1():
    ans = []

    for line in file:
        line = line.strip("\n")
        for char in line:
            if char == "L" and keypad[pos[0]][pos[1] - 1] != "#":
                pos[1] -= 1
            elif char == "R" and keypad[pos[0]][pos[1] + 1] != "#":
                pos[1] += 1
            elif char == "U" and keypad[pos[0] - 1][pos[1]] != "#":
                pos[0] -= 1
            elif char == "D" and keypad[pos[0] + 1][pos[1]] != "#":
                pos[0] += 1
        ans.append(keypad[pos[0]][pos[1]])
        
        
                
    return "".join(ans)
    
print(part1())