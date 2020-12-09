def is_nice(string):
    pairs = False
    repeat = False
    for i in range(len(string)-2):
        if string[i:i+2] in string[i+2:]:
            pairs = True
            break
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            repeat = True
            break
            
    if pairs and repeat:
        return True
    return False
    


nice = 0


file = open('input.txt', 'r')

for line in file:
    if is_nice(line.strip("\n")):
        nice+=1

    
print(nice)