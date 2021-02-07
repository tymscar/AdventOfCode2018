file = open('input.txt', 'r')

imgWidth = 25
imgHeight = 6
layers = []

for line in file:
    line = line.rstrip()
    layers = [line[i:i+(imgHeight * imgWidth)] for i in range(0, len(line), (imgWidth * imgHeight))]

image = []
for i in range(0,len(layers[0])):
    for layer in layers:
        if layer[i] != "2":
            image.append(layer[i])
            break

rows = [image[i:i+(imgWidth)] for i in range(0, len(image), (imgWidth))]

for row in rows:
    for column in row:
        if column == "1":
            print("#",end="")
        else:
            print(" ",end="")
    print("")
print("")