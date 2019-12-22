file = open('input.txt', 'r')

howManyCards = 10007
cards = [i for i in range(howManyCards)]

for line in file:
    command = line.split(" ")
    if command[0] == "cut":
        howMany = int(command[1])
        cards = cards[howMany:] + cards[:howMany]
    else:
        if command[1] == "into":
            cards.reverse()
        else:
            increment = int(command[3])
            oldDeck = cards.copy()
            for i in range(howManyCards):
                cards[(i*increment)%howManyCards] = oldDeck[i]

for index, card in enumerate(cards):
    if card == 2019:
        print(index)
        break
