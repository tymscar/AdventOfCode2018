import math

def howMuchFuelFor(mass):
    reqForThis = math.floor(int(mass)/3) - 2
            
    if reqForThis <= 0:
        return 0
                            
    return reqForThis + howMuchFuelFor(reqForThis)

file = open('input.txt','r')

totalFuel = 0

for line in file:
    fuel = howMuchFuelFor(line)
    totalFuel += fuel

print(totalFuel)
