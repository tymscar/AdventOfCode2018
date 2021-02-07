vowels = ["a","e","i","o","u"]
bad = ["ab", "cd", "pq", "xy"]


def is_nice(string):
    vow = 0
    in_a_row = False
    contains_bad = False
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            in_a_row = True
    for char in string:
        if char in vowels:
            vow += 1
    for bd in bad:
        if bd in string:
            contains_bad = True
            break
    if vow >= 3 and in_a_row == True and contains_bad == False:
        return True
    return False
    


nice = 0


file = open('input.txt', 'r')

for line in file:
    if is_nice(line.strip("\n")):
        nice+=1

    
print(nice)