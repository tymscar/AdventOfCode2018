def part_1():
    input_file = open('input.txt').read().split('\n\n')
    player1 = [int(card) for card in input_file[0].split(":\n")[1].split("\n")]
    player2 = [int(card) for card in input_file[1].split(":\n")[1].split("\n")]

    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)




    if len(player1) != 0:
        winner = player1
    else:
        winner = player2

    winner_score = 0

    for i in range(len(winner)):
        winner_score += (len(winner) - i) * winner[i]

    return winner_score


print(part_1())