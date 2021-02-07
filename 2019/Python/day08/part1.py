file = open('input.txt', 'r')

imgWidth = 25
imgHeight = 6
layers = []

for line in file:
    line = line.rstrip()
    layers = [line[i:i+(imgHeight * imgWidth)] for i in range(0, len(line), (imgWidth * imgHeight))]

leastNumOfZero = imgHeight * imgWidth
layerWithFewestZeroes = 0

for i in range(0,len(layers)):
    zeroes = 0
    for char in layers[i]:
        if char == "0":
            zeroes += 1
    if zeroes < leastNumOfZero:
        leastNumOfZero = zeroes
        layerWithFewestZeroes = i

numOfOnes = 0
numOfTwos = 0
for char in layers[layerWithFewestZeroes]:
    if char == "1":
        numOfOnes += 1
    if char == "2":
        numOfTwos += 1

print(numOfOnes * numOfTwos)