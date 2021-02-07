import math


file = open('input.txt','r')

totalFuel = 0

for line in file:
    fuel = math.floor(int(line)/3) - 2
    totalFuel += fuel

print(totalFuel)
