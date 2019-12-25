## Read tries.txt to see me trying all the inputs. Solved today mostly by hand!

from intcode import IntcodeVM

file = open('input.txt', 'r')


memry = []

for line in file:
    memry = line.split(',')
    
comp = IntcodeVM(memry)

while True:
    comp.run()
    print(chr(comp.prgOutput),end="")
        